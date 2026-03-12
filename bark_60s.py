import requests
import os

# ================= 配置区 =================
# 如果在本地测试，直接填入你的 Key；如果用 GitHub Actions，建议使用环境变量
BARK_KEY = os.getenv("BARK_KEY")
# ==========================================

def push_to_bark():
    # 60s 图片直连地址
    img_url = "https://60s.viki.moe/v2/60s?encoding=image"
    
    # 构造 Bark 推送接口
    # 参数说明：自动保存通知、设置分组为“每日简报”、携带图片地址
    api_url = f"https://api.day.app/{BARK_KEY}/每日60秒看世界/点击查看大图"
    
    params = {
        "image": img_url,
        "isArchive": 1,
        "group": "60s新闻"
    }
    
    print("正在推送至 Bark...")
    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        print("推送成功！")
    else:
        print(f"推送失败，错误代码：{response.status_code}")

if __name__ == "__main__":
    push_to_bark()
