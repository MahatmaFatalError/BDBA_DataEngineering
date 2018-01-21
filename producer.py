from KafkaHelper import BDBAProducer
from SodaHelper import SodaConnector
import random
import time
import json

soda = SodaConnector("data.cityofnewyork.us")
requests = soda.get_data("fhrw-4uyv", limit=1000)
producer = BDBAProducer()
topic = 'ServiceRequests'

for request in requests:
    json_string = json.dumps(request)
    json_byte = b"" + json_string
    producer.send_service_request(topic, json_byte)
    time.sleep(random.randint(0, 100) * 0.1)