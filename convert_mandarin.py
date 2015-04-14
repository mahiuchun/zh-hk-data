import codecs
import json
import sys

def do_mandrain():
    chinese_to_mandarin = dict()
    h = codecs.open('Unihan_Readings.txt', 'r', encoding='utf8')
    for line in h:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        fields = line.split()
        if fields[1] != 'kMandarin':
            continue
        cp = int('0x'+fields[0][2:], 16)
        if cp > sys.maxunicode:
            continue
        ch = unichr(cp)
        if ch not in chinese_to_mandarin:
            chinese_to_mandarin[ch] = list()
        for read in fields[2:]:
            chinese_to_mandarin[ch].append(read)
    h.close()
    chinese_to_mandarin_json = json.dumps(chinese_to_mandarin, ensure_ascii=False, sort_keys=True)
    codecs.open('chinese_to_mandarin.js', 'w', encoding='utf8').write('var chinese_to_mandarin='+chinese_to_mandarin_json+'\n')

def main():
    do_mandrain()

if __name__ == '__main__':
    main()
