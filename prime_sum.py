# 用户输入一个区间，求该区间所有素数和素数的个数

first_number = eval(input("请输入该区间的起始值："))  # 获取该区间
end_number = eval(input("请输入该区间的终止值："))
prime_list = []

for number in range(first_number, end_number + 1):
    for factor in range(2, number):  # 判定是否为素数
        if number % factor == 0:
            break
    else:  # 如果是素数就将其添加到素数列表中
        prime_list.append(number)


list_len = len(prime_list)  # 判定区间内是否无素数

if list_len == 0:
    print("该区间没有素数！")
else:
    print("该区间有以下素数：")
    for number in prime_list:
        print(number, end=" ")
    print("")
    print(f"共计{list_len}个")

input("---请键入 Enter 键退出---")
