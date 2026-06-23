# GitHub Trending Projects 🚀

这是一个自动抓取 GitHub 上最火项目的网页应用，每天凌晨 1:00 会更新一次，并部署到 [GitHub Pages](https://your-username.github.io/github-trending-projects/)

## ✅ 功能

- 自动抓取 GitHub 上 Star 数超过 10,000 的热门项目
- 每天自动更新一次
- 部署为静态 HTML 网页（兼容 GitHub Pages）

## 📦 技术栈

- Python
- GitHub Actions + GitHub Pages
- Jinja2 模板引擎
- requests 抓取 GitHub API 数据

## 📦 部署流程

1. 创建 GitHub 仓库 `github-trending-projects`
2. 将本项目代码提交到该仓库
3. 设置 `GITHUB_API_TOKEN` Secrets（推荐 GitHub Personal Access Token）
4. 等待每天凌晨 1 点的调度任务自动更新并部署

## 🌐 访问页面

访问：https://your-username.github.io/github-trending-projects/

## 🧪 测试方法

- 首次部署，可以点击 "Run workflow"
- 每天凌晨会自动更新

---