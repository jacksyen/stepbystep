package io.hedwig.concurrent.basic;

/**
 * Created by patrick on 16/2/23.
 */
public class StartThread {
    public static void main(String[] args) {
        for (int i = 0; i <10 ; i++) {
            Calculator calculator=new Calculator(i);
            Thread thread=new Thread(calculator);
            thread.start();
        }
    }



}
