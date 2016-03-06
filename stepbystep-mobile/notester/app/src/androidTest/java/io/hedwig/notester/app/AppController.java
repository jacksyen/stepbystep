package io.hedwig.notester.app;

import android.app.Application;
import android.content.Context;
import android.text.TextUtils;

import io.hedwig.notester.BuildConfig;

/**
 * Created by patrick on 16/3/5.
 */
public class AppController extends Application {

    private static Context context;

    public static Context getContext(){
        return context;
    }


    @Override
    public void onCreate() {
        super.onCreate();
        context=this;
        if(!BuildConfig.DEBUG){
            Thread.setDefaultUncaughtExceptionHandler(new AppExceptionHandler(this));
        }


//        // 友盟账号统计
//        if (!TextUtils.isEmpty(LoginShared.getAccessToken(this))) {
//            MobclickAgent.onProfileSignIn(LoginShared.getLoginName(this));
//        } else {
//            MobclickAgent.onProfileSignOff();
//        }

    }
}
