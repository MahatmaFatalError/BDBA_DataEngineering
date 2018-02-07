package com.srh.bdba.dataengineering;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

/**
 * common constants
 * @author jruppel
 *
 */
public interface KafkaCommons {
	final static String TOPIC = "ServiceRequests";
	final static String BOOTSTRAP_SERVERS = "localhost:9092,localhost:9093,localhost:9094";

	static Properties loadProperties() throws IOException{
		Properties prop = new Properties();

		try (InputStream input = KafkaCommons.class.getResourceAsStream("/kafka_config.properties")) {
			prop.load(input);
			return prop;
		}

	}
}
