#__init__=['test1','test2']
def test1():
    print('包1-模块1-test1')
def test2():
    print('包1-模块1-test2')
if __name__ == '__main__':
    test1()
    test2()
    print('此次是内部执行')

