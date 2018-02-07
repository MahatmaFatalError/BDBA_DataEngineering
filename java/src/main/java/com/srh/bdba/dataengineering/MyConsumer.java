package com.srh.bdba.dataengineering;

import java.io.IOException;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.Types;
import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Properties;
import java.util.stream.Collectors;

import org.apache.commons.lang3.StringUtils;
import org.apache.kafka.clients.consumer.Consumer;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.serialization.LongDeserializer;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.PreparedStatementSetter;
import org.springframework.jdbc.core.metadata.TableMetaDataContext;
import org.springframework.jdbc.datasource.SimpleDriverDataSource;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

/**
 * Reads JSON from a Kafka Topic and stores the data in a postgres database table
 * @author jruppel
 *
 */
public class MyConsumer implements Runnable {

	private final ObjectMapper objectMapper = new ObjectMapper();
	private final String targetTable;
	private final String postgresPW;
	private final String postgresUser;
	private final String postgresUrl;

	public MyConsumer() throws IOException{
		postgresPW = KafkaCommons.loadProperties().getProperty("POSTGRESQL_PW");
		postgresUser = KafkaCommons.loadProperties().getProperty("POSTGRESQL_USER");
		postgresUrl = KafkaCommons.loadProperties().getProperty("POSTGRESQL_URL");
		targetTable = KafkaCommons.loadProperties().getProperty("POSTGRESQL_TARGET_TABLE");
	}

	/**
	 *
	 * @param dbURL
	 * @param tableName
	 * @param dbUser
	 * @param dbPassword
	 */
	public MyConsumer(String dbURL, String tableName, String dbUser, String dbPassword){
		this.postgresUrl = dbURL;
		this.targetTable = tableName;
		this.postgresUser = dbUser;
		this.postgresPW = dbPassword;
	}


	public static void main(String[] args) throws Exception {
		new MyConsumer().runConsumer();
	}

	public void runConsumer() throws Exception {
		SimpleDateFormat formatter = new SimpleDateFormat("MM/dd/yyyy HH:mm:ss a");

		JdbcTemplate template = getJdbcTemplate();
		final List<String> tableColumns = findColumnsOfTable(template, targetTable);

		try (final Consumer<Long, String> consumer = createConsumer()) {
			List<String> topics = Arrays.asList(new String[] { KafkaCommons.loadProperties().getProperty("KAFKA_TOPIC", KafkaCommons.TOPIC)});
			consumer.subscribe(topics);

			while (true) {
				ConsumerRecords<Long, String> records = consumer.poll(100);

				for (ConsumerRecord<Long, String> record : records) {
					System.out.printf("Received Message topic =%s, partition =%s, offset = %d, key = %s, value = %s\n", record.topic(), record.partition(), record.offset(), record.key(), record.value());

					JsonNode jsonNode = objectMapper.readTree(record.value());

					Map<String, Object> result = objectMapper.convertValue(jsonNode, Map.class);
					Map<String, Object> intersectedColumns = new LinkedHashMap<>();

					for (Map.Entry<String, Object> entry : result.entrySet()) {
						if (tableColumns.contains(entry.getKey().toLowerCase().replace(" ", "_"))) {
							intersectedColumns.put(entry.getKey().toLowerCase().replace(" ", "_"), entry.getValue());
						}
					}

					String sql = buildSql(intersectedColumns);

					template.update(sql, new PreparedStatementSetter() {

						@Override
						public void setValues(PreparedStatement ps) throws SQLException {
							try {
								ps.setTimestamp(1, new java.sql.Timestamp(formatter.parse((String) result.get("Created Date")).getTime()));
								ps.setString(2, (String) result.get("Agency Name"));
								ps.setString(3, (String) result.get("Complaint Type"));
								ps.setString(4, (String) result.get("Descriptor"));
								
								if (StringUtils.isBlank((String)result.get("Longitude"))) {
									ps.setNull(5, Types.NULL);
								} else {
									ps.setFloat(5, Float.valueOf((String) result.get("Longitude")));									
								}
								
								if (StringUtils.isBlank((String)result.get("Latitude"))) {
									ps.setNull(6, Types.NULL);
								} else {
								
									ps.setFloat(6, Float.valueOf((String) result.get("Latitude")));
								}
								
								ps.setString(7, (String) result.get("Agency"));
							} catch (Exception e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}
						}
					});

				}

				consumer.commitSync();
			}
		}
	}

	private String buildSql(Map<String, Object> intersect) {
		String columns = String.join(",", intersect.keySet());
		String placeholders = String.join(",", intersect.keySet().stream().map(col -> "?").collect(Collectors.toList()));

		columns = "created_date,agency_name,complaint_type,descriptor,longitude,latitude,agency";
		placeholders = "?,?,?,?,?,?,?";

		String sql = "INSERT INTO " + targetTable + "( " + columns + ") values (" + placeholders + ")";
		return sql;
	}

	private List<String> findColumnsOfTable(JdbcTemplate template, String tabname) {
		TableMetaDataContext tableMetadataContext = new TableMetaDataContext();
		tableMetadataContext.setTableName(tabname);
		tableMetadataContext.processMetaData(template.getDataSource(), Collections.<String>emptyList(), new String[0]);
		return tableMetadataContext.getTableColumns();
	}

	private JdbcTemplate getJdbcTemplate() {
		SimpleDriverDataSource ds = new SimpleDriverDataSource();
		ds.setDriver(new org.postgresql.Driver());
		ds.setUrl("jdbc:postgresql://" + postgresUrl);
		ds.setUsername(postgresUser);
		ds.setPassword(postgresPW);

		return new JdbcTemplate(ds);
	}

	private Consumer<Long, String> createConsumer() throws IOException{
		Properties props = new Properties();
		props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, KafkaCommons.loadProperties().getProperty("KAFKA_BOOTSTRAP_SERVERS", KafkaCommons.BOOTSTRAP_SERVERS));
		props.put(ConsumerConfig.CLIENT_ID_CONFIG, "KafkaCSVProducer");
		props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, LongDeserializer.class.getName());
		props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
		props.put(ConsumerConfig.GROUP_ID_CONFIG, "test-consumer-group");
		return new KafkaConsumer<>(props);
	}

	@Override
	public void run() {
		try {
			runConsumer();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

}
