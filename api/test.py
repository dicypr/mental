import os

from sqlalchemy import create_engine

DATABASE_URL = os.environ.get("DATABASE_URL") or "postgresql+psycopg2://sanjeev@localhost/mentalapp"

engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    result = connection.execute("SELECT 1")
    print(result.scalar())