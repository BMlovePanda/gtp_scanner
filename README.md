# gtp_scanner
用于探测gtp协议
gtp协议是udp端口，只是探测的话可能曾在误报
结合metasploit的gtp探测模块，抓包发现GTP V1和V2协议中的不同报文，编写针对2123和2152端口的协议探测。

目前测试了一下，准确度和metasploit的结果基本一致。
通过一下命令安装需要的库
```
pip install -r requirements.txt
```

请放心服用
