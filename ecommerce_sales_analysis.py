import pandas as pd
from datetime import date
path = 'D:\T4Teq\My Projects\Sales Report Analysis\messy_ecommerce_sales_2022_2025.csv'.replace('/','//')
df = pd.read_csv(path)

df.columns = df.columns.str.lower().str.replace(' ','_')
print(df.columns)

df.info()

df.describe()

df['price'] = df.groupby('product_category')['price'].transform(lambda x: x.fillna(x.median()))
print(df['price'])
df['customer_rating'] = df.groupby('product_category')['customer_rating'].transform(lambda x: x.fillna(x.median()))
print(df['customer_rating'])

df['price'] = df['price'].abs()
print(df['price'])
df['revenue'] = df['revenue'].abs()
print(df['revenue'])

date = df['purchase_date']
df['purchase_date'] = pd.to_datetime(date, format='mixed').dt.strftime('%d-%m-%Y')
print(df)

df['quantity'] = df['quantity'].replace('two',2)
print(df['quantity'])

str_proper = ['product_name','product_category','region','payment_method']
for col in str_proper:
    df[col] = df[col].astype(str).str.title()

print(df[str_proper])

df.to_csv('D:\T4Teq\My Projects\Sales Report Analysis\output.csv')

from sqlalchemy import create_engine
username = 'root'
password = 'root'
host = 'localhost'
port = '3306'
database = 'ecommerce_sales'

engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

table_name = 'sales'
df.to_sql(table_name, engine, if_exists='replace', index=False)

pd.read_sql('select * from sales limit 5;', engine)

null = df.isnull().sum()
print(null)
