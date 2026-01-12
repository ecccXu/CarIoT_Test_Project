# 高级测试
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
headers = {
    "User-Agent": "Python-Test-Client",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
# print(f"状态码: {response.status_code}")

# 异常处理
import requests
from requests.exceptions import RequestException

def safe_request(url, method="GET", **kwargs):
    """安全的请求方法，处理异常"""
    try:
        if method == "GET":
            response = requests.get(url, **kwargs)
        elif method == "POST":
            response = requests.post(url, **kwargs)
        elif method == "PUT":
            response = requests.put(url, **kwargs)
        elif method == "DELETE":
            response = requests.delete(url, **kwargs)
        else:
            raise ValueError(f"不支持的HTTP方法: {method}")

        response.raise_for_status()  # 检查HTTP错误
        return response

    except RequestException as e:
        print(f"请求失败: {e}")
        return None


# 使用示例
response = safe_request("https://jsonplaceholder.typicode.com/posts/1")
if response:
    print(f"请求成功: {response.json()}")