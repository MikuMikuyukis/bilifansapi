import json
import time
import requests
while True:
      res = requests.get("https://api.bilibili.com/x/relation/stat?vmid=13575511")
      #vmid=your bilibili UID
      obj = json.loads(res.text)
      fans = (obj["data"]["follower"])
      print(fans)
      time.sleep(3)
