# _*_ coding=utf-8 _*_
from datetime import datetime
import pygal

__author__ = 'patrick'

date_y=pygal.DateY()
Date_Y = pygal.DateY(x_label_rotation=25)
date_y.title="Fightings and amount of passaeges"
date_y.add("Arrival",[
    (datetime(2014,1,5),42),
    (datetime(2014, 1, 14), 123),
    (datetime(2014, 2, 2), 97),
    (datetime(2014, 3, 22), 164)
])
date_y.render_to_file('datey_chart.svg')
