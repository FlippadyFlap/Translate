from xpinyin import Pinyin

def split_by_type(line):
    line_list = []
    outer_word = ''
    for char in line:
        if pinyin.get_pinyin(char) == char:
            outer_word += char
        else:
            if len(outer_word) > 0:
                line_list.append(outer_word)
                outer_word = ''
            line_list.append(char)
    return line_list





pinyin=Pinyin()

in_file = open('elin-text.txt', 'r', encoding='UTF-8')

elin_text = in_file.readlines()

new_text = ''

for line in elin_text:
    words = split_by_type(line)
    while len(words) > 0:
        temp_ch = ''
        temp_py = ''
        while len(temp_py) < 90 and words:
            temp_py += pinyin.get_pinyin(words[0], tone_marks='marks') + ' '
            temp_ch += words[0]
            words = words[1:]
        new_text += temp_py + '\n' + temp_ch + '\n' + '\n'


print(new_text)