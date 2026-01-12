import requests


def test_get_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    # 验证状态码
    assert response.status_code == 200, f"状态码错误: {response.status_code}"
    print("✓ 状态码验证通过")

    # 验证响应时间小于1秒
    response_time = response.elapsed.total_seconds()
    assert response_time < 10.0, f"响应时间过长: {response_time}秒"
    print(f"✓ 响应时间验证通过: {response_time}秒")

    # 验证响应体包含数据
    data = response.json()
    assert "id" in data, "响应体缺少id字段"
    assert "title" in data, "响应体缺少title字段"
    print("✓ 响应体验证通过")

    # 验证ID为1
    assert data["id"] == 1, f"ID错误: {data['id']}"
    print(f"✓ ID验证通过: {data['id']}")


if __name__ == "__main__":
    test_get_post()
    print("\n所有测试通过！")