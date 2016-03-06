package com.hedwig;

import org.joda.time.DateTime;
import org.joda.time.Days;
import org.joda.time.Minutes;
import java.util.Date;

/**
 * Created with IntelliJ IDEA.
 * PackageName:com.dooioo.help.util
 * Author: pengfei
 * Create: pengfei (2015/3/27 15:35)
 * Description:反馈、保修等待时间计算工具类
 */
public class DurationUtils {
    private String sTime;
    private String eTime;
    private String time;

    public static String formatDuration(Date startTime, Date endTime){
        return formatDuration(computeMinuteDiff(startTime, endTime));
    }

    /**
     * 把等待时间（单位为分钟），格式化为页面展示的格式（xx天xx小时xx分）
     * @param duration
     * @return
     */
    public static String formatDuration(Integer duration){
        if(duration == null){
            return null;
        }

        int days = duration / (9 * 60);
        int hours = duration % (9 * 60) / 60;
        int minutes = duration % (60);

        StringBuilder sb = new StringBuilder();
        if(days > 0){
            sb.append(days).append(" 天 ");
        }
        if(hours > 0){
            sb.append(hours).append(" 小时 ");
        }
        if(minutes >= 0){
            sb.append(minutes).append(" 分 ");
        }
        return sb.toString();
    }

    /**
     * 计算两个时间之间相差的工作时间分钟数
     * @param startTime
     * @param endTime
     * @return
     */
    public static Integer computeMinuteDiff(Date startTime, Date endTime){
        if(startTime == null || endTime == null){
            return null;
        }
        if(startTime.getTime() > endTime.getTime()){
            return computeMinuteDiff(endTime, startTime);
        }

        DateTime startDateTime = convert2WorkTime(startTime);
        DateTime endDateTime = convert2WorkTime(endTime);

        int dayDiff = 0;
        Date startDateHMS = new Date(1990, 01, 01, startTime.getHours(), startTime.getMinutes(), startTime.getSeconds());
        Date endDateHMS = new Date(1990, 01, 01, endTime.getHours(), endTime.getMinutes(), endTime.getSeconds());
        while(Days.daysBetween(startDateTime, endDateTime).getDays() != 0){
            if(startDateTime.getDayOfWeek() == 6 || startDateTime.getDayOfWeek() == 7){
                startDateTime = startDateTime.plusDays(1);
                continue;
            }
            if (startDateTime.getDayOfWeek() == 5 && startDateHMS.after(endDateHMS)){
                startDateTime = startDateTime.plusDays(1);
                continue;
            }
            startDateTime = startDateTime.plusDays(1);
            dayDiff++;
        }
        int minuteDiff = dayDiff * 9 * 60;

        int i = Minutes.minutesBetween(startDateTime, endDateTime).getMinutes();
        if(i > 9 * 60){
            i = i - (24 - 18) * 60 - 9 * 60;
        }

        return minuteDiff + i;
    }

    /**
     * 把时间转化为工作时间
     * @param date
     * @return
     */
    private static DateTime convert2WorkTime(Date date){
        DateTime dateTime = new DateTime(date);
        if(dateTime.getDayOfWeek() == 6 || dateTime.getDayOfWeek() == 7){
            dateTime = dateTime.plusDays(6).dayOfWeek().setCopy(1).minuteOfDay().setCopy(9 * 60);
        }else{
            if(dateTime.getHourOfDay() < 9){
                dateTime = dateTime.minuteOfDay().setCopy(9 * 60);
            }else if(dateTime.getMinuteOfDay() > 18 * 60){
                dateTime = dateTime.minuteOfDay().setCopy(18 * 60);
            }
        }
        return dateTime;
    }

