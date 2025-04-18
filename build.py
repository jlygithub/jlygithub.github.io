import os

os.system("build.bat")

host = 'http://localhost:4000/'

with open("public/jp/index.html", "r", encoding="utf-8") as f:
    content = f.read()
    content = content.replace(
        f'class="site-page child" target="_blank" rel="noopener" href="{host}',
        f'class="site-page child" target="_self" rel="noopener" href="{host}',
    )

with open("public/jp/index.html", "w", encoding="utf-8") as f:
    f.write(content)
