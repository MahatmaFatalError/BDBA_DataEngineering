from kafka import KafkaProducer
from SodaHelper import SodaConnector
import threading
import random
import time
import json


class Producer(threading.Thread):

    def __init__(self, from_date, to_date):
        super(Producer, self).__init__()
        self.soda = SodaConnector("data.cityofnewyork.us")
        self.topic = 'ServiceRequests'
        self.producer = KafkaProducer()
        self.limit = 10000
        self.from_date = from_date
        self.to_date = to_date

    def fetch_data(self, from_date, to_date, limit):
        requests = self.soda.get_data(dataset_identifier="fhrw-4uyv",
                                      from_date=from_date,
                                      to_date=to_date,
                                      limit=limit)
        length = len(requests)
        if length > 0:
            date = requests[-1]["created_date"]
        else:
            date = self.to_date
        for request in requests:
            json_string = json.dumps(request)
            json_byte = b"" + json_string
            print("Sending to Kafka...")
            self.producer.send(self.topic, json_byte)
            # time.sleep(random.randint(0, 50) * 0.1)

        return len(requests), date

    def run(self):
        number_of_entries, to_date = self.fetch_data(from_date=self.from_date,
                                                     to_date=self.to_date,
                                                     limit=self.limit)
        while number_of_entries == self.limit and to_date != self.from_date:
            print("Next Request...")
            number_of_entries, to_date = self.fetch_data(from_date=self.from_date,
                                                         to_date=to_date,
                                                         limit=self.limit)
        print("The End.")
