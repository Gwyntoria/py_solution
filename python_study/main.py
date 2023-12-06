import random
import socket
import struct
import time


def get_ntp_time():
    # NTP服务器地址
    ntp_server = "time.google.com"

    # 创建UDP套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 设置超时时间为1秒
    client_socket.settimeout(1)

    # NTP协议使用的时间戳是自1900年1月1日以来的秒数，加上70年的偏移量
    ntp_timestamp_offset = 2208988800

    try:
        # 发送时间请求数据
        ntp_data = b'\x1b' + 47 * b'\0'
        client_socket.sendto(ntp_data, (ntp_server, 123))

        # 接收服务器返回的数据
        response, address = client_socket.recvfrom(1024)

        # 解析时间戳
        ntp_timestamp = struct.unpack('!12I', response)[10]

        # 转换为普通时间
        ntp_time = ntp_timestamp - ntp_timestamp_offset
        return time.ctime(ntp_time)

    except socket.timeout:
        print("请求超时")

    finally:
        # 关闭套接字连接
        client_socket.close()


def find_max():
    n = eval(input("请输入数字的个数:"))
    max_v = eval(input("输入第1个数字:"))

    for i in range(0, n - 1):
        x = eval(input("请输入第{}个数字：".format(i + 2)))
        if x > max_v:
            max_v = x
        else:
            x = 0

    print("The max value: ", max_v)


def generate_number():
    if random.random() < 0.5:
        # 生成数字8的情况
        return 8
    else:
        # 生成其他数字的情况，可以使用random.randint(0, 9)生成[0, 9]范围内的随机整数
        return random.randint(0, 7)


def crc8(data):
    crc8_polynomial = 0x07
    crc = 0

    for byte in data:
        crc ^= byte  # 异或当前数据字节

        for _ in range(8):
            if crc & 0x80:
                crc = (crc << 1) ^ crc8_polynomial
            else:
                crc <<= 1

    return crc & 0xFF


if __name__ == '__main__':
    # 获取时间并打印
    # print(get_ntp_time())

    # find_max()

    # 要计算CRC-8的数据
    message = bytearray([0x02, 0x09, 0x03])

    result_crc = crc8(message)
    # print(result_crc)
    print(f"CRC-8: 0x{result_crc:02X}")
