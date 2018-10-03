def encode():
    message = input("输入消息: ")
    key = int(input("输入密钥: "))
    encode_message = []
    for ch in message:
        encode_message.append(chr(ord(ch) + key))

    encode_message = ''.join(encode_message)
    print(encode_message)


def decode():
    encode_message = input("输入密文: ")
    key = int(input("输入密钥: "))
    decode_message = []
    for ch in encode_message:
        decode_message.append(chr(ord(ch) - key))

    decode_message = ''.join(decode_message)
    print(decode_message)


encode()
decode()
