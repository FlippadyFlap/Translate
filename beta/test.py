from google.cloud import translate
from xpinyin import Pinyin

translate_client = translate.Client()
pinyin = Pinyin()

text = input("Enter English Text:\n")
target = 'zh'
translation = translate_client.translate(text, target_language=target)
translation = u'{}'.format(translation['translatedText'])

pinyin_text = pinyin.get_pinyin(chars=translation, splitter=' ', tone_marks="marks")
print(pinyin_text)


# import lyricsgenius
# genius = lyricsgenius.Genius("e8jTVBsM9j2r8nRML0tNY_7IOSUdBxxKJ7SG9x08gzPWNg18vRCH3CmckzfFDPv2")
# artist = genius.search_artist('higher brothers')
# print(artist)

