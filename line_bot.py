import requests
import sys
sys.path.append('../API')  # 親ディレクトリのパスを追加
from get_fortune import get_fortune
import line_notify_api


# 取得したTokenを代入
line_notify_token = line_notify_api.line_notify_token

# 占いのメッセージを中日新聞のページから取得
message = "\n"+get_fortune()

# Line Notifyを使った、送信部分
line_notify_api = 'https://notify-api.line.me/api/notify'
headers = {'Authorization': f'Bearer {line_notify_token}'}
data = {'message': f'{message}'}
requests.post(line_notify_api, headers=headers, data=data)
