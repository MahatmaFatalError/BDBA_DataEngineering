package com.srh.bdba.dataengineering;

/**
 * starts both a produces and a consumer thread in parallel
 * @author jruppel
 *
 */
public class Main {

	public static void main(String[] args) throws Exception {

		MyProducer producer = new MyProducer("/data/311_Service_Requests_from_2010_to_Present.csv");
		MyConsumer consumer = new MyConsumer();

		new Thread(producer).start();
		new Thread(consumer).start();

	}
}
