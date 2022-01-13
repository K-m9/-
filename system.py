# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 11:44:00 2022

@author: 13416
"""


import pandas as pd
from sqlalchemy import create_engine
from flask import Flask, render_template

# 数据导入
connection = create_engine("mysql+pymysql://root:@localhost:3306/电商系统?charset=utf8")
data_sql = "select * from district"
data = pd.read_sql(data_sql, connection)

commodity_sql = "SELECT shopname,SUM(sold) as sale FROM commodity GROUP BY shopname ORDER BY sale DESC"
data_commodity = pd.read_sql(commodity_sql, connection)
income_sql = "SELECT commodity.ItemCat, commodity.district, SUM(sold*price) as income, SUM(remain) as rest, sum(sold + remain) as total FROM commodity GROUP BY commodity.ItemCat, commodity.district"
data_income = pd.read_sql(income_sql, connection)

# 传参 当前文件实例化并给到app对象
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# # 路由：url与函数的映射关系，即index()函数对应 127.0.0.1:5000/index 此url
# # 当匹配到路由为hello的时候，必须是get和post的方法，
# # 表单或者ajax异步请求需要用post
@app.route('/', methods = ['GET','POST'])
def post_data():
    data_json = data.to_dict('list')
    keys = ','.join(data_json.keys())
    commodity_json = data_commodity.to_dict('list')
    # 变成列表
    p = keys.split(',')
    month = data_json['Month']
    GZ = data_json['Guangzhou']
    CD = data_json['Chengdu']
    BJ = data_json['Beijing']
    SH = data_json['Shanghai']
    commodity = commodity_json['sale']
    shopname = commodity_json['shopname']
    district = data_income['district'].drop_duplicates().tolist()
    item = data_income['ItemCat'].drop_duplicates().tolist()
    income_dis = data_income.groupby('district')['income'].sum().tolist()
    rest_item = data_income.groupby('ItemCat')['rest'].sum().tolist()
    total_item = data_income.groupby('ItemCat')['total'].sum().tolist()
    print(rest_item)
    print(total_item)
    income_item = data_income.groupby('ItemCat')['income'].sum()
    return render_template('system.html', column = p[1:-1], month = month, GZ = GZ, CD = CD, BJ = BJ, SH = SH, commodity = commodity, shopname = shopname,
                           district = district, item = item, income_dis = income_dis, income_item = income_item, rest_item = rest_item, total_item = total_item)
# 运行
if __name__ == '__main__':
    app.run()