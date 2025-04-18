# def fac(num):
#     result = 1
#     for n in range(1,num+1):
#         result *= n
#     return result
# m = int(input("m:"))
# n = int(input("n:"))
# print(fac(m)//fac(n)//fac(m-n))

# import random
# import string

# ALL_CHARS = string.digits + string.ascii_letters

# def generate_random_code(*,code_len=4):
#     return ''.join(random.choices(ALL_CHARS,k=code_len))
# for _ in range(5):
#     print(generate_random_code())
def is_prime(num:int)->bool:
    for i in range(2,num):
        if num % i == 0:
            return False
    else:
        return True
m = int(input('请输入一个整数，我可以帮你判断它是否是一个质数：'))
if is_prime(m):
    print(f'{m}是质数')
else:
    print(f'{m}不是质数')
