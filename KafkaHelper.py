from kafka import KafkaProducer


class BDBAProducer:
        def __init__(self):
            self.producer = KafkaProducer()

        def send_service_request(self, topic, content):
            self.producer.send(topic, content)