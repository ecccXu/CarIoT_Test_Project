import requests
import pytest

# 测试数据
test_data = [
    (1, "sunt aut facere"),
    (2, "qui est esse"),
    (3, "ea molestias quasi")
]


class TestDataDriven:
    base_url = "https://jsonplaceholder.typicode.com/posts"

    @pytest.mark.parametrize("post_id, expected_title", test_data)
    def test_get_posts(self, post_id, expected_title):
        """数据驱动测试：验证多篇文章"""
        url = f"{self.base_url}/{post_id}"
        response = requests.get(url)

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == post_id
        assert expected_title in data["title"]
        print(f"✓ 文章{post_id}: {data['title']}")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])