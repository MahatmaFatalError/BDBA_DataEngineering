package com.srh.bdba.dataengineering;

import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.util.Properties;
import java.util.Random;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVRecord;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.clients.producer.RecordMetadata;
import org.apache.kafka.common.serialization.LongSerializer;
import org.apache.kafka.common.serialization.StringSerializer;

import com.fasterxml.jackson.databind.ObjectMapper;

/**
 * Reads a given CSV file line wise and writes the records as json to a Kafka Topic
 * @author jruppel
 *
 */
public class MyProducer implements Runnable {

	private final ObjectMapper objectMapper = new ObjectMapper();
	
	private final String filepath;
	
	public MyProducer(String filepath) {
		this.filepath = filepath;
	}

	public static void main(String[] args) throws Exception {

		Reader in = new FileReader("/data/311_Service_Requests_from_2010_to_Present.csv");
		Iterable<CSVRecord> records = CSVFormat.RFC4180.withFirstRecordAsHeader().parse(in);
		
		new MyProducer("").runProducer(records);

	}

	public void runProducer(final Iterable<CSVRecord> records) throws Exception {

		try (final Producer<Long, String> producer = createProducer()) {

			for (final CSVRecord csvRecord : records) {
				String json = objectMapper.writeValueAsString(csvRecord.toMap());
				final ProducerRecord<Long, String> record = new ProducerRecord<>(KafkaCommons.loadProperties().getProperty("KAFKA_TOPIC", KafkaCommons.TOPIC), Long.parseLong(csvRecord.get("Unique Key")), json);
				Thread.sleep(new Random().nextInt(2000));
				RecordMetadata metadata = producer.send(record).get();
				System.out.printf("sent record(key=%s value=%s) " + "meta(partition=%d, offset=%d)\n", record.key(), record.value(), metadata.partition(), metadata.offset());

			}

		}
	}

	private Producer<Long, String> createProducer() throws IOException{
		Properties props = new Properties();
		props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, KafkaCommons.loadProperties().getProperty("KAFKA_BOOTSTRAP_SERVERS", KafkaCommons.BOOTSTRAP_SERVERS));
		props.put(ProducerConfig.CLIENT_ID_CONFIG, "KafkaCSVProducer");
		props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, LongSerializer.class.getName());
		props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
		return new KafkaProducer<>(props);
	}

	@Override
	public void run() {
		try {
			Reader in = new FileReader(filepath);
			Iterable<CSVRecord> records = CSVFormat.RFC4180.withFirstRecordAsHeader().parse(in);		
			
			runProducer(records);
			
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			
		}
		
	}

}
