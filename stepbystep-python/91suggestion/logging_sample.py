# _*_ coding=utf-8 _*_
from logging import NullHandler
import logging

__author__ = 'patrick'

logging.getLogger(__name__).addHandler(NullHandler())



