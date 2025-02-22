from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings
import dotenv
from redis import Redis


dotenv.load_dotenv()

class Settings(BaseSettings):
    DATABASE_HOST: str
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_PORT: int
    REDIS_URL: str
    TOKEN_SECRET: str
    TOKEN_ALGORITHM: str
    TOKEN_EXPIRATION: int


redis = Redis.from_url(url=Settings().REDIS_URL, db=0, decode_responses=True)

setting = Settings()


db_url = f"mysql+mysqldb://{setting.DATABASE_USERNAME}:{setting.DATABASE_PASSWORD}@{setting.DATABASE_HOST}:{setting.DATABASE_PORT}/{setting.DATABASE_NAME}"
engine =  create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()