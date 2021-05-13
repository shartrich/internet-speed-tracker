from src.flows.speed_test import run_test
from src.flows.insert_results import insert_speed_results
from src.utils.files.write import write_row
from src.configs.settings import DEBUG_MODE

if __name__ == '__main__':
    result = run_test()
    if DEBUG_MODE:
        write_row(result)
    else:
        insert_speed_results(result)