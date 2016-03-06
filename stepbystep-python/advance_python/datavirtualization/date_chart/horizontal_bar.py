# _*_ coding=utf-8 _*_
import pygal

__author__ = 'patrick'

bar=pygal.HorizontalBar()
bar.title='Searches for term: sleep in April'
bar.add('Searches',[81,88,88,100])
bar.render_to_file('bar_char.svg')