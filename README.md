# 小圣杯监测脚本
本程序为python脚本，作用是辅助找出使用脚本/手动高强度挂单的用户。   
使用过程中如想退出或重来，按`Ctrl + c`即可。

相关帖：https://bgm.tv/group/topic/354526
## 使用方法

### 在repl.it中运行（推荐）
 
 + 打开 https://repl.it/ 
 + 点击网页最右上角的 `+ new repl`
 + 使用 `python` 而非 `python2.7` 创建一个repl。
 + 将 `monitoring_r.py` 里的代码复制到新创建的repl中
 + 点击网页正上方的 `run` 来运行
 
 注：第一次运行需要初始化，请耐心等待即可

### 电脑端直接运行  

+ MacOS用户可直接运行 `monitoring_r` 文件  
+ Windows用户可直接运行 `monitoring_nr.exe` 文件  

注：可执行文件由`pyinstaller`打包生成，可能出现各种bug

### 在本地python环境运行

原脚本 `monitoring_r.py` 推荐在python版本>=3.6以上运行，需安装`requests`库，同时保证运行环境接入互联网。

由于`monitoring_r.py`脚本中的多线程任务在windows中会触发bug，所以增加了windows可用的单线程版本的`monitoring_nr.py`，效率可能稍有降低。

---
## 运行错误

使用过程中如果出现含有提示 `time out` 或 `Max retries exceeded with url`的错误，则意味着脚本短时间内请求过多过快，可通过增加白名单用户及延长检测间隔秒数解决。

