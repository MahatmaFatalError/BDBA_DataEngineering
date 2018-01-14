from kafka import KafkaConsumer, KafkaProducer


class BDBAConsumer:

    def __init__(self, topic):
        self.consumer = KafkaConsumer(topic, bootstrap_servers='localhost:9092')


class BDBAProducer:
        def __init__(self):
            self.producer = KafkaProducer()

        def send_service_request(self, content):
            topic = 'Service Requests'
            self.producer.send(topic, content)