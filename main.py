def counter(text_1):
    words = text_1.split(' ')
    for k in range(0, len(words)):
        words[k] = "".join(words[k])
    return words

def deleted():
    words = counter(text)
    bool_f = 0
    text_r = ' '
    for i in range(0, len(words)):
        c = 0
        for j in range(0, len(words)):
            if words[i] == words[j]:
                c += 1
                bool_f = j
            if (c > 2) & (j == (len(words) - 1)):
                current = words[bool_f]
                text_r = text.replace(current,' ')
    return text_r

def format():
    text_r = deleted()
    for i in range(0, len(text_r)):
        text_r = text_r.replace('  ', ' ')
    return text_r

text = input("Введите строчку:")
text_r_1 = format()
print("Измененная строчка:", text_r_1)