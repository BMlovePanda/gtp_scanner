# gtp_scanner

## 这是啥
用于探测gtp协议

## 为啥写
gtp协议是udp端口，只是探测的话存在误报

## 怎么做
结合metasploit的gtp探测模块，抓包发现GTP V1和V2协议中的不同报文，编写针对的探测脚本

## 怎么用
通过一下命令安装需要的库
```
pip install -r requirements.txt
```
需要root权限

在gtp_ip_list.txt填写IP
```
sudo python gtp_scanner.py
```
在gtp_ip_result.txt中查看结果



准确度和metasploit的结果基本一致。

大家一起卷起来。


IP较多的话，可以用tqdm写个进度条，拒绝等待焦虑。
