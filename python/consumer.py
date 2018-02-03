from kafka import KafkaConsumer
from DBHelper import DBHelper
import json

db_helper = DBHelper('bdba')
db_table = 'service_request'
db_columns = db_helper.get_table_column_names(db_table)

requests = KafkaConsumer("ServiceRequests", bootstrap_servers='localhost:9092') # auto_offset_reset='earliest'

for message in requests:
    db_entry = {}
    message_json = json.loads(message.value)
    for column in db_columns:
        if column in message_json:  # check if key is available in request object
            db_entry[column] = message_json[column]

    db_helper.insert(db_entry, db_table)
