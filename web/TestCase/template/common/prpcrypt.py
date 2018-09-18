# -*- coding: utf-8 -*-

# from binascii import b2a_hex, a2b_hex
# from Crypto.Cipher import DES
from pyDes import *
import random
'''加密解密工具类'''
class Prpcrypt:

    '''
    解密
    '''
    # @staticmethod
    # def decipher(seed,text):
    #     des = DES.new(seed)
    #     get_cryp = a2b_hex(text)
    #     after_text = des.decrypt(get_cryp)
    #     print(after_text)

    # '''
    # 解密
    # '''
    # @staticmethod
    # def crypt(seed,text):
    #     des = DES.new(seed)
    #     cryp = des.encrypt(text)
    #     pass_hex = b2a_hex(cryp)
    #     print(pass_hex)

    @staticmethod
    def encrypt(seed,data):
        k = des(seed, CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
        d = k.encrypt(data)
        print(d)
        return d

    @staticmethod
    def decrypt(seed,data):
        r = random.SystemRandom()
        r.seed(seed)
        p = r.getrandbits(8)
        print(p)



        k = des(p, CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
        d = k.decrypt(data)
        print(d)


if __name__ == "__main__":
    seed = 'test_KEY'
    text = '123456'
    p = Prpcrypt()
    d = p.encrypt(seed,text)
    p.decrypt(seed,d)

