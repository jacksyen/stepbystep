package io.hedwig.concurrent.features;


import java.util.Random;
import java.util.concurrent.*;

/**
 * Created by patrick on 16/2/16.
 */
public class CompletableFutures {

    public static void main(String[] args) {
        Future<Boolean> future = getBooleanCompletableFuture();
        System.out.println("testing");
        System.out.println("testing");
        System.out.println("testing");
        System.out.println("testing");
        try {
            System.out.println("testing");
            System.out.println(future.get(2000L, TimeUnit.MILLISECONDS));
            System.out.println("testing");
            System.out.println("testing");
            System.out.println("testing");
        } catch (Exception e) {
            e.printStackTrace();
            throw new RuntimeException("timeout exception");
        }

        System.out.println("testing");
        System.out.println("testing");
        System.out.println("testing");
    }

    private static CompletableFuture<Boolean> getBooleanCompletableFuture() {
        CompletableFuture<Boolean> future = new CompletableFuture<>();
        Thread thread = new Thread() {

            @Override
            public void run() {
                try {
                    Thread.currentThread().sleep(1000L);
                    if (new Random().nextBoolean()){
                        throw new RuntimeException("testing");
                    }else{
                        future.completeExceptionally(new Exception("插入任务失败，事务失败回滚"));
                    }
                } catch (InterruptedException e) {
                    future.completeExceptionally(e);
                    return;
                }

                future.complete(true);
            }
        };

        thread.start();
        return future;
    }
}
