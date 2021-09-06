# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
pip3 install pycryptodome
'''

import base64
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as PKCS1_signature
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher


def generate_key(private_key_file="rsa_private_key.pem", public_key_file="rsa_public_key.pem"):
    '''
    生成公私钥对
    :param private_key_file: 私钥文件存放路径
    :param public_key_file: 公钥文件存放路径
    :return:
    '''
    random_generator = Random.new().read
    rsa = RSA.generate(2048, random_generator)
    # 私钥
    private_key = rsa.exportKey()
    # print(f"privateKey:{private_key.decode('utf-8')}")
    # 公钥
    public_key = rsa.publickey().exportKey()
    # print(f"publicKey:{public_key.decode('utf-8')}")
    # 将密钥写入文件
    with open(private_key_file, "wb") as fp:
        fp.write(private_key)
    with open(public_key_file, "wb") as fp:
        fp.write(public_key)
    print("generate rsa key success.")
    print(f"private_file:{private_key_file}, public_file:{public_key_file}")


def read_key_from_file(key_file):
    '''
    读取加密密钥
    :param key_file: 密钥文件
    :return:
    '''
    with open(key_file) as fp:
        data = fp.read()
        key = RSA.importKey(data)
    return key


def encrypt_text(public_key_file, message, key_length=2048):
    '''
    加密
    :param public_key_file: 公钥文件
    :param message: 明文内容
    :param key_length: 密钥长度
    :return:
    '''
    public_key = read_key_from_file(public_key_file)
    cipher = PKCS1_cipher.new(public_key)
    block_length = int(key_length / 8) - 11
    message_bytes = bytes(message.encode("utf8"))
    if len(message_bytes) <= block_length:
        encrypt_msg = base64.b64encode(cipher.encrypt(message_bytes))
        return encrypt_msg.decode('utf-8')
    else:
        encrypted_messages = []
        start = 0
        end = block_length
        while start < end <= len(message_bytes):
            mb = message_bytes[start: end]
            encrypt_msg = base64.b64encode(cipher.encrypt(mb))
            encrypted_messages.append(encrypt_msg.decode('utf-8'))
            start = end
            end = end + block_length if end + block_length <= len(message_bytes) else len(message_bytes)
        return "\n".join(encrypted_messages)


def decrypt_text(private_key_file, encrypt_message):
    '''
    解密
    :param private_key_file: 私钥文件
    :param encrypt_message: 密文内容
    :return:
    '''
    private_key = read_key_from_file(private_key_file)
    cipher = PKCS1_cipher.new(private_key)
    if encrypt_message.find("\n") <= 0:
        back_text = cipher.decrypt(base64.b64decode(encrypt_message), 0)
        return back_text.decode('utf-8')
    else:
        blocks = encrypt_message.split("\n")
        decrypted_messages_bytes = b""
        for block in blocks:
            back_text = cipher.decrypt(base64.b64decode(block), 0)
            decrypted_messages_bytes += back_text
        return decrypted_messages_bytes.decode("utf-8")


def encrypt_text_file(public_key_file, text_file, encrypted_file):
    '''
    加密文本文件
    :param public_key_file: 公钥
    :param text_file: 原始文本文件
    :param encrypted_file: 加密后文件
    :return:
    '''
    with open(text_file, encoding="utf8") as fp:
        message = fp.read()
    encrypted_text = encrypt_text(public_key_file, message)
    # 写入加密后文件
    with open(encrypted_file, "w") as fp:
        fp.write(encrypted_text)
    print(f"finish encrypt text file. {text_file} => {encrypted_file}")


def decrypt_text_file(private_key_file, encrypted_file, text_file=None, to_console=True):
    '''
    解密文本文件
    :param private_key_file: 私钥
    :param encrypted_file: 加密后的文本文件
    :param text_file: 解密后的文本文件
    :param to_console: 是否输出到控制台
    :return:
    '''
    with open(encrypted_file, encoding="utf8") as fp:
        message = fp.read()
    decrypted_text = decrypt_text(private_key_file, message)
    # 写入加密后文件
    with open(text_file, "w") as fp:
        fp.write(decrypted_text)
    if to_console:
        print("-"*10 + "Start: decrypted text file content" + "-"*20)
        print(decrypted_text)
        print("-"*10 + "End: decrypted text file content" + "-"*20)
    print(f"finish decrypt text file. {encrypted_file} => {text_file}")


if __name__ == '__main__':

    # 公私钥文件存放路径
    public_key_file = "data/my_keys/wang_rsa_public_key.pem"
    private_key_file = "data/my_keys/wang_rsa_private_key.pem"

    # 生成密钥
    # generate_key(private_key_file=private_key_file, public_key_file=public_key_file)

    '''加解密字符串'''
    # 加密
    # encrypted_message = encrypt_text(public_key_file, "今天天气正好啊。")
    # print(encrypted_message)
    # 解密
    # decrypted_message = decrypt_text(private_key_file, encrypted_message)
    # print(decrypted_message)

    '''加解密文本文件'''
    # text_file = "data/wang_message_0412.txt"
    encrypted_file = "data/rar_password_0413.txt"
    decrypt_file = "data/rar_password_decrypt_0413.txt"
    # 加密文本文件
    # encrypt_text_file(public_key_file, text_file, encrypted_file)
    # 解密文本文件
    decrypt_text_file(private_key_file, encrypted_file, decrypt_file)
