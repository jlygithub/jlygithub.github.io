@echo off
echo 备份原始配置文件并切换为日文配置
ren _config.butterfly.yml config2.yml
ren _config.butterfly-jp.yml _config.butterfly.yml

echo 生成日文内容
call hexo clean && call hexo g --config="_config-jp.yml"


echo 恢复原始配置并生成默认内容
move /Y config2.yml _config.butterfly.yml
call hexo clean && call hexo g


echo 移动日文生成内容到子目录
move /Y public-jp public\jp

echo 运行Gulp任务
call gulp