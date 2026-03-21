from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager

from src.execptions.repository_exceptions import DatabaseConnectionError


class DBHelper:
    def __init__(self, db_url):
        self.database_url = db_url
        self.engine = create_engine(self.database_url)

    # create a managed session, Thread-safety
    # for more information, check the difference between scoped_session vs session maker
    def create_session(self):
        return scoped_session(sessionmaker(autocommit=False,autoflush=False, bind=self.engine))

    @contextmanager
    def session(self) -> Generator[scoped_session, None, None]:
        """
        Context manager that provides transaction management for nested blocks.
        A transaction is started when the block is entered and then either
        committed if the block exists without incident, or rolled back if an error is raised
        :return: Scoped Session
        """
        session = self.create_session()
        if session is None:
            raise DatabaseConnectionError("Couldn't connect to database to create session!")
        try:
            yield session
            session.commit()
        except Exception as error:
            session.rollback()
            raise error
        finally:
            session.close()
