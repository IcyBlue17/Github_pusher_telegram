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
