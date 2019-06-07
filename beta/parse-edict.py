def seek_char(dictionary, char):
    indices = []
    start = 0
    while True:
        if indices:
            start = indices[-1]+1
        if dictionary.find(char, start) == -1:
            break
        index = dictionary.find(char, start)
        indices.append(index)
        if not(dictionary[indices[-1]] == char):
            print(index)
            print(dictionary[index])

    return indices


def isolate_line(dictionary, idx):

    line_start = dictionary.rfind('\n', 0, idx)
    line_end = dictionary.find('\n', idx)
    line = dictionary[line_start:line_end]

    start_char = line.find(' ') + 1
    end_char = line[start_char:].find(' ') + start_char

    if line.find(dictionary[idx]) == -1 or line[start_char:end_char].find(dictionary[idx]):
        line = ''
    return line


def line_processing(line, char):
    start_char = line.find(' ') + 1
    end_char = line[start_char:].find(' ')+start_char
    char_list = line[start_char:end_char]

    py_start = line.find('[') + 1
    py_end = line[py_start:].find(']')+py_start
    pinyin_list = line[py_start:py_end]
    pinyin_list = pinyin_list.split(' ')
    index = char_list.find(char)

    return char_list[index], pinyin_list[index]


def pre_processing(dictionary):
    clean = ''
    dirty = dictionary.split('\n')

    for line in dirty:
        if line[0] != '#':
            clean += line[0:line.find('/')]+'\n'
    return clean


def unique_pronunciations(assoc_pairs):
    pron_list = []
    for pair in assoc_pairs[1]:
        if not(pair.lower() in pron_list) and pair != 'xx5':
            pron_list.append(pair.lower())

    weighted_pronunciations = [[], []]
    for candidate in pron_list:
        weighted_pronunciations[0].append(candidate)
        weighted_pronunciations[1].append(assoc_pairs[1].count(candidate))

    return weighted_pronunciations


def build_weighted_string(assoc_pairs):
    weighted_string = ''
    for i in range(0, len(assoc_pairs[0])):
        idx = (assoc_pairs[1].index(max(assoc_pairs[1])))
        weighted_string += assoc_pairs[0][idx]+'|'
        del assoc_pairs[1][idx]
        del assoc_pairs[0][idx]

    return weighted_string[:-1] + '\n'


def build_dict(dictionary):
    pydic = ""
    for i in range(int('0x4E00', 0), int('0x9FEF', 0)):
        index_list = seek_char(dictionary, chr(i))
        pairs = [[], []]
        for idx in index_list:
            isoline = (isolate_line(dictionary, idx))
            if isoline:
                processed_line = line_processing(isoline, chr(i))
                pairs[0].append(processed_line[0])
                pairs[1].append(processed_line[1].lower())
        pinyin_pairs = unique_pronunciations(pairs)
        w_string = build_weighted_string(pinyin_pairs)
        if w_string != '\n':
            pydic += chr(i) + ' ' + w_string
    return pydic[:-1]


eDictFile = open('cedict_ts.u8', 'r', encoding='UTF-8')
eDict = eDictFile.read()
eDictFile.close()
print('File Opened')


eDict = pre_processing(eDict)
print('PreProcessing done')
newDict = (build_dict(eDict))
print('Dictionary built')

outfile = open('pinyin.dat', 'w', encoding='UTF-8')
outfile.write(newDict)
outfile.close()
print('File Saved')
