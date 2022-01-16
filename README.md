# 电商实时监控系统

## 项目介绍
- 项目描述：
该项目主要为电商相关公司开发的销售数据实时监控系统，主要实现了销售量、销售额和库存关于地区和商品类目的实时数据监控，各模块支持图片导出。该系统采用了python的Flask框架，Mysql数据库，前端html页面负责显示，使用了JavaScript中的echarts可视化库。
- 软件环境：python、MySQL、HTML、JavaScript
- 开发工具：pycharm

## 系统页面展示图
展示视频请点击 [此处](https://github.com/K-m9/real-time_monitoring_System.io/blob/main/video_%E9%A1%B9%E7%9B%AE%E5%B1%95%E7%A4%BA.mp4)下载观看
<img src = "https://github.com/K-m9/real-time_monitoring_System.io/blob/main/%E9%A1%B5%E9%9D%A2%E5%B1%95%E7%A4%BA.png">

<iframe src="//player.bilibili.com/player.html?aid=508127641&bvid=BV1zu411272Y&cid=485822246&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>

## 代码使用方法
- 下载整个代码包
- 使用记事本打开 create_table.py，将connection更改成本地的数据库路径；同理打开system.py，将connection更改成本地的数据库路径
- 打开cmd
- 打开代码存放路径: cd xx
- 运行creat_table.py文件: python creat_table.py
- 运行system.py文件: python system.py
- 在浏览器中打开 http://127.0.0.1:5000/ 即可看到系统页面
