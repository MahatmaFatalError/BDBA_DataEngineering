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
	 * @param args path to csv file
	 * @throws Exception
	 */
	public static void main(String[] args) throws Exception {

		String csvFilePath = "/data/311_Service_Requests_from_2010_to_Present.csv";

		if (args != null && args.length > 0 && !StringUtils.isBlank(args[0])){
			csvFilePath = args[0];
		}

		MyProducer producer = new MyProducer(csvFilePath);
		MyConsumer consumer = new MyConsumer();

		new Thread(producer).start();
		new Thread(consumer).start();

	}
}
