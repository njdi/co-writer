# 翻译问题分析：自动改进的软件

## 问题列表

1. **"整个 agent 开发生命周期由五条指令覆盖"** — "覆盖"用词不当，原文 "covered by five instructions" 在此语境指"通过五条指令来完成"，应改为"五条指令涵盖了整个 agent 开发生命周期的全部环节"。

2. **"以极少的监督递归地改进我的 agent"** — "递归地"过于技术化，此处原文 "recursively" 取其比喻含义，表示反复循环，应改为"在几乎无需人工干预的情况下持续迭代改进我的 agent"。

3. **"每个关键操作都可以用 cURL 或 bash 运行"** — "bash" 首字母应大写为 Bash，保持一致性。

4. **"claude code 可以测试一个 agent，然后通过读取 sessions、traces 和日志来判断 PASS 或 FAIL"** — "claude code" 应为 "Claude Code"（大写），全文其他地方也应保持一致。

5. **"一个汇总隔夜 Slack 消息的 agent"** — "隔夜"表述略显奇怪，原文是 overnight Slack messages，应译为"汇总隔夜积压 Slack 消息的 agent"或"汇总当天 Slack 消息的 agent"。

6. **"有些是主路径探针，有些是边缘情况，有些是工具选择测试"** — 结构生硬，可改为"有些测试主路径，有些测试边缘情况，有些测试工具选择是否正确"。

7. **"对于每次失败，它选择一个调节手段"** — "调节手段"过于生硬，原文 "remediation" 指补救/修复措施，应改为"针对每次失败，它选择相应的修复手段"。

8. **"文档和代码之间的漂移一直是生产软件的税"** — "税"作为隐喻略显生硬，原文 "drift between docs and code has always been a tax on production software" 中 "tax" 意为额外负担/成本，可改为"文档与代码之间的偏离，历来是生产软件的隐性成本"。
