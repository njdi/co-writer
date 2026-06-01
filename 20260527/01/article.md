# 把 Codex 安装到 Docker 里：多账号隔离使用的一种办法

最近我在日常开发里用 Codex 比较多，但遇到了一个很现实的问题：我有多个 ChatGPT 账号，希望能把这些账号的额度和资源都利用起来，而 Codex 目前并不支持在同一个环境里同时登录多个账号。

我的解决办法比较简单粗暴：把 Codex 安装到 Docker 容器里。

这样做有两个好处。

第一，每个 Docker 容器可以登录一个独立的 ChatGPT 账号。只要启动多个容器，就可以得到多个彼此隔离的 Codex 环境。

第二，权限管理会更放心一些。Codex 需要在本地执行命令、读写文件，如果直接跑在宿主机上，总会担心它影响系统环境。放到 Docker 容器里之后，即使给它比较高的执行权限，它实际影响的也是容器内部环境；只要挂载好工作目录，就可以在安全边界内完成大部分开发任务。

下面记录一下完整安装过程。

## 先在 ChatGPT 里打开设备代码授权

在 Docker 环境里运行 Codex 时，通常没有办法直接打开浏览器完成 ChatGPT 登录，所以需要使用设备代码登录。

在开始之前，先登录 ChatGPT，然后进入安全设置，为 Codex 启用设备代码授权：

```text
设置 -> 安全 -> 为 Codex 启用设备代码授权
```

这个选项打开之后，后面才能通过设备码在容器里完成登录。

## 创建 Ubuntu 容器

先拉取 Ubuntu 24.04 镜像：

```bash
docker pull ubuntu:24.04
```

然后创建一个用于运行 Codex 的容器：

```bash
docker run -dit \
  --name codex-gsw \
  --hostname codex-gsw \
  -v $HOME/workspace:/workspace \
  -w /workspace \
  ubuntu:24.04 \
  tail -f /dev/null
```

这里我把宿主机的 `$HOME/workspace` 挂载到了容器里的 `/workspace`，并且把容器的工作目录也设置成了 `/workspace`。这样 Codex 在容器里工作时，读写的就是这个挂载目录。

如果你想给不同账号准备不同环境，可以把 `codex-gsw` 换成其他容器名，例如 `codex-account-a`、`codex-account-b`。

进入容器：

```bash
docker exec -it codex-gsw bash
```

## 安装 Node.js 和 Codex

进入容器之后，先安装 `curl`：

```bash
apt update && apt install -y curl
```

接着安装 nvm：

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.4/install.sh | bash
```

加载 nvm：

```bash
\. "$HOME/.nvm/nvm.sh"
```

安装 Node.js 24：

```bash
nvm install 24
```

最后全局安装 Codex：

```bash
npm i -g @openai/codex
```

到这里，Codex 就已经安装完成了。

## 启动 Codex 并选择设备码登录

在容器里执行：

```bash
codex
```

第一次启动时，会看到类似下面的提示：

```text
Welcome to Codex, OpenAI's command-line coding agent

Sign in with ChatGPT to use Codex as part of your paid plan
or connect an API key for usage-based billing

1. Sign in with ChatGPT
   Usage included with Plus, Pro, Business, and Enterprise plans

> 2. Sign in with Device Code
   Sign in from another device with a one-time code

3. Provide your own API key
   Pay for what you use

Press Enter to continue
```

这里选择第二项：

```text
Sign in with Device Code
```

需要注意的是，Docker 容器里通常没有桌面浏览器，所以不要选择普通的 ChatGPT 登录方式。设备码登录会让你在宿主机或其他设备的浏览器中完成授权。

选择之后，Codex 会输出一个登录链接和一次性代码：

```text
Welcome to Codex, OpenAI's command-line coding agent

Finish signing in via your browser

1. Open this link in your browser and sign in

https://auth.openai.com/codex/device

2. Enter this one-time code after you are signed in (expires in 15 minutes)

XXXX-XXXXX

Device codes are a common phishing target. Never share this code.

Press Esc to cancel
```

接下来在浏览器里打开：

```text
https://auth.openai.com/codex/device
```

登录对应的 ChatGPT 账号，然后输入容器里显示的一次性代码。

授权完成后，容器里的 Codex 会显示：

```text
Welcome to Codex, OpenAI's command-line coding agent

✓ Signed in with your ChatGPT account

Before you start:

Decide how much autonomy you want to grant Codex
For more details see the Codex docs

Codex can make mistakes
Review the code it writes and commands it runs

Powered by your ChatGPT account
Uses your plan's rate limits and training data preferences

Press Enter to continue
```

看到这个输出，就表示 Codex 已经成功登录。按回车之后，就可以在这个容器里正常使用 Codex 了。

## 多账号怎么用

如果你有多个 ChatGPT 账号，可以为每个账号创建一个独立容器。核心思路就是容器名、主机名和登录的 ChatGPT 账号一一对应。

例如再创建一个容器：

```bash
docker run -dit \
  --name codex-alt \
  --hostname codex-alt \
  -v $HOME/workspace:/workspace \
  -w /workspace \
  ubuntu:24.04 \
  tail -f /dev/null
```

然后重复前面的安装和登录步骤。这个新容器里的 Codex 登录另一个 ChatGPT 账号，就可以和 `codex-gsw` 分开使用。

当然，如果你希望不同账号处理不同项目，也可以给不同容器挂载不同目录：

```bash
-v $HOME/project-a:/workspace
```

或者：

```bash
-v $HOME/project-b:/workspace
```

这样文件权限和工作区也会更加清晰。

## 一点使用建议

把 Codex 放进 Docker 并不意味着可以完全不看它执行了什么。Codex 仍然可能生成错误代码，也可能执行不符合预期的命令，所以关键操作前最好确认一下。

不过相比直接运行在宿主机上，Docker 容器确实给了一个更明确的边界。你可以只挂载必要的工作目录，把系统环境和开发环境隔离开；也可以随时删除容器、重新创建一个干净环境。

对我来说，这个方案最大的价值是把多账号和环境隔离两个问题一起解决了。每个账号一个容器，每个容器一个独立 Codex，既方便切换，也不会把本机环境弄得太乱。
