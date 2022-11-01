from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///./sql_app.db",
                       echo=True, connect_args={"check_same_thread": False})


Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
