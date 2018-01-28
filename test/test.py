from python.DBHelper import DBHelper


db_table = 'service_request'
db_helper = DBHelper('bdba')
db_columns = db_helper.get_table_column_names(db_table)

for column in db_columns:
    print(column)