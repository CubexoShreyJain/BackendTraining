from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

url = URL.create(
    drivername= 'postgresql',
    username = 'cubexo',
    password = 'shrey123',
    database= 'cubexo',
    host = "127.0.0.1",
    port = "5432"
)
engine = create_engine(url)
conn = engine.connect()

Base  = declarative_base()

# table 1
class Article(Base):
    __tablename__ = 'articles'
    
    id = Column(Integer(), primary_key=True) 
    slug = Column(String(100), nullable=False, unique = True) 
    title = Column(String(100), nullable=False) 
    created_on = Column(DateTime(), default= datetime.now)
    # author_id = Column(Integer(), ForeignKey('authors.id')) 

# table2
class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer(), primary_key=True) 
    firstname = Column(String(100)) 
    lastname = Column(String(100)) 
    email = Column(String(255), nullable=False) 
    joined_on = Column(DateTime(), default= datetime.now)
    
    # articles = relationship('Article', backref='author')
    
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

shrey = Author(
    firstname="Shrey",
    lastname="Jain",
    email="shrey.jain@gmail.com"
)

ish = Author(
    firstname="Ish",
    lastname="Abrol",
    email="ish.abrol@cubexo.io"
)

# session.add(shrey)
# session.add(ish)
session.add_all([shrey, ish])
session.commit()

articles = session.query(Author).all()
for x in articles:
    print(x.firstname)
    
    
    