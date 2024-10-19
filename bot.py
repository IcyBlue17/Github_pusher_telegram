from flask import *
from datetime import *
import requests
import os
app = Flask(__name__)

bot_token = os.getenv('TOKEN') 
chat_id = os.getenv('CHATID') 
api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

@app.route("/", methods=["GET", "POST"])
def root():
    return jsonify({"status": "error"}), 400

@app.route("/github", methods=["POST"])
def webhooker():
    if request.method == "POST":
        payload = request.json
        if 'commits' in payload and 'repository' in payload:
            repo_name = payload['repository']['name']
            repo_owner = payload['repository']['owner']['login']
            for commit in payload['commits']:
                commit_hash = commit['id'][:7]
                author = commit['author']['name']
                message = commit['message']
                commit_time = datetime.strptime(commit['timestamp'], '%Y-%m-%dT%H:%M:%S%z').strftime('%Y-%m-%d %H:%M:%S')

                msg = (
                    f"🔨 在仓库 {repo_owner}/{repo_name} 中有一个新的提交❕\n\n"
                    f"📖 {commit_hash} by {author}\n\n"
                    f"❕提交信息: {message}\n"
                    f"⌚️提交时间: {commit_time}"
                )

                payload = {
                    'chat_id': chat_id,
                    'text': msg
                }
                response = requests.post(api_url, json=payload)

                if response.status_code != 200:
                    print(f"Failed to send message: {response.text}")

        return jsonify({"status": "success"}), 200

    return jsonify({"status": "error"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1145)
