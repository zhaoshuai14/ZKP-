ZKP（非交互式）零知识证明

2.1实验原理
1.零知识证明
允许一方说服另一方相信某个声明或事实的同时不泄露额外信息，即一方告诉另一方自己直到消息x，而无需传达任何信息，除了他知道x。本质是通过简单的揭露信息来证明某人具有某些信息的知识是微不足道的。

2.非交互式零知识证明
验证者提出的挑战由公开可信的随机数代提，利用Hash函数产生挑战，将身份识别协议转化为签名，数字签名本质上既是非交互式证明。

3.交互式证明与非交互式证明区别
交互式可以在更小的时间，更加有效的使验证者相信；非交互式证明可以解决交互式由于私钥泄露问题使得算法无法在公开的环境下使用的问题。

4.ElGamal加密
基于离散对数问题的非确定性加密算法，每次加密会使用一个随机数，加密相同的m，会产生不同的c。

![image](https://user-images.githubusercontent.com/105495105/181895382-8ea42c3e-a35c-415d-ac3b-e9dfc5e02fd8.png)

![image](https://user-images.githubusercontent.com/105495105/181896884-47529fbc-3e88-4e14-abed-0ec16bb949b1.png)


5.Hash函数
将任意长度的二进制串映射成固定长度的比特串，是单向函数，从哈希值不能反向推出原始数据，利用哈利函数的单向性，将消息m加入哈希函数，构造签名公开进行验证。

2.2 使用交互式零知识证明

![image](https://user-images.githubusercontent.com/105495105/181897063-b0023a46-304a-4bea-8423-29e46ac38313.png)

![image](https://user-images.githubusercontent.com/105495105/181897171-39cee10d-ba32-4d2e-a04a-082a08f8fe12.png)

![image](https://user-images.githubusercontent.com/105495105/181897292-eea7c1a9-56d2-4611-b075-06338ed41e08.png)

![image](https://user-images.githubusercontent.com/105495105/181897433-960eef17-bc5f-4ea5-b41e-c03c647879c0.png)




2.3转化为非交互式零知识证明

交互式零知识证明无法在公开验证的条件下进行验证，因为整个协议存在交互过程，此方案只对参与交互的验证者有效，其他不参与交互的验证者无法判断整个过程是否存在串通舞弊的行为，因为如果有两个验证者，他们相互交换自己得到的值，便可以推出私钥，因此交互式零知识证明是无法公开验证的，非交互零知识证明方案可以避免公开环境下验证私钥泄露问题。

![image](https://user-images.githubusercontent.com/105495105/181897835-99768484-4e0b-46d3-bca4-c66a829ff84d.png)

![image](https://user-images.githubusercontent.com/105495105/181897986-564a8310-908f-4410-bc1d-dffcc3698f7d.png)


