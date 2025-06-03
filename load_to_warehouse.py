import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("weather.csv/part-00000-363828f5-8a96-40c7-8a54-0032cd8b15da-c000.csv")

engine = create_engine("postgresql+psycopg2://pswd@pg-328dcccd-petergatitu61-111d.i.aivencloud.com:14741/gatitu")
df.to_sql("weather_data", engine, if_exists="replace", index=False, schema='weather')
