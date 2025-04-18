# f = float(input("请输入华氏温度："))
# c = (f - 32) / 1.8
# # print("%.1f华氏度 = %.1f摄氏度" % (f, c))
# print(f'{f:.1f}华氏度={c:.1f}摄氏度')

# year = int(input('请输入年份：'))
# is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
# # print(is_leap)
# print('%d是闰年' % year if is_leap else '%d不是闰年' % year)

# heigth = float(input('请输入身高(cm)：'))
# weight = float(input('请输入体重(kg)：'))
# bmi = weight / (heigth / 100) ** 2
# print(f'BMI指数为:{bmi:.1f}')
# if bmi < 18.5:
#     print('过轻')
# elif bmi >= 18.5 and bmi < 25:
#     print('正常')
# elif bmi > 27:
#     print('肥胖')

# x = float(input('请输入一个实数:'))
# match x :
#     case x if x > 1:
#         y = 3* x - 5
#     case x if x < -1:
#         y = 5 * x + 3
#     case _:
#         y = x + 2
# print(f'y={y:.1f}')

# for num in range(100,1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(num)

# import random
# money = 1000
# while money > 0:
#     print(f'你的剩余资产为：{money}元\n')
#     while True:
#         debt = int(input('请下注：'))
#         if 0 < debt <= money:
#             break
#         elif debt > money:
#             print(f'您的剩余财产不足，请重新下注！')
#     firstpoint = random.randrange(1,7) + random.randrange(1,7)
#     if firstpoint == 7 or firstpoint == 12:
#         print(f'第一轮投掷骰子的结果为：{firstpoint}点，玩家获胜\n')
#         money += debt
#     elif firstpoint == 2 or firstpoint == 3 or firstpoint == 12:
#         print(f'第一轮投掷骰子的结果为：{firstpoint}点，庄家获胜\n')
#         money -= debt
#     else:
#         print(f'第一轮投掷骰子的结果为：{firstpoint}点，未分胜负，进入第二轮')
#         while True:
#             currentpoint = random.randrange(1,7) + random.randrange(1,7)
#             if currentpoint == firstpoint:
#                 print(f'第二轮投掷骰子的结果为：{currentpoint}点，玩家获胜\n')
#                 money += debt
#                 break
#             elif currentpoint == 7:
#                 print(f'第二轮投掷骰子的结果为：{currentpoint}点，庄家获胜\n')
#                 money -= debt
#                 break
# print('你破产了，游戏结束！')

# items1 = [35, 12, 99, 68, 55, 35, 87]
# print(type(items1))

# import random
# counters = [0] * 6
# for _ in range(6000):
#     face = random.randrange(1,7)
#     counters[face - 1] += 1
# for face in range(1,7):
#     print(f'点数{face}出现了{counters[face - 1]}次')

# languages = ['Python', 'Java', 'SQL', 'Java', 'C++', 'Java', 'JavaScript']
# if 'Java' in languages:
#     languages.remove('Java')
# print(languages)

# scores = []
# for _ in range(5):
#     temp = []
#     for _ in range(3):
#         score = int(input('请输入: '))
#         temp.append(score)
#     scores.append(temp)
# print(scores)

# a, b, *c = range(1, 10)
# print(a, b, c)
# a, b, c = [1, 10, 100]
# print(a, b, c)
# a, *b, c = 'hello'
# print(a, b, c)

# s1 = '\it \is \time \to \read \now'
# s2 = r'\it \is \time \to \read \now'
# print(f's1={s1}')
# print(f's2={s2}')

# xinhua = {
#     '麓': '山脚下',
#     '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
#     '蕗': '甘草的别名',
#     '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
# }
# print(xinhua)
# person = {
#     'name': '王大锤',
#     'age': 55,
#     'height': 168,
#     'weight': 60,
#     'addr': '成都市武侯区科华北路62号1栋101', 
#     'tel': '13122334455',
#     'emergence contact': '13800998877'
# }
# print(person)

def fac(num):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result
m = int(input('m = '))
n = int(input('n = '))
# 计算阶乘的时候不需要写重复的代码而是直接调用函数
# 调用函数的语法是在函数名后面跟上圆括号并传入参数
print(fac(m) // fac(n) // fac(m - n))
