from kafka import KafkaConsumer
from DBHelper import DBHelper
import json
from datetime import datetime


requests = KafkaConsumer("ServiceRequests", bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
db_helper = DBHelper('postgres')

for message in requests:
    message_json = json.loads(message.value)
    print(json.dumps(message_json))

    time = datetime.now()
    print(time)
    if 'agency_name' in message_json:
        agency_name =  message_json['agency_name']
        print(agency_name)
    if 'complaint_type' in message_json:
        type = message_json['complaint_type']
        print(type)
    if 'descriptor' in message_json:
        descriptor = message_json['descriptor']
        print(descriptor)
    if 'longitude' in message_json:
        longitude = message_json['longitude']
        print(longitude)
    if 'latitude' in message_json:
        latitude = message_json['latitude']
        print(latitude)

    entry = {
        'created_date': time,
        'agency_name': agency_name,
        'complaint_type': type,
        'descriptor': descriptor,
        'longitude': longitude,
        'latitude': latitude
    }

    db_helper.insert(entry, 'service_request')
