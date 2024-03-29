from abc import abstractmethod
import time
import requests
from core.interact import Interact
from scheduler.thread_manager import MyThread
from utils import config_util , util
import threading

interact_datas = []
class YoutubeViewer:
    def __init__(self):
        self.running = True
        self.live_started = False
        self.live_chat_id = None  # 存储liveChatId
        self.processed_message_ids = set()  # 存储已处理消息的ID

    def get_live_chat_id(self):
        global running
        url = f"https://www.googleapis.com/youtube/v3/videos"
        params = {
            "part": "liveStreamingDetails",
            "id": config_util.config['source']['youTube']['id'],
            "key": config_util.key_youtube_developer_key
        }
        response = requests.get(url, params=params).json()
        try:
            live_chat_id = response['items'][0]['liveStreamingDetails']['activeLiveChatId']
            return live_chat_id
        except KeyError:
            util.log(1, '無法獲取activeLiveChatId響應...')
            running = False
            return None

    def get_live_chat_messages(self):
        global interact_datas
        """获取YouTube直播间聊天消息"""
        if self.live_chat_id is None:
            self.live_chat_id = self.get_live_chat_id()  # 获取liveChatId
        """获取YouTube直播间聊天消息"""
        url = f'https://www.googleapis.com/youtube/v3/liveChat/messages'
        params = {
            'liveChatId': self.live_chat_id,
            'part': 'id,snippet,authorDetails',
            'maxResults': 5,  # 请求最多5条消息
            'key': config_util.key_youtube_developer_key
        }


        response = requests.get(url, params=params).json()

        for item in response.get('items', []):
            message_id = item['id']
            if message_id not in self.processed_message_ids:
                if 'displayMessage' in item['snippet']:
                    message = item['snippet']['displayMessage']
                    user = item['authorDetails']['displayName']
                    interact_datas.append(Interact("live", 1, {"user": user, "msg": message}))
                    # 将新消息ID添加到已处理集合
                    self.processed_message_ids.add(message_id)

    def start(self):
        """启动直播间监控"""
        threading.Thread(target=self.monitor_live_chat).start()

    def monitor_live_chat(self):
        global interact_datas
        """监控YouTube直播间聊天"""
        while self.running:
            self.get_live_chat_messages()
            # 將收到的數據交給on_interact處理
            for interact in interact_datas:
                print(interact)
                MyThread(target=self.on_interact, args=[interact, time.time()]).start()
            interact_datas.clear()
            time.sleep(10)  # 根据需要调整请求间隔

    def stop(self):
        global running
        """停止直播间监控"""
        running = False

    @abstractmethod
    def on_interact(self, interact, event_time):
        pass