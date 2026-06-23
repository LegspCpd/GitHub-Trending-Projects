import os
from jinja2 import Environment, PackageLoader

# 获取项目数据
repos = fetch_trending_repos()  # 你也可以在这里定义固定数据（用于调试）

# 加载 Jinja2 模板
env = Environment(loader=PackageLoader('github-trending-projects', 'templates'))
template = env.get_template('index.html')
html = template.render(repos=repos)

# 创建 dist 文件夹保存 HTML 文件
os.makedirs("dist", exist_ok=True)
with open("dist/index.html", "w", encoding="utf-8") as f:
    f.write(html)