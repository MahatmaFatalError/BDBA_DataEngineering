package com.srh.bdba.dataengineering;

import org.apache.commons.lang3.StringUtils;

/**
 * starts both a produces and a consumer thread in parallel
 * @author jruppel
 *
 */
public class Main {

	/**
	 *
	 * @param args
	 * 		path to csv file
	 * 		postgresPW
	 *		postgresUser
	 *		postgresUrl
	 *		targetTable
	 *
	 * @throws Exception
	 */
	public static void main(String[] args) throws Exception {

		String csvFilePath = "/data/311_Service_Requests_from_2010_to_Present.csv";


		MyConsumer consumer = new MyConsumer();

		if (args != null && args.length > 0 && !StringUtils.isBlank(args[0])){
			csvFilePath = args[0].trim();

			if (args.length > 1){ // set PostgreSQL config
				consumer = new MyConsumer(args[1].trim(),args[2].trim(),args[3].trim(),args[4].trim());
			}


		}

		MyProducer producer = new MyProducer(csvFilePath);


		new Thread(producer).start();
		new Thread(consumer).start();

	}
}
