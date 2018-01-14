from kafka import KafkaConsumer

requests = KafkaConsumer("ServiceRequests", bootstrap_servers='localhost:9092', auto_offset_reset='earliest')

for message in requests:
    print (message.value)
