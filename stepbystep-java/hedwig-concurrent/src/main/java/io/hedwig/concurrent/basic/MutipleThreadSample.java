package io.hedwig.concurrent.basic;

import io.hedwig.concurrent.basic.tasks.CleanerTask;
import io.hedwig.concurrent.basic.tasks.Event;
import io.hedwig.concurrent.basic.tasks.WriterTask;

import java.util.ArrayDeque;
import java.util.Deque;


/**
 * Main class of the example. Creates three WriterTaks and a CleanerTask 
 *
 */
public class MutipleThreadSample {

	/**
	 * Main method of the example. Creates three WriterTasks and a CleanerTask
	 * @param args
	 */
	public static void main(String[] args) {
		
		// Creates the Event data structure
		Deque<Event> deque=new ArrayDeque<Event>();
		
		// Creates the three WriterTask and starts them
		WriterTask writer=new WriterTask(deque);
		for (int i=0; i<3; i++){
			Thread thread=new Thread(writer);
			thread.start();
		}
		
		// Creates a cleaner task and starts them
		CleanerTask cleaner=new CleanerTask(deque);
		cleaner.start();

	}

}