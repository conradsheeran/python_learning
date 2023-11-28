line_1 = []  # 创建每一行的对应的列表
line_2 = []
line_3 = []

for _ in range(9):  # 从用户那里获得所需的 9 个数据
    number = eval(input("请依次输入 3*3 矩阵的数："))
    if len(line_1) < 3:  # 将这些数据分别存入到每行对应的列表中去
        line_1.append(number)
    elif len(line_2) < 3:
        line_2.append(number)
    elif len(line_3) < 3:
        line_3.append(number)
matrix_sum = line_1[0] + line_2[1] + line_3[2]
print(f"该矩阵对角线的和为{matrix_sum}")

input("---请输入 Enter 键退出---")
