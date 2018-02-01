from KafkaHelper import BDBAProducer
from SodaHelper import SodaConnector
import random
import time
import json
import datetime
import locale

from_date_string = str(raw_input("Please specify a Start Date with format ddmmYYYY: "))
# raw input in python2 is the same as input in python3 (returns a string instead of a python expression)
to_date_string = str(raw_input("Please specify a End Date with format ddmmYYYY: "))
locale.setlocale(locale.LC_ALL, '')
from_date = datetime.datetime.strptime(from_date_string, '%d%m%Y').isoformat()
to_date = datetime.datetime.strptime(to_date_string, '%d%m%Y')
tmp_date = to_date + datetime.timedelta(1)
to_date = tmp_date.isoformat()
soda = SodaConnector("data.cityofnewyork.us")
topic = 'ServiceRequests'
producer = BDBAProducer()
limit = 10000


def process():
    requests = soda.get_data(dataset_identifier="fhrw-4uyv",  from_date=from_date, to_date=to_date, limit=limit)
    length = len(requests)
    if length > 0:
        date = requests[-1]["created_date"]
    else:
        date = to_date
    for request in requests:
        print("Starting...")
        print(request["created_date"])
        json_string = json.dumps(request)
        json_byte = b"" + json_string
        producer.send_service_request(topic, json_byte)
        # time.sleep(random.randint(0, 50) * 0.1)
        print("Done...")

    return len(requests), date


number_of_entries, to_date = process()

while number_of_entries == limit and to_date != from_date:
    print("Next Request...")
    number_of_entries, to_date = process()
