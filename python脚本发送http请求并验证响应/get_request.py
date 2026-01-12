import requests

# 发送GET请求
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

# 打印响应信息
print(f"状态码: {response.status_code}")
print(f"响应时间: {response.elapsed.total_seconds()}秒")
print(f"响应头: {response.headers}")
print(f"响应体: {response.json()}")