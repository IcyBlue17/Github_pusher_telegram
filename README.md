# Github_pusher_telegram
一个简单的基于Python的Telegram机器人，配合Github Webhook实现仓库Commit消息的推送    
# Docker部署  

docker run -d \
  --name github-pusher \
  -e TOKEN=你的token \
  -e CHATID=你的chat_id \
  -p 宿主机映射端口:1145 \  
  icymichiko/github_pusher_telegram:latest
