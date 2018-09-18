#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
 Through paramiko access ssh
 '''
import paramiko

class SshHelper:

    start_appium='appium -a 192.168.21.30 -p 4726 --bootstrap-port 4780 --session-override --log "/usr/local/appium" --command-timeout 600 &'

    @staticmethod
    def ssh_connect(host,user,pwd):
        '''
        Get ssh client
        '''
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, 22, user, pwd)
        return client

    @staticmethod
    def ssh_cmd(host,user,pwd,cmd):
        try:
            ssh_client=SshHelper.ssh_connect(host,user,pwd)
            stdin,stdout,stderr=ssh_client.exec_command(cmd)
            print(stdout.readlines())
        except Exception as e:
            stderr =ssh_client.exec_command(cmd)
            print(stderr.readlines())
            print(e)

if __name__ == '__main__':
    SshHelper.ssh_cmd('192.168.21.30','root','123456',SshHelper.start_appium)


