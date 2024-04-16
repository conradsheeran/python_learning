def lower_strs_list(str_list):
    strs = eval(str_list)
    lower_strs = []
    for letter in strs:
        lower_letter = letter.lower()
        lower_strs.append(lower_letter)
    return lower_strs


def premix(raw):
    raw = lower_strs_list(eval(input("请输入待处理字符列表：")))
    premix_letter = ''
    strs_lens = len(raw)
    min_len = min(len(_) for _ in raw)
    for _ in range(strs_lens):
        strs = raw[_]
        for num in range(min_len):
            letter

