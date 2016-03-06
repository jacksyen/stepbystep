package io.hedwig.notester.app;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;

/**
 * Created by patrick on 16/3/5.
 */
public class AppExceptionHandler implements Thread.UncaughtExceptionHandler {
    private Context context;

    public AppExceptionHandler(Context context) {
        this.context = context;
    }

    @Override
    public void uncaughtException(Thread thread, Throwable ex) {
//        Intent intent = new Intent(context,CrashLogActivity.class);
//        intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
//        Bundle bundle = new Bundle();
//        bundle.putSerializable("e", ex);
//        intent.putExtras(bundle);
//        context.startActivity(intent);
//        System.exit(1);

    }
}