    /**
     * 处理开始时间，转换为工作时间算法，剔除部分了非工作时间
     * @param startDateTime
     * @return
     */
    private static DateTime processStartTime(DateTime startDateTime){
        // 先解决开始时间的问题
        if(startDateTime.getHourOfDay() < 9) {
            // 如果是当天9点以前的提交就相当于当天9点提的反馈
            startDateTime = startDateTime.minuteOfDay().setCopy(9*60);
        }else if(startDateTime.getHourOfDay() >= 18) {
            // 如果是工作日的18点以后提交就可以相当于第二天9点提的反馈，这是一个坑要，多注意
            startDateTime = startDateTime.plusDays(1).minuteOfDay().setCopy(9*60);
        }
        // 调整时间之后，如果发现加了一天之后，是周末，就直接当作下周一9点提交的反馈
        if (startDateTime.getDayOfWeek() == 6){
            startDateTime = startDateTime.plusDays(2).dayOfWeek().setCopy(1).secondOfDay().setCopy(9 * 60 * 60);
        }else if(startDateTime.getDayOfWeek() == 7){
            startDateTime = startDateTime.plusDays(1).dayOfWeek().setCopy(1).secondOfDay().setCopy(9 * 60 * 60);
        }
        return startDateTime;
    }

    /**
     * 处理结束时间，转换为工作时间算法，剔除部分了非工作时间
     * @param startDateTime
     * @param endDateTime
     * @return
     */
    private static DateTime processEndTime(DateTime startDateTime, DateTime endDateTime){
        // 结束时间不在工作时间的话,分别倒退1天至两天，相当于去除整天的非工作时间
        if(endDateTime.getDayOfWeek() == 6){
            // 结束时间是周六
            endDateTime = endDateTime.minuteOfDay().setCopy(18*60).minusDays(1);
        }else if(endDateTime.getDayOfWeek() == 7){
            // 结束时间是周日
            endDateTime = endDateTime.minuteOfDay().setCopy(18*60).minusDays(2);
        }else {
            if(endDateTime.getHourOfDay()<9){
                endDateTime = endDateTime.minuteOfDay().setCopy(9*60);
            }else if(endDateTime.getHourOfDay() >= 18){
                endDateTime = endDateTime.minuteOfDay().setCopy(18*60);
            }
            // 结束时间是工作日，就要刨去之间的周六周日了(这里要处理跨年的问题)
            int startTimeWeekOfWeekyear = startDateTime.weekOfWeekyear().get();
            int endTimeWeekOfWeekyear = endDateTime.weekOfWeekyear().get();
            if (endTimeWeekOfWeekyear < startTimeWeekOfWeekyear){
                endTimeWeekOfWeekyear = startTimeWeekOfWeekyear + endTimeWeekOfWeekyear;
            }
            int weekends = endTimeWeekOfWeekyear - startTimeWeekOfWeekyear;//两个日期之间间隔了几个周末
            endDateTime = endDateTime.minusDays(weekends*2);
        }
        return endDateTime;
    }

    /**
     * 计算两个时间之内的等待时间，其中是去除了非工作时间
     * 具体规则参照:http://chandao.dooioo.com/story-view-3933-3-project-544.html
     * @param startTime
     * @param endTime
     * @return 给定的两个时间之间相差的分钟数，并且已经去掉了非工作时间的分钟数
     */
    public static Integer calWaitingTimeWithOutWorkTime(Date startTime,Date endTime){
        if(startTime == null || endTime == null){
            return null;
        }
        if(startTime.getTime() > endTime.getTime()){
            return computeMinuteDiff(endTime, startTime);
        }
        DateTime startDateTime = new DateTime(startTime);
        DateTime endDateTime = new DateTime(endTime);
        startDateTime = processStartTime(startDateTime);
        endDateTime = processEndTime(startDateTime,endDateTime);
        // 计算两个时间之间相差的分钟数量
        int minutesDiff = Minutes.minutesBetween(startDateTime, endDateTime).getMinutes();
        // 计算两个日期之间相差几天，方便下面去除非工作时间
        int betweenDays = Days.daysBetween(startDateTime.hourOfDay().setCopy(0).minuteOfDay().setCopy(0)
                                          ,endDateTime.hourOfDay().setCopy(0).minuteOfDay().setCopy(0)).getDays();
        if(minutesDiff > 9 * 60){
            minutesDiff = minutesDiff -((24-18)*60 + 9*60)*betweenDays;
        }
        return minutesDiff;
    }

    public String getsTime() {
        return sTime;
    }

    public void setsTime(String sTime) {
        this.sTime = sTime;
    }

    public String geteTime() {
        return eTime;
    }

    public void seteTime(String eTime) {
        this.eTime = eTime;
    }


    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
}
