# -*- encoding: utf-8 -*-
'''
@author: xiaozhong
'''
import sys

sys.path.append("..")
from heart import CreateHear
from Binlog import Metadata


class Entrance(Metadata.TableMetadata):
    def __init__(self):
        pass

    def __start_client(self):
        '''启动客户端检查'''

    def __rollback(self):
        '''回滚'''

    def __append(self):
        '''追加'''

    def __enter__(self):

        #p = multiprocessing.Process(target=CheckDB, args=())
        #p.start()

        '''先注释掉'''
        CreateHear().listener()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
