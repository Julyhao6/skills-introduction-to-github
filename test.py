from gmssl import sm2

# 生成密钥对
private_key = '00B9AB0B828FF68872F21A837FC303668428DEA11DCD1B24429D0C99E24EED83D'
public_key = 'B9C9A6E04E9C91F7BA880429273747D7EF5DDEB0BB2FF6317EB00BEF331A83081A6994B8993F3F5D6EADDDB81872266C87C018FB4162F5AF347B483E24620207'

sm2_crypt = sm2.CryptSM2(
    public_key=public_key, private_key=private_key)
data = b"bonddigit_user:admin password:654qwe123!"
# 加密
enc_data = sm2_crypt.encrypt(data)
# 解密
dec_data = sm2_crypt.decrypt(enc_data)

print(f"原始数据: {data}")
print(f"加密后的数据: {enc_data.hex()}")
print(f"解密后的数据: {dec_data}")
