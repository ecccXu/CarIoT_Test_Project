import requests
import pytest


class TestPostAPI:
    base_url = "https://jsonplaceholder.typicode.com/posts"

    def test_get_all_posts(self):
        """测试获取所有文章"""
        response = requests.get(self.base_url)

        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 5.0

        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
        print(f"✓ 获取到{len(data)}篇文章")

    def test_get_single_post(self):
        """测试获取单篇文章"""
        url = f"{self.base_url}/1"
        response = requests.get(url)

        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 5.0

        data = response.json()
        assert data["id"] == 1
        assert "title" in data
        assert "body" in data
        print(f"✓ 获取文章: {data['title']}")

    def test_create_post(self):
        """测试创建文章"""
        data = {
            "title": "Python测试文章",
            "body": "这是Python创建的测试内容",
            "userId": 1
        }
        response = requests.post(self.base_url, json=data)

        assert response.status_code == 201

        result = response.json()
        assert result["title"] == data["title"]
        assert result["body"] == data["body"]
        assert "id" in result
        print(f"✓ 创建文章成功，ID: {result['id']}")

    def test_update_post(self):
        """测试更新文章"""
        url = f"{self.base_url}/1"
        data = {
            "id": 1,
            "title": "更新后的标题",
            "body": "更新后的内容",
            "userId": 1
        }
        response = requests.put(url, json=data)

        assert response.status_code == 200

        result = response.json()
        assert result["title"] == data["title"]
        assert result["body"] == data["body"]
        print(f"✓ 更新文章成功: {result['title']}")

    def test_delete_post(self):
        """测试删除文章"""
        url = f"{self.base_url}/1"
        response = requests.delete(url)

        assert response.status_code == 200
        print("✓ 删除文章成功")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])