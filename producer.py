from kafka import KafkaProducer

producer = KafkaProducer()
for index in range(100):
    producer.send('tests', b'My {0} ever Message after i realized it has worked'.format(str(index)))