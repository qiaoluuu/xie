
#数据类型的转换
# print(type("哈哈"))
# print(type(2333))
# print(type(2.333))
# print(type(True))
# print(type(()))   #元组
# print(type([]))   #数组
# print(type({}))  #字典


"""
print("你好")
a = input("请输入：")   #输入和赋值
b = input("请输入：")
print("input输入的内容是：",a+b)  #输出的是字符串



print("你好")
a = float(input("请输入："))   #输入和赋值
b = float(input("请输入："))
print("input输入的内容是：",a+b)    #结果
"""


#len()函数：计算字符串的长度
# a = input("请输入：")   #输入和赋值
# b = input("请输入：")
# print("input输入的内容是：",len(a+b))  #输出的是字符串



"""
练习
获取用户的个人信息，并且存放到字典中
个人信息包括name\age\sex
"""
name = input("请输入姓名：")
age = input("请输入年龄：")
sex = input("请输入性别：")
useriofo = {}
useriofo.update(name = name,age = age,sex = sex)
print(useriofo)