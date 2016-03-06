# _*_ coding=utf-8 _*_
import random

__author__ = 'patrick'

# 定义一个20*5的二维数组，用来存储某班级20位学员的5门课的成绩；这5门课按存储顺序依次为：
# core C++，coreJava，Servlet，JSP和EJB。
# （1）循环给二维数组的每一个元素赋0~100之间的随机整数。
# （2）按照列表的方式输出这些学员的每门课程的成绩。
# （3）要求编写程序求每个学员的总分，将其保留在另外一个一维数组中。
# （4）要求编写程序求所有学员的某门课程的平均

courses = "core C++,coreJava,Servlet,JSP,EJB"
course_list = courses.split(",")
print(courses)

student_num = 20
student_score_list = [[random.randint(1, 100) for i in range(student_num)] for n in range(len(course_list))]
print(student_score_list)

everyone_score = [student_score_list[j][i] for j in range(len(course_list)) for i in range(student_num)]
ave_course_score = [sum(student_score_list[i]) / len(student_score_list) for i in range(len(course_list))]
every_course_total = [sum(everyone_score) for i in range(student_num)]
print everyone_score
print ave_course_score
print(every_course_total)