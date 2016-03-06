package com.hedwig.stepbystep.javatutorial.helpers;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

/**
 * 属性工具类
 */
public class PropertiesHelper {
    private static final Logger logger = LogManager.getLogger(PropertiesHelper.class.getName());
    private final static String TEST_ENV_SETTING="env.properties";
    private static Properties properties ;
    private PropertiesHelper(){}
    static{

        if(null==properties){
            init();
        }
    }

    /**
     * load properties
     */
    public static void init(){
        properties = new Properties();
        InputStream in = null;
        try{
            in = PropertiesHelper.class.getClassLoader().getResourceAsStream(TEST_ENV_SETTING);
            properties.load(in);
        } catch (IOException e){
            logger.error("error= {}" , e);
            logger.error("load properties failed, please check the file {}",TEST_ENV_SETTING);
        }finally {
            try {
               if(in!=null){
                in.close();
               }
            } catch (IOException e) {
                logger.error("load properties failed {}", e);
            }
        }
    }

    /**
     * return property by key
     * @param key
     * @return
     */
    public static String getValueFor(String key){
        return getProperty(key.toLowerCase());
    }

    public static String getProperty(String key){
        return null==properties.get(key.toLowerCase())?null:properties.get(key.toLowerCase()).toString();
    }

    public static int getProperty(String key, int defaultValue){
        return null==getProperty(key.toLowerCase())?defaultValue:Integer.valueOf(getProperty(key.toLowerCase()));
    }

    public static String getProperty(String key, String defaultValue){
        return null==getProperty(key.toLowerCase())?defaultValue:getProperty(key.toLowerCase());
    }
}
