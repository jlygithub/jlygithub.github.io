REM mv _config.butterfly.yml config2.yml && mv config-butterfly-en.yml _config.butterfly.yml && hexo clean && hexo g --config="config-en.yml" && mv -f config2.yml _config.butterfly.yml && hexo clean && hexo g && mv --force public-en/ public/en/ && gulp
@echo off
REM 备份原始配置文件并切换为日文配置
ren _config.butterfly.yml config2.yml
ren _config.butterfly-jp.yml _config.butterfly.yml

REM 生成日文内容
hexo clean
hexo g --config="_config-jp.yml"

REM 恢复原始配置并生成默认内容
move /Y config2.yml _config.butterfly.yml
hexo clean
hexo g

REM 移动日文生成内容到子目录
if exist public\jp rmdir /s /q public\jp
move /Y public-jp public\jp

REM 运行Gulp任务
gulp