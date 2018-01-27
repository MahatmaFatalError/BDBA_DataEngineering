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
requests = soda.get_data("fhrw-4uyv", from_date=from_date, to_date=to_date)
topic = 'ServiceRequests'

producer = BDBAProducer()

for request in requests:
    json_string = json.dumps(request)
    json_byte = b"" + json_string
    producer.send_service_request(topic, json_byte)
    time.sleep(random.randint(0, 100) * 0.1)