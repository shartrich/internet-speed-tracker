from sqlalchemy import create_engine
from pymysql import connect, cursors
from src.configs.settings import DB_USERNAME, DB_PASSWORD, DB_DATABASE, DB_HOST, DB_PORT

# Create an SQL engine we can provide to pandas for direct dataframe actions
def create_sql_engine(database=DB_DATABASE):
    engine_string = "mysql+pymysql://{user}:{password}@{host}:{port}/{db}".format(
            host=DB_HOST,
            user=DB_USERNAME,
            password=DB_PASSWORD,
            port=DB_PORT,
            db=database
        )
    return create_engine(
        engine_string,
        encoding='latin1', 
    )

# create a connection we can use for quick queries
def create_connection(database=DB_DATABASE):
    connection = connect(
        host=DB_HOST,
        user=DB_USERNAME,
        password=DB_PASSWORD,
        db=database,
        port=int(DB_PORT),
        cursorclass=cursors.DictCursor
    )
    return connection