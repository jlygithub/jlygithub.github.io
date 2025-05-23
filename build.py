import subprocess
from pathlib import Path
import shutil
import os

print('生成日文内容')
Path('_config.butterfly.yml').rename('config2.yml')
Path('_config.butterfly-jp.yml').rename('_config.butterfly.yml')
subprocess.run(['hexo', 'clean'], shell=True, check=True)
subprocess.run(['hexo', 'g', '--config', '_config-jp.yml'], shell=True, check=True)

print('生成英文内容')
Path('_config.butterfly.yml').rename('_config.butterfly-jp.yml')
Path('_config.butterfly-en.yml').rename('_config.butterfly.yml')
subprocess.run(['hexo', 'clean'], shell=True, check=True)
subprocess.run(['hexo', 'g', '--config', '_config-en.yml'], shell=True, check=True)

print('恢复原始配置并生成默认内容')
Path('_config.butterfly.yml').rename('_config.butterfly-en.yml')
Path('config2.yml').rename('_config.butterfly.yml')
subprocess.run(['hexo', 'clean'], shell=True, check=True)
subprocess.run(['hexo', 'g'], shell=True, check=True)

print('移动日文生成内容到子目录')
shutil.move('public-jp', 'public/jp')
shutil.move('public/jp/style-jp.css', 'public')

print('移动英文生成内容到子目录')
shutil.move('public-en', 'public/en')
shutil.move('public/en/style-en.css', 'public')

print('运行gulp任务')
subprocess.run('gulp', shell=True, check=True)

# Python替换字符串，防止跳回主页时打开新界面
print('修改切换跳转URL')
local_host = 'http://localhost:4000/'
remote_host = local_host                                # local test
# remote_host = 'https://jlygithub.github.io/'            # githubio
# remote_host = 'http://www.meiwas.com/'                # meiwas

def find_index_files(root_dir):
    index_paths = []
    # 遍历目录树
    for root, dirs, files in os.walk(root_dir):
        # 跳过 node_modules 等常见不需要遍历的目录（可选）
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
        
        # 查找 index.html 文件
        if 'index.html' in files:
            full_path = os.path.join(root, 'index.html')
            index_paths.append(full_path)
    
    return index_paths

def replace_index(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        content = content.replace(
            f'class="site-page child" target="_blank" rel="noopener" href="{local_host}',
            f'class="site-page child" target="_self" rel="noopener" href="{remote_host}',
        )

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

search_root = "public"
    
# 获取结果
results = find_index_files(search_root)

# 打印找到的文件路径
for path in results:
    replace_index(path)


# # 替换日文跳转URL方式
# with open("public/jp/index.html", "r", encoding="utf-8") as f:
#     content = f.read()
#     content = content.replace(
#         f'class="site-page child" target="_blank" rel="noopener" href="{local_host}',
#         f'class="site-page child" target="_self" rel="noopener" href="{remote_host}',
#     )

# with open("public/jp/index.html", "w", encoding="utf-8") as f:
#     f.write(content)

# # 替换英文跳转URL方式
# with open("public/en/index.html", "r", encoding="utf-8") as f:
#     content = f.read()
#     content = content.replace(
#         f'class="site-page child" target="_blank" rel="noopener" href="{local_host}',
#         f'class="site-page child" target="_self" rel="noopener" href="{remote_host}',
#     )

# with open("public/en/index.html", "w", encoding="utf-8") as f:
#     f.write(content)