# 小圣杯监测脚本
本程序为python脚本，目的为辅助找出使用脚本挂单的用户。 
使用过程中如想退出或重来，按`Ctrl + c`即可。

目前只支持电脑端使用：
MacOS用户可直接运行 `monitoring_r` 文件  
Windows用户可直接运行 `monitoring_nr.exe` 文件  

原脚本 `monitoring_r.py` 推荐在python版本>=3.6以上运行，需安装`requests`库，同时保证运行环境接入互联网。

由于`monitoring_r.py`脚本中的多线程任务在windows中会触发bug，所以增加了windows可用的单线程版本的`monitoring_nr.py`，效率可能稍有降低。

使用过程中如果出现含有提示 `time out` 的错误，则意味着脚本短时间内请求过多过快，可通过增加白名单用户及延长检测间隔秒数解决。
