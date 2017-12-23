# -*- encoding: utf-8 -*-
'''
@author: xiaozhong
'''
import sys,time
sys.path.append("..")
import zkhandle
from Loging import Logging
from config import get_config
from Binlog import Metadata
from CheckDB import CheckDB
import multiprocessing


class Entrance(Metadata.TableMetadata):
    def __init__(self):
        pass

    def __start_client(self):
        '''启动客户端检查'''

    def __rollback(self):
        '''回滚'''

    def __append(self):
        '''追加'''

    def __entry(self):
        '''总入口'''

    def __enter__(self):

        p = multiprocessing.Process(target=CheckDB, args=())
        p.start()

        '''先注释掉'''
        #with zkhandle.ZkHandle():
        #    pass

