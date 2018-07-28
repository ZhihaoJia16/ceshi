#封装一个模块，并发布、安装

#步骤如下
 
dir #显示当前目录的文件
cd Desktop #进入桌面
cd shicao3  #打开包文件
python setup.py build #建立包
python setup.py sdist #压缩包
cd dist   #进入dist文件夹
cd PKG1-2.0  #进入文件夹
python setup.py install  #安装包