from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, Session, declarative_base
# from clickhouse_sqlalchemy import get_declarative_base, make_session

engine = create_engine('clickhouse://default:@ch_server:8123/default', echo=True, future=True)
# metadata = MetaData(bind=engine)

Base = declarative_base()


def get_pg_session():
    pg_session = Session(
        sessionmaker(
            autocommit=False,
            bind=engine
        )
    )
    return pg_session
