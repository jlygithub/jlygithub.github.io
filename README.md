# CoCo民宿网站
> 图片来自: [pixabay](https://pixabay.com/)
地址：〒930-0133 富山県富山市呉羽町１７６８－５
Address：930-0133 1768-5, Kurehamachi, Toyama City, Toyama Prefecture

## 导航菜单
1. 主页             /
2. 房间介绍         /room-introduction/
3. 车辆服务         /vehicle-service/
4. 周边设施         /surrounding-facilities/
5. 周边景点         /nearby-attractions/
6. 交通情况         /traffic-status/

## 房间介绍
1. 和式榻榻米8块
2. 和式榻榻米6块
3. 洋式双人床1.5M
4. 洋式双人床1.8M
5. 8畳
6. 榻榻米休息室

## 车辆服务
1. 定制服务
2. 自行车
3. 司导包车
4. 渔船
5. 游览船

## 周边设施
车站    station.jgp
干洗店  washing.jpg
超市    supermarket.jpg
便利店  store.jpg
药妆店  pharmacy.jpg
面包店  bakery.jpg

## 周边景点
立山大雪谷      1.jpg
雨晴海岸        2.jpg
富山最美星巴克  3.jpg
富山玻璃美术馆  4.jpg
富山城天守阁    5.jpg

## 交通情况
- 国内直飞：从日本各地东京大阪名古屋
- 电车、开车

## 多语言支持参考方案
https://github.com/jerryc127/butterfly.js.org/tree/main


运行完脚本build.bat之后，修改下面的html(public/jp/index.html):
```html
<a class="site-page child" target="_blank" rel="noopener" href="http://localhost:4000/"><i class="fa-fw fa-fw fas fa-c"></i> <span>中文</span></a>

<a class="site-page child" target="_self" rel="noopener" href="http://localhost:4000/"><i class="fa-fw fa-fw fas fa-c"></i> <span>中文</span></a>
```
如果是正式版，则将`http://localhost:4000/` 改成 `http://www.meiwas.com`
