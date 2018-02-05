from kafka import KafkaConsumer
from DBHelper import DBHelper
import json
import threading
import config


class Consumer(threading.Thread):

    def __init__(self):
        super(Consumer, self).__init__()
        self.db_table = config.TABLE_NAME
        self.db_helper = DBHelper(config.DATABASE_NAME)
        self.db_columns = self.db_helper.get_table_column_names(self.db_table)

    def run(self):
        requests = KafkaConsumer(config.KAFKA_TOPIC,
                                 bootstrap_servers=config.KAFKA_SERVER)  # auto_offset_reset='earliest'

        for message in requests:
            db_entry = {}
            message_json = json.loads(message.value)
            for column in self.db_columns:
                if column in message_json:  # check if key is available in request object
                    db_entry[column] = message_json[column]
            print("Saving in DB...")
            self.db_helper.insert(db_entry, self.db_table)
