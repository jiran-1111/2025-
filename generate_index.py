import os

# 仓库根目录
root_dir = "."  # 当前目录，也可以改成你的笔记路径

# 输出 HTML 文件名
output_file = "index.html"

# HTML 头部和样式
html_header = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>我的笔记</title>
<style>
body { font-family: Arial; background-color: #f5f5f5; padding: 20px; }
h1 { text-align: center; }
.container { display: flex; flex-wrap: wrap; gap: 20px; }
.card { background-color: #fff; border: 2px solid #ccc; border-radius: 10px;
        width: 150px; height: 100px; display: flex; align-items: center; 
        justify-content: center; text-align: center;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
        transition: transform 0.2s, box-shadow 0.2s; }
.card:hover { transform: translateY(-5px); box-shadow: 4px 4px 12px rgba(0,0,0,0.3);}
.card a { text-decoration: none; color: #333; font-weight: bold; }
</style>
</head>
<body>
<h1>我的笔记文件夹</h1>
<div class="container">
"""

html_footer = """
</div>
</body>
</html>
"""

# 遍历文件夹和文件
cards = ""
for entry in os.listdir(root_dir):
    if entry == output_file:
        continue  # 不把生成的 HTML 自己加入
    path = os.path.join(root_dir, entry)
    if os.path.isdir(path):
        cards += f'<div class="card"><a href="{entry}/">📁 {entry}</a></div>\n'
    elif os.path.isfile(path):
        cards += f'<div class="card"><a href="{entry}">📄 {entry}</a></div>\n'

# 写入 HTML 文件
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_header + cards + html_footer)

print(f"{output_file} 已生成！")
