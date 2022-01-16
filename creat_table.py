import pandas as pd
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Date, Integer, String, ForeignKey

# 数据库创建
connection = create_engine("mysql+pymysql://root:@localhost:3306/电商系统?charset=utf8", echo=True)
## 绑定引擎
metadata = MetaData(connection)
## 定义表格
district_table = Table('district', metadata,
        Column('Month', String(20)),
        Column('Guangzhou', Integer),
        Column('Chengdu', Integer),
        Column('Beijing', Integer),
        Column('Shanghai', Integer)
        )

address_table = Table('commodity', metadata,
        Column('ItemCat', String(50)),
        Column('shopname', String(50)),
        Column('district', String(30)),
        Column('price', Integer, nullable=False),
        Column('sold', Integer, nullable=False),
        Column('remain', Integer, nullable=False)
        )

metadata.create_all()


# 数据导入
district = pd.read_excel('district.xlsx', index_col= None)
commodity = pd.read_excel('commodity.xlsx')
district.to_sql('district', con=connection, if_exists = 'append', index = False)
commodity.to_sql('commodity', con=connection, if_exists = 'append', index = False)