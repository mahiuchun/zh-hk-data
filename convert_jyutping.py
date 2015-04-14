import codecs
import json
import sys

def do_jyutping():
    chinese_to_jyutping = json.loads(codecs.open('cantonese-syllables-characters.json', encoding='utf8').read())
    chinese_to_jyutping_json = json.dumps(chinese_to_jyutping, ensure_ascii=False, sort_keys=True)
    codecs.open('chinese_to_jyutping.js', 'w', encoding='utf8').write('var chinese_to_jyutping='+chinese_to_jyutping_json+'\n')

def main():
    do_jyutping()

if __name__ == '__main__':
    main()
