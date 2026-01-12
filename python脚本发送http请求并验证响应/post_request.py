import requests
import json

# 准备请求数据
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "我的测试文章",
    "body": "这是测试内容",
    "userId": 1
}

# 发送POST请求
response = requests.post(url, json=data)

# 打印响应信息
print(f"状态码: {response.status_code}")
print(f"响应体: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")