package io.hedwig.concurrent.thread.threadsInThreadLocal;


import java.util.Random;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;

/**
 * Created by patrick on 16/2/19.
 */
public class ThreadInThreadLocals {
    private ThreadLocal<String> localThreads = new ThreadLocal<>();

    public String getCurrentString(){
        if (localThreads.get()==null) {
            localThreads.set(Thread.currentThread().getName());
        }
        return localThreads.get();
    }

    public Future<String> getFutureString(){
        CompletableFuture<String> future = new CompletableFuture<>();
        new Thread(){
            @Override
            public void run() {
                System.out.println(Thread.currentThread().getName());
                System.out.println(getCurrentString());
                future.complete(getCurrentString());
                if(new Random().nextBoolean()){
                    throw new RuntimeException("throw exceptions");
                }
            }
        }.start();
        return future;
    }

    public static void main(String[] args) throws ExecutionException, InterruptedException {
        ThreadInThreadLocals l = new ThreadInThreadLocals();
        System.out.println(l.getCurrentString());
        try{
            System.out.println(l.getFutureString().get());
        }catch (Exception e){
            System.out.println(e);
        }

    }
}
