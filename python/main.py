from Consumer import Consumer
from Producer import Producer
from SignalHandler import SignalHandler
import threading
import datetime
import locale
import signal


def main():
    # handle user input
    from_date_string = str(raw_input("Please specify a Start Date with format ddmmYYYY: "))
    # raw input in python2 is the same as input in python3 (returns a string instead of a python expression)
    to_date_string = str(raw_input("Please specify a End Date with format ddmmYYYY: "))
    locale.setlocale(locale.LC_ALL, '')
    from_date = datetime.datetime.strptime(from_date_string, '%d%m%Y').isoformat()
    to_date = datetime.datetime.strptime(to_date_string, '%d%m%Y')
    tmp_date = to_date + datetime.timedelta(1)
    to_date = tmp_date.isoformat()

    threads = list()
    stopper = threading.Event()

    consumer = Consumer()
    producer = Producer(from_date=from_date, to_date=to_date)

    threads.append(consumer)
    threads.append(producer)

    handler = SignalHandler(stopper, threads)
    signal.signal(signal.SIGINT, handler)

    consumer.start()
    producer.start()


if __name__ == '__main__':
    print("End this Skript with Ctrl + C")
    main()
