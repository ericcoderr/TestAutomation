'''
Pexpect is not working on windows platform .
'''
#import pexpect.popen_spawn
#import subprocess
import paramiko

class TestSsh:
    def ssh_cmd(self):
        #print(dir(pexpect.popen_spawn))

        #login_cmd = 'ssh %s@%s' % ('root', '192.168.21.30')
        #child = pexpect.popen_spawn.PopenSpawn(login_cmd)
        # p=subprocess.Popen(login_cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE )
        # a=p.wait()
        #print(a)

        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect('192.168.21.30', 22, 'root', '123456')

        stdin, stdout, stderr =client.exec_command('uptime')
        print(stdout.readlines())



        ## expect() 是期望的返回
        # child.expect('password:')
        # ## 输入密码
        # ret = child.sendline('123456')
        # ## 登录成功后, 会显示 [$, #, >>>] 等符号
        # child.expect('\$')
        #print(child)
        pass

if __name__ == '__main__':
    test_s = TestSsh()
    test_s.ssh_cmd()



