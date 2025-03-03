from gmssl import sm3, func

def content_to_sm3(text):
    # 将消息编码为字节类型
    message_bytes = text.encode()
    # 计算 SM3 哈希值
    hash_hex = sm3.sm3_hash(func.bytes_to_list(message_bytes))
    return hash_hex

if __name__ == '__main__':
    # 待加密的消息
    text = "邦得数字账号:jedkw 密码:23rfkl23"
    # 调用加密函数
    hash_result = content_to_sm3(text)
    print(f"原始消息: {text}")
    print(f"SM3 加密结果: {hash_result}")
