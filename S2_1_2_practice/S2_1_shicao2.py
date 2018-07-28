#写一个文件读写的程序，并在其中加入异常处理

try:
    f=open('testShicao.txt','r',encoding='utf-8')
    f.write('这是一个测试文件')
except (ZeroDivisionError,FileNotFoundError,ValueError,Exception) as result:
    print('文件打开异常')
    print(result)  #result.args
    print(result.args)
    print(type(result))
finally:
    print('感谢使用！')
    try:
        f.close()
    except Exception as e:
        print(e.args)