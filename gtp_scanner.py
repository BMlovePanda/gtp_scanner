from scapy.all import *
import concurrent.futures

with open("./gtp_ip_list.txt") as f:
    target_ip_list = [line.strip() for line in f.readlines()]

target_port_list = [2152, 2123]
#payload来源metasloit的gtp探测模块
payload_list = [
    b"\x32\x01\x00\x02\x00\x00\x00\x00\x00\x00",  # GTP Version 1
    b"\x40\x01\x00\x04\x00\x00\x00\x00"           # GTP Version 2
]

timeout = 3

output_file = open('gtp_scan_results.txt', 'w')
output_file.write('IP,Port,GTP_Version\n')

# 定义发送 GTP 数据包的函数
def send_gtp_packet(target_ip, target_port, payload):
    pkt = IP(dst=target_ip) / UDP(dport=target_port, sport=RandShort()) / Raw(payload)
    response = sr1(pkt, timeout=timeout, verbose=0)
    if response:
        version = payload_list.index(payload) + 1
        output_message = f"{target_ip},{target_port},{version}\n"
        # 写入文件
        output_file.write(output_message)

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures = []
    for target_ip in target_ip_list:
        for target_port in target_port_list:
            for payload in payload_list:
                futures.append(executor.submit(send_gtp_packet, target_ip, target_port, payload))
    concurrent.futures.wait(futures)

output_file.close()
