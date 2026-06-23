import requests
import os
import json

GITHUB_API_URL = "https://api.github.com/search/repositories"
headers = {
    "Accept": "application/vnd.github.mercy+json"
}

def get_github_api_token():
    token = os.getenv("GH_API_TOKEN")
    if not token:
        print("⚠️ API Token 未设置，将使用默认权限（限制请求次数）")
        return ""
    return f"token {token}"

def fetch_trending_repos():
    params = {
        "q": "stars:>10000",
        "sort": "stars",
        "order": "desc",
        "per_page": 10  # 抓取前 10 个项目
    }
    headers = {
        "Authorization": get_github_api_token(),
        "Accept": "application/vnd.github.mercy+json"
    }
    response = requests.get(GITHUB_API_URL, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        print(f"❌ GitHub API 请求失败。状态码：{response.status_code}")
        print(response.text)
        return []