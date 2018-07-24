'''
异常处理之多分支处理
使用语句如下
try:
except:
else:
'''


a=input('请输入被除数')
b=input('请输入除数')
try:
    a=int(a)
    print('-----------')
    b=int(b)
    print('***********')
    c=a/b
    print('+++++++++++')
    print(c)

except ValueError:
    print('输入类型错误')
except ZeroDivisionError:
    print('除数不能为零')

except Exception:
    print('遇到异常')
else:
    print('商为：{0}'.format(c))
