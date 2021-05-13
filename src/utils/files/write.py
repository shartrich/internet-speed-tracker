import csv
from src.configs.settings import OUTPUT_CSV

def write_row(result, output_path=OUTPUT_CSV):
    data_row = [result['record_datetime'], result['unit'], result['download'], result['upload'], result['ping']]

    with open(output_path, 'a') as data_csv:
        csv_writer = csv.writer(data_csv)
        csv_writer.writerow(data_row)