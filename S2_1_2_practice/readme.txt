﻿#写一个文件读写的程序，并在其中加入异常处理
'''
异常处理一般使用try-except-finally组合，需要注意的是，close文件时也要使用异常处理，
因为文件若打不开并执行异常处理后，再执行close时就会报错。

'''