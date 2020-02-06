# 小圣杯监测脚本
本程序为python脚本，目的为辅助找出使用脚本挂单的用户。 
使用过程中如想退出或重来，按`Ctrl + c`即可。

## 使用说明

 可执行文件由`pyinstaller`生成，可能出现各种bug，以下为解决方案：
 
 + 在 https://repl.it/ 上注册账号
 + 使用 `python` 而非 `python2.7` 创建一个repl。
 + 将 `monitoring_r.py` 里的代码复制到新创建的repl中
 + 点击正上方的 `run` 来运行
 
 注：第一次运行需要初始化，请耐心等待即可
 
 ----------------------------

可执行文件只支持电脑端使用：  

+ MacOS用户可直接运行 `monitoring_r` 文件  
+ Windows用户可直接运行 `monitoring_nr.exe` 文件  

原脚本 `monitoring_r.py` 推荐在python版本>=3.6以上运行，需安装`requests`库，同时保证运行环境接入互联网。

由于`monitoring_r.py`脚本中的多线程任务在windows中会触发bug，所以增加了windows可用的单线程版本的`monitoring_nr.py`，效率可能稍有降低。

## 运行错误

使用过程中如果出现含有提示 `time out` 或 `Max retries exceeded with url`的错误，则意味着脚本短时间内请求过多过快，可通过增加白名单用户及延长检测间隔秒数解决。


