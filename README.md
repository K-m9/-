# 电商实时监控系统

## 项目介绍
- 项目描述：
该项目使用了虚拟的电商数据，主要实现了销售量、销售额和库存关于地区和商品类目的实时动态数据监控，各模块支持图片导出。该系统采用了python的Flask框架，Mysql数据库，前端html页面负责显示，使用了JavaScript中的echarts可视化库。
- 软件环境：python、MySQL、HTML、JavaScript
- 开发工具：pycharm

## 系统页面展示图
<b>展示视频请点击 [此处](https://www.bilibili.com/video/BV1zu411272Y/)观看</b>

<img src = "https://github.com/K-m9/real-time_monitoring_System.io/blob/main/%E9%A1%B5%E9%9D%A2%E5%B1%95%E7%A4%BA.png">

## 代码使用方法
- 下载整个代码包
- 使用记事本打开 create_table.py，将connection更改成本地的数据库路径；同理打开system.py，将connection更改成本地的数据库路径
- 打开cmd
- 打开代码存放路径: cd xx
- 运行creat_table.py文件: python creat_table.py
- 运行system.py文件: python system.py
- 在浏览器中打开 http://127.0.0.1:5000/ 即可看到系统页面
