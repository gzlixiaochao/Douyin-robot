# -*- coding: utf-8 -*-
import os
import subprocess
import platform

class auto_adb():
    def __init__(self):
        try:
            adb_path = 'adb'
            subprocess.Popen([adb_path], stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
            self.adb_path = adb_path
        except OSError:
            print("请安装 ADB 及驱动并配置环境变量")
        exit(1)

    def get_screen(self):
        process = os.popen(self.adb_path + ' shell wm size')
        output = process.read()
        return output

    def run(self, raw_command):
        print(raw_command)
        command = '{} {}'.format(self.adb_path, raw_command)
        process = os.popen(command)
        output = process.read()
        return output

    def test_device(self):
        print("检查设备是否连接...")
