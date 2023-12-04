raw_massage = input("请输入原文：")
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "a", "b"]
raw_massage_list = list(raw_massage)
pwd = []  # 为保证重复字符也得以加密

for letter in raw_massage_list:  # 运行加密算法
    if letter.isalpha():
        if letter.isupper():  # 处理大写字母无法加密问题
            letter_lower = letter.lower()
            index_rml = raw_massage_list.index(letter)
            index_alphabet = alphabet.index(letter_lower)
            pwd_index = index_alphabet + 2  # 使用索引位移实现字符位移
            pwd_letter = alphabet[pwd_index].upper()
            raw_massage_list[index_rml] = pwd_letter
        else:
            index_rml = raw_massage_list.index(letter)
            index_alphabet = alphabet.index(letter)
            pwd_index = index_alphabet + 2
            pwd_letter = alphabet[pwd_index]
            raw_massage_list[index_rml] = pwd_letter
        pwd.append(pwd_letter)
    else:
        pwd.append(letter)

print("加密后的密文：", end="")
for letter in pwd:
    print(letter, end="")

input("\n---请键入 Enter 键退出---")
