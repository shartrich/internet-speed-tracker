CREATE_TABLE_STATEMENT = '''
    CREATE TABLE IF NOT EXISTS `speed_results` (
        record_datetime DATETIME NOT NULL,
        unit VARCHAR(4) NOT NULL,
        download DOUBLE,
        upload DOUBLE,
        ping DOUBLE
    )
'''

INSERT_STATEMENT_TEMPLATE = '''
    INSERT INTO `speed_results` (
        record_datetime,
        unit,
        download,
        upload,
        ping
    ) VALUES (
        '{record_datetime}',
        '{unit}',
        {download},
        {upload},
        {ping}
    )
'''