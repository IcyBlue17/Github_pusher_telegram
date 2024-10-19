![Github_pusher_telegram](https://socialify.git.ci/IcyBlue17/Github_pusher_telegram/image?description=1&descriptionEditable=%E9%85%8D%E5%90%88%20Github%20Webhook%20%E5%AE%9E%E7%8E%B0%E4%BB%93%E5%BA%93%20Commit%20%E6%B6%88%E6%81%AF%E7%9A%84%E6%8E%A8%E9%80%81%20Telegram%20%E6%9C%BA%E5%99%A8%E4%BA%BA&forks=1&issues=1&language=1&name=1&owner=1&pattern=Circuit%20Board&pulls=1&stargazers=1&theme=Light)

<p align="center">
  <img
    src="https://img.shields.io/github/last-commit/IcyBlue17/Github_pusher_telegram.svg?style=flat-square"
  />
  <img
    src="https://img.shields.io/github/issues-pr-closed/IcyBlue17/Github_pusher_telegram.svg?style=flat-square"
  />
  <img
    src="https://img.shields.io/github/commit-activity/w/IcyBlue17/Github_pusher_telegram?style=flat-square"
  />
  <br />
  <img
    src="https://img.shields.io/github/languages/code-size/IcyBlue17/Github_pusher_telegram.svg?style=flat-square"
  />
  <img
    src="https://img.shields.io/github/repo-size/IcyBlue17/Github_pusher_telegram?style=flat-square"
  />
  <img
    src="https://img.shields.io/github/languages/count/IcyBlue17/Github_pusher_telegram?style=flat-square"
  />
  <img
    src="https://img.shields.io/github/languages/top/IcyBlue17/Github_pusher_telegram?style=flat-square"
  />
  <img
    src="https://img.shields.io/github/issues/IcyBlue17/Github_pusher_telegram?style=flat-square"
  />
  <img
    src="https://img.shields.io/github/issues-closed-raw/IcyBlue17/Github_pusher_telegram?style=flat-square"
  />
  <br />
  ⭐️ 您的 Star 对我来说很有用！
</p>

## 部署

### Docker

您可以通过一行命令快速部署项目：

```bash
docker run -d
--name github-pusher
-e TOKEN=<你的 token>
-e CHATID=<你的 chat_id>
-p 1145:1145 \
icymichiko/github_pusher_telegram:latest
```

环境变量说明：

| 环境变量 | 说明                                                                   |
| :------- | :--------------------------------------------------------------------- |
| TOKEN    | Telegram Bot Token，可以通过 [@BotFather](https://t.me/BotFather) 获取  |
| CHATID   | Telegram Chat ID                                                       |


---

## 配置 GitHub 仓库 Webhook

为了让 GitHub 仓库的提交信息发送到 Telegram 机器人，你需要在你的 GitHub 仓库中配置 Webhook。

### 1. 获取 Webhook URL

部署项目后，记住暴露的端口，假设服务器 IP 地址为 `114.5.1.4`，那么此时的 Webhook URL 为：

```
http://114.5.1.4:暴露的端口/github
```


  可以根据情况自行反代（确保Webhook可用就行了）
### 2. 在 GitHub 仓库中添加 Webhook

1. 进入需要配置推送的 GitHub 仓库，点击 **Settings**。

2. 找到 **Webhooks** 点击 **Add webhook**。

3. 在 **Payload URL** 中输入上一步获取的Webhook URL（例如 `http://114.5.1.4:1145/github`）。

4. 将 **Content type** 设为 `application/json`。

5. 在 **Which events would you like to trigger this webhook?** 中，选择 **Just the push event**，根据具体情况决定开不开启https

6. 点击 **Add webhook** 完成配置。

### 3. 测试 Webhook

成功配置后，你可以尝试推送代码到 GitHub 仓库，或者在 Webhook 设置页面点击 **Recent Deliveries** 旁边的 **Redeliver** 按钮，来测试 Webhook 是否正常工作。

如果配置成功，您会在 Telegram 中收到类似以下格式的消息：

```
🔨 在仓库 xxx/xxx 中有一个新的提交❕
📖 xxx by xxx
❕提交信息: 我喜欢你
⌚️提交时间: xxx
```


