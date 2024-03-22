DATABASES = {
    'default': {
        'HOST': 'localhost',
        'NAME': 'mydb',
        'USER': 'root',
        'PASSWORD': 'root',
        'PORT': '3306'
    }
}
user = DATABASES['default']['USER']
password = DATABASES['default']['PASSWORD']
host = DATABASES['default']['HOST']
name = DATABASES['default']['NAME']

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
import sqlalchemy as db 

db_url=f'mysql+pymysql://{user}:{password}@{host}/{name}'

engine = create_engine(url = db_url, echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)
DB_SESSION = Session()