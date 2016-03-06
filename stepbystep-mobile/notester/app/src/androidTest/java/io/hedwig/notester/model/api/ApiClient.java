package io.hedwig.notester.model.api;

import retrofit.RestAdapter;

/**
 * Created by patrick on 16/3/5.
 */
//todo use enum
public final class ApiClient {

    private ApiClient(){}

    public static final ApiService service = new RestAdapter.Builder()
            .setEndpoint(ApiDefine.API_HOST)
            .setConverter(new GsonConverter(GsonWrapper.gson))
            .setRequestInterceptor(new ApiRequestInterceptor())
            .setLogLevel(BuildConfig.DEBUG ? RestAdapter.LogLevel.FULL : RestAdapter.LogLevel.NONE)
            .build()
            .create(ApiService.class);

}
