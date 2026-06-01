# Docker 容器里访问本机端口：认识 host.docker.internal

在 Docker 容器里调试程序时，经常会遇到一个看起来很反直觉的问题：

宿主机上明明已经启动了一个服务，比如 MySQL 跑在：

```text
127.0.0.1:3306
```

但是进入容器之后，访问：

```bash
curl http://127.0.0.1:3306
```

却连不上。

原因很简单：**容器里的 `127.0.0.1` 不是你的电脑本机，而是容器自己。**

这时候就要用到 Docker 提供的一个特殊主机名：

```text
host.docker.internal
```

它的作用是：让容器可以访问 Docker 宿主机，也就是运行 Docker 的那台机器。

## 先搞懂 localhost 指向谁

很多问题都出在 `localhost` 这个词上。

在宿主机上：

```text
localhost
```

指的是宿主机自己。

但在容器里：

```text
localhost
```

指的是容器自己。

这两者不是同一个网络空间。Docker 容器默认有自己的网络环境，所以你在容器里访问 `127.0.0.1:3306`，实际上是在问：

> 这个容器里面有没有一个服务监听在 3306 端口？

如果 MySQL 是跑在宿主机上的，而不是跑在这个容器里的，那当然访问不到。

可以把关系简单理解成这样：

```text
宿主机 localhost              = 宿主机自己
容器内 localhost              = 容器自己
容器内 host.docker.internal  = 宿主机
```

所以，如果你的 MySQL 跑在宿主机的 `3306` 端口，容器里应该这样连：

```text
host.docker.internal:3306
```

## 一个实际例子

假设宿主机上启动了 MySQL：

```text
127.0.0.1:3306
```

在容器里连接它时，数据库地址不要写：

```text
127.0.0.1
```

而应该写：

```text
host.docker.internal
```

例如一个应用的数据库配置可以写成：

```env
DB_HOST=host.docker.internal
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=your_database
```

如果容器里安装了 MySQL 客户端，也可以直接测试：

```bash
mysql -h host.docker.internal -P 3306 -u root -p
```

## 小结

`host.docker.internal` 可以理解成 Docker 给容器准备的一个“宿主机入口”。

在容器里：

```text
localhost = 容器自己
host.docker.internal = 宿主机
```

所以，当你的服务跑在本机，比如 MySQL 的 `3306` 端口，而程序跑在 Docker 容器里时，就不要再写：

```text
127.0.0.1:3306
```

而应该写：

```text
host.docker.internal:3306
```
