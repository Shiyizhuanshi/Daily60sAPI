import requests
import os
import time

# ================= 配置区 =================
BARK_KEY = os.getenv("BARK_KEY")  # 确保环境变量正确设置，或者硬编码密钥
# ==========================================

def push_to_bark():
    # 60s 图片直连地址，添加时间戳避免缓存
    img_url = f"https://60s.viki.moe/v2/60s?encoding=image&timestamp={int(time.time())}"
    
    # 构造 Bark 推送接口
    api_url = f"https://api.day.app/{BARK_KEY}/每日60秒看世界/点击查看大图"
    
    # 推送参数
    params = {
        "image": img_url,
        "isArchive": 1,
        "group": "60s新闻"
    }

    # 调试：打印请求 URL 和参数
    print(f"请求的 URL: {api_url}")
    print(f"请求的参数: {params}")
    
    # 发送请求
    print("正在推送至 Bark...")
    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        print("推送成功！")
    else:
        print(f"推送失败，错误代码：{response.status_code}")
        print(f"响应内容：{response.text}")  # 打印错误详情

if __name__ == "__main__":
    push_to_bark()
