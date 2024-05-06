import math

a = eval(input("请输入系数a："))
b = eval(input("请输入系数b："))
c = eval(input("请输入系数c："))

if b ** 2 - 4 * a * c < 0:  # 判断该方程是否有实数根
    print(f"{a}x^2+{b}y+{c}=0 该方程无实数根")
elif b ** 2 - 4 * a * c == 0:  # 判断是否只有一个实数根
    x0 = (-b + math.pow(b ** 2 - 4 * a * c, 1/2)) / (2 * a)
    if x0 - math.trunc(x0) == 0:  # 判断实数根是浮点数还是整数
        x0 = int(x0)
        print(f"{a}x^2+{b}y+{c}=0 该方程有一实数根{x0}")  # 格式化输出
    else:
        x0 = round(x0, 2)
        print(f"{a}x^2+{b}y+{c}=0 该方程有一实数根{x0}")
else:
    x1 = (-b + math.pow(b ** 2 - 4 * a * c, 1/2)) / (2 * a)
    x2 = (-b - math.pow(b ** 2 - 4 * a * c, 1/2)) / (2 * a)
    if (x1 - math.trunc(x1) == 0) and (x2 - math.trunc(x2) == 0):
        x1 = int(x1)
        x2 = int(x2)
        print(f"{a}x^2+{b}y+{c}=0 该方程有两个实数根，分别为{x1}, {x2}")
    elif (x1 - math.trunc(x1) != 0) and (x2 - math.trunc(x2) != 0):
        x1 = round(x1, 2)
        x2 = round(x2, 2)
        print(f"{a}x^2+{b}y+{c}=0 该方程有两个实数根，分别为{x1}, {x2}")
    else:
        if x1 - math.trunc(x1) != 0:
            x1 = round(x1, 2)
            x2 = int(x2)
            print(f"{a}x^2+{b}y+{c}=0 该方程有两个实数根，分别为{x1}, {x2}")
        else:
            x1 = int(x1)
            x2 = round(x2, 2)
            print(f"{a}x^2+{b}y+{c}=0 该方程有两个实数根，分别为{x1}, {x2}")

input("---请输入 Enter 键退出---")
