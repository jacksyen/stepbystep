package com.hedwig.stepbystep.javatutorial.httpclient.base;

import java.io.IOException;
import java.io.InputStream;

import org.apache.http.HttpEntity;
import org.apache.http.auth.AuthenticationException;
import org.apache.http.auth.UsernamePasswordCredentials;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.auth.BasicScheme;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClientBuilder;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class HttpClientBasicPostLiveTest {

    private static final String SAMPLE_URL = "http://www.github.com";

    private CloseableHttpClient instance;

    private CloseableHttpResponse response;

    @Before
    public final void before() {
        instance = HttpClientBuilder.create().build();
    }

    @After
    public final void after() throws IllegalStateException, IOException {
        if (response == null) {
            return;
        }

        try {
            final HttpEntity entity = response.getEntity();
            if (entity != null) {
                final InputStream instream = entity.getContent();
                instream.close();
            }
        } finally {
            response.close();
        }
    }

    // tests - non-GET

    @Test
    public final void whenExecutingPostRequest_thenNoExceptions() throws ClientProtocolException, IOException {
        instance.execute(new HttpPost(SAMPLE_URL));
    }

    @Test
    public final void whenExecutingPostRequestWithBody_thenNoExceptions() throws ClientProtocolException, IOException {
        final HttpPost request = new HttpPost(SAMPLE_URL);
        request.setEntity(new StringEntity("in the body of the POST"));
        instance.execute(request);
    }

    @Test
    public final void givenAuth_whenExecutingPostRequestWithBody_thenNoExceptions() throws ClientProtocolException, IOException, AuthenticationException {
        final HttpPost request = new HttpPost(SAMPLE_URL);
        request.setEntity(new StringEntity("in the body of the POST"));
        final UsernamePasswordCredentials creds = new UsernamePasswordCredentials("username", "password");
        request.addHeader(new BasicScheme().authenticate(creds, request, null));
        instance.execute(request);
    }

}
