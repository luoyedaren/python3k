# -*- coding: utf-8 -*-

# coding:utf-8
import os
import sys

key = [0xAC, 0xEC, 0xDF, 0x57]

def crack_file(argv):
    filename = argv[0]
    new_name = argv[1]

    prePath = 'C:/Users/Administrator/PycharmProjects/tools/kugoutool/'
    file = open(prePath+filename, "rb")
    file.seek(1024, os.SEEK_SET)  # 偏移量1024
    changed_file = open(new_name, 'wb+')  # 以二进制追加写的方式打开

    try:
        b = file.read(4)  #  一次读4个字节  type(b)  --> 'bytes'
        while(b):
            for num,i in enumerate(b):
                h = i >> 4  # type(i) --> int
                l = i & 0xf
                kh = key[num] >> 4
                kl = key[num] & 0xf
                y = l ^ kl
                y = (h ^ kh ^ y) << 4 | y

                temp = bytes([y])  #  将int转为bytes
                changed_file.write(temp)
            b = file.read(4)
    except Exception as e:
        print(e)
    else:
        print("成功")
    finally:
        file.close()
        changed_file.close()

if __name__ == "__main__":
    crack_file(sys.argv[1:])