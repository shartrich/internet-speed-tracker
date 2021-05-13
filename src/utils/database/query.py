from src.utils.database.connection import create_connection 
from src.configs.settings import DB_DATABASE

# create a connection to the targetted database and return the result
def do_query(query, database=DB_DATABASE):
    conn = create_connection(database)
    cursorObject = conn.cursor()
    cursorObject._defer_warnings = True
    cursorObject.execute(query)
    conn.commit()
    conn.close()
    return cursorObject.fetchall()