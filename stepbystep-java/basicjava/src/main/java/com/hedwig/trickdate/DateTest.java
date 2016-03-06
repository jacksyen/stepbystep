package com.hedwig.trickdate;



import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.TimeZone;

/**
 * Created by patrick on 16/1/27.
 */
public class DateTest {

    public static void main(String[] args) throws ParseException {
        Date date = new Date();
        System.out.println(TimeZone.getTimeZone("CST"));
        date.setTime(1448692808000L); //1448692808000
//        date.setTime(1448784840000L);
        String dateString="2015-11-28 14:40:08";
        String t = "2015-11-28T14:40:08.000";
        SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
//        formatter.setTimeZone(TimeZone.getTimeZone("Asia/Shanghai"));
        System.out.println(formatter.getTimeZone());
        Date formatedDate =formatter.parse(dateString);
        //1448692808000
        System.out.println(formatedDate.getTime());
        System.out.println(date.getTime());

    }
}
