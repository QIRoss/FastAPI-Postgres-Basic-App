from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = f"postgresql+psycopg://{os.getenv('DB_USER','postgres')}:{os.getenv('DB_PASSWORD','admin')}@localhost:5432/postgres"
print('aaaa')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
print('bbbb')
