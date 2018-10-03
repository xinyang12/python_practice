def main():
    lower_alpha = 'abcdefghijklmnopqrstuvwxyz'
    message = input("输入消息: ")
    key = int(input("输入密钥: "))
    encode_message = []
    for ch in message:
        index = ord(ch) - ord('a')
        encode_message.append(lower_alpha[(index + key) % 26])

    encode_message = "".join(encode_message)
    print(encode_message)


main()
