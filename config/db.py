from sqlalchemy import create_engine, MetaData

engine = create_engine("mariadb+pymysql://root:fastapiPass@localhost:3306/storedb")

meta = MetaData()

conn = engine.connect()