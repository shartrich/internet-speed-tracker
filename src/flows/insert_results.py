from src.utils.database.query import do_query 
from src.configs.constants import CREATE_TABLE_STATEMENT, INSERT_STATEMENT_TEMPLATE


def insert_speed_results(result):
    do_query(CREATE_TABLE_STATEMENT)
    do_query(INSERT_STATEMENT_TEMPLATE.format(**result))