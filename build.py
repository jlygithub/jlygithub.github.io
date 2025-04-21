import subprocess
from pathlib import Path
import shutil

Path('_config.butterfly.yml').rename('config2.yml')
Path('_config.butterfly-jp.yml').rename('_config.butterfly.yml')

print('生成日文内容')

subprocess.run(['hexo', 'clean'], shell=True, check=True)
subprocess.run(['hexo', 'g', '--config', '_config-jp.yml'], shell=True, check=True)

print('恢复原始配置并生成默认内容')
Path('_config.butterfly.yml').rename('_config.butterfly-jp.yml')
Path('config2.yml').rename('_config.butterfly.yml')

subprocess.run(['hexo', 'clean'], shell=True, check=True)
subprocess.run(['hexo', 'g'], shell=True, check=True)

print('移动日文生成内容到子目录')
shutil.move('public-jp', 'public/jp')
shutil.move('public/jp/style-jp.css', 'public')

print('运行gulp任务')
subprocess.run('gulp', shell=True, check=True)

# Python替换字符串，防止跳回主页时打开新界面
print('修改中日文切换跳转URL')
local_host = 'http://localhost:4000/'
remote_host = local_host                                # local test
# remote_host = 'https://jlygithub.github.io/'            # githubio
remote_host_jp = 'http://www.meiwas.com'                # meiwas

with open("public/jp/index.html", "r", encoding="utf-8") as f:
    content = f.read()
    content = content.replace(
        f'class="site-page child" target="_blank" rel="noopener" href="{local_host}',
        f'class="site-page child" target="_self" rel="noopener" href="{remote_host}',
    )

with open("public/jp/index.html", "w", encoding="utf-8") as f:
    f.write(content)
