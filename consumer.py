from kafka import KafkaConsumer

consumer = KafkaConsumer('tests', bootstrap_servers='localhost:9092')
for message in consumer:
    print(message)