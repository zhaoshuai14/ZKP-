import random
from math import pow

a = random.randint(2, 10) #产生小于p的随机常数a


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
        return gcd(b, a % b)

    # Generating large random numbers


def gen_key(q):
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)

    return key


# Modular exponentiation
def power(a, b, c):
    x = 1
    y = a

    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)

    return x % c


# Asymmetric encryption
def encrypt(msg, p, h, r):
    en_msg = []

    b = gen_key(p)  # 得b
    print("b",b)
    K = power(h, b, p)#K=(Sa)^b mod p
    u = power(r, b, p) #u=Sb=r^b mod p
    print("K:",K)

    for i in range(0, len(msg)):
        en_msg.append(msg[i])

    print("u : ", u)
    # print("(Sa)^b mod p used : ", K)
    for i in range(0, len(en_msg)):
        en_msg[i] = K * ord(en_msg[i])
    print("w : ", en_msg)
    return en_msg, u


def decrypt(w, u, a, p):
    dr_msg = []
    h = power(u, a, p)
    for i in range(0, len(w)):
        dr_msg.append(chr(int(w[i] / h)))

    return dr_msg


# Driver code
def main():
    msg = '01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234'               # 共125位数字，1000bit
    print("明文 :", msg)

    p = random.randint(pow(10, 20), pow(10, 50))# 获得大素数q
    print("p",p)
    r = random.randint(2, p)#得r

    a = gen_key(p)  # Private key for receiver
    print("私钥：",a)
    h = power(r, a, p)
    print("h:",h)
    #s=h**a
    #print("s:",s)
    

    w, u = encrypt(msg, p, h, r)
    dr_msg = decrypt(w, u, a, p)
    dmsg = ''.join(dr_msg)
    print("解密后文 :", dmsg);


if __name__ == '__main__':
    main()
