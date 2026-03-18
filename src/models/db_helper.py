from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBHelper:
    def __init__(self, db_url):
        self.database_url = db_url
        self.engine = create_engine(self.database_url)

    def create_session(self):
        return sessionmaker(autocomit=False,autoflush=False, bind=self.engine)
