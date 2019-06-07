from xpinyin import Pinyin
from lyricsgenius import Genius
import re


def import_pinyin_dictionary():
    dict_file = open('pinyin.dat', 'r', encoding='UTF-8')
    pinyin_dictionary = {}
    for line in dict_file:
        pair = [line[0], line[line.find(' '):line.find('|')]]
        pinyin_dictionary.update({pair[0]: pair[1]})
    dict_file.close()
    return pinyin_dictionary


def isolate_final(pinyin):
    final = ''
    reg = re.compile("(([aeiou:])+(([ngr])?)+\d)")
    if reg.search(pinyin):
        final = reg.search(pinyin)[0]
    return final


def get_pinyin(text):
    final = isolate_final(text)
    if final:

        i_accents = ['ī', 'í', 'ǐ', 'ì', 'i']
        a_accents = ['ā',  'á', 'ǎ', 'à', 'a']
        e_accents = ['ē', 'é', 'ě', 'è', 'e']
        o_accents = ['ō', 'ó', 'ǒ', 'ò', 'o']
        u_accents = ['ū', 'ú', 'ǔ', 'ù', 'u']
        um_accents = ['ǖ', 'ǘ', 'ǚ', 'ǜ', 'ü']
        pinyin = ''
        regs = [re.compile('(ao)|(an)|(ua)|(ai)|(ia)|(a+\d)'), re.compile('(i+\d)|(io)|(in)|(ui)'),
                re.compile('(ie)|(en)|(ue)|(er)|(e+\d)'), re.compile('(ou)|(uo)|(ong)|(o+\d)'), re.compile('(iu)|(un)|(u+\d)'),
                re.compile('(u:)')]

        if regs[0].search(final):
            a = final.find('a')
            pinyin = text[:text.find(final)] + a_accents[int(final[-1]) - 1] + text[a + 3:-1]


        elif regs[1].search(final):
            i = final.find('i')
            pinyin = text[:text.find(final)] + i_accents[int(final[-1]) - 1] + text[i + 3:-1]

        elif regs[3].search(final):
            o = final.find('o')
            pinyin = text[:text.find(final)] + o_accents[int(final[-1]) - 1] + text[o + 3:-1]

        elif regs[2].search(final):
            e = final.find('e')
            pinyin = text[:text.find(final)] + e_accents[int(final[-1]) - 1] + text[e + 3:-1]

        elif regs[4].search(final):
            u = final.find('u')
            pinyin = text[:text.find(final)] + u_accents[int(final[-1]) - 1] + text[u + 3:-1]

        elif regs[5].search(final):
            um = final.find('u:')
            pinyin = text[:text.find(final)] + um_accents[int(final[-1]) - 1] + text[um + 3:-1]

    else:
        pinyin = text

    return pinyin


def block_pinyin(block, pydic):
    pinyin = ''
    py = ''
    pointer = 0
    for char in block:

        print('context: ' + block[pointer-10:pointer])
        if char in pydic:
            py = get_pinyin(pydic[char])
            print('char: ' + char)
        else:
            py = char
        pinyin += py
        print('char: ' + py)
        pointer += 1

    return pinyin


def cleanup(text):
    clean = "\n"
    for char in text:
        if clean[-1] != '\n' and clean[-1] != ' ':
            clean += char
        else:
            if char != " ":
                clean += char
        if clean[-1] == '\n':
            clean += '\n'
    return clean


def main():
    genius = Genius("e8jTVBsM9j2r8nRML0tNY_7IOSUdBxxKJ7SG9x08gzPWNg18vRCH3CmckzfFDPv2")
    genius.excluded_terms = ['(How to pronounce)']
    genius.remove_section_headers = True
    genius.skip_non_songs = True
    # pinyin = Pinyin()

    song_info = [input("Enter the song name\n"),
                 input("Enter the artist name (recommended, leave blank if you don't know)\n")]
    song = genius.search_song(song_info[0], song_info[1])
    lyrics = song.lyrics

    edict = import_pinyin_dictionary()
    pinyin_lyrics = block_pinyin(lyrics, edict)
    pinyin_lyrics = cleanup(pinyin_lyrics)
    print(pinyin_lyrics)

    outfile_path = "C:\\Users\\Declan\\Desktop\\" + song.title + ', ' + song.artist + '-Pinyin.txt'
    outfile = open(outfile_path, 'w', encoding='utf-8')
    outfile.write(pinyin_lyrics)
    outfile.close()

# main()
edict = import_pinyin_dictionary()
print('%' + get_pinyin(edict['的']) + '!')
print((edict['的']))
print(get_pinyin('xiong4'))