from collections import deque
import random
import socket
import struct
import time

from class_test import A, B, C, D, TestClass


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
        ntp_data = b"\x1b" + 47 * b"\0"
        client_socket.sendto(ntp_data, (ntp_server, 123))

        # 接收服务器返回的数据
        response, address = client_socket.recvfrom(1024)

        # 解析时间戳
        ntp_timestamp = struct.unpack("!12I", response)[10]

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


def crc8(data: list):
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


def set_global_variable():
    global global_variable
    global_variable = 20


def access_global_variable():
    global global_variable
    global_variable += 12
    print("Global variable:", global_variable)


def set_obj_b():
    global obj_b
    obj_b = B()


def obj_b_method():
    global obj_b

    obj_b.method()

if __name__ == "__main__":
    # 获取时间并打印
    # print(get_ntp_time())

    # find_max()
    message = [0x02, 0x09, 0x03, 0x45, 0x23, 0xAE, 0xAA]

    result_crc = crc8(message)
    # print(result_crc)
    print(f"CRC-8: 0x{result_crc:02X}")

    message_queue = deque(message)
    print(type(message_queue))

    message_queue.popleft()
    print(message_queue)

    message_queue.append(0x12)
    print(message_queue)

    message_queue.appendleft(0x0A)
    print(message_queue)

    message_queue.extend(deque([0x01, 0x88, 0x19]))
    print(f"message_queue:      {message_queue}")

    queue_test = TestClass(
        message_queue,
    )
    test = queue_test.message
    test.pop()
    print(f"test:               {test}")
    queue_test.message.pop()
    print(f"queue_test.message: {queue_test.message}")

    message_queue.extendleft([int(num) for num in range(3)])
    print(message_queue)

    obj_d = D()
    obj_d.method()

    # # 查看各个类的 MRO
    # print("MRO for class A:", A.__mro__)
    # print("MRO for class B:", B.__mro__)
    # print("MRO for class C:", C.__mro__)
    # print("MRO for class D:", D.__mro__)

    set_global_variable()

    access_global_variable()

    set_obj_b()
    obj_b_method()