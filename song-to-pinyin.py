from xpinyin import Pinyin
from lyricsgenius import Genius
import apikeys


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
    genius = Genius(apikeys.genius)
    genius.excluded_terms = ['(How to pronounce)']
    genius.remove_section_headers = True
    genius.skip_non_songs = True
    pinyin = Pinyin()

    song_info = [input("Enter the song name\n"),
                 input("Enter the artist name (recommended, leave blank if you don't know)\n")]
    song = genius.search_song(song_info[0], song_info[1])
    lyrics = song.lyrics

    pinyin_lyrics = pinyin.get_pinyin(lyrics, splitter=' ', tone_marks='marks')
    pinyin_lyrics = cleanup(pinyin_lyrics)
    print(pinyin_lyrics)

    outfile_path = "C:\\Users\\Declan\\Desktop\\" + song.title + ', ' + song.artist + '-Pinyin.txt'
    outfile = open(outfile_path, 'w', encoding='utf-8')
    outfile.write(pinyin_lyrics)
    outfile.close()

main()