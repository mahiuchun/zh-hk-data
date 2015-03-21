import codecs
import json
import sys

def do_cangjie():
    chinese_to_cangjie3 = dict()
    chinese_to_cangjie5 = dict()
    h = codecs.open('libcangjie-table.txt', 'r', encoding='utf8')
    for line in h:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        fields = line.split()
        if len(fields) != 15:
            continue
        ch = fields[0]
        is_chinese = (int(fields[2]) != 0)
        cj3 = fields[11].split(',')
        cj5 = fields[12].split(',')
        if not is_chinese:
            continue
        if cj3[0] != 'NA':
            chinese_to_cangjie3[ch] = list()
            for cj in cj3:
                chinese_to_cangjie3[ch].append(cj)
        if cj5[0] != 'NA':
            chinese_to_cangjie5[ch] = list()
            for cj in cj5:
                chinese_to_cangjie5[ch].append(cj)
    h.close()
    chinese_to_cangjie3_json = json.dumps(chinese_to_cangjie3, ensure_ascii=False, sort_keys=True)
    chinese_to_cangjie5_json = json.dumps(chinese_to_cangjie5, ensure_ascii=False, sort_keys=True)
    codecs.open('chinese_to_cangjie3.js', 'w', encoding='utf8').write('var chinese_to_cangjie3='+chinese_to_cangjie3_json+'\n')
    codecs.open('chinese_to_cangjie5.js', 'w', encoding='utf8').write('var chinese_to_cangjie5='+chinese_to_cangjie5_json+'\n')

def do_jyutping():
    chinese_to_jyutping = json.loads(codecs.open('cantonese-syllables-characters.json', encoding='utf8').read())
    chinese_to_jyutping_json = json.dumps(chinese_to_jyutping, ensure_ascii=False, sort_keys=True)
    codecs.open('chinese_to_jyutping.js', 'w', encoding='utf8').write('var chinese_to_jyutping='+chinese_to_jyutping_json+'\n')

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
        mandarin = fields[2].split()
        chinese_to_mandarin[ch] = mandarin
    h.close()
    chinese_to_mandarin_json = json.dumps(chinese_to_mandarin, ensure_ascii=False, sort_keys=True)
    codecs.open('chinese_to_mandarin.js', 'w', encoding='utf8').write('var chinese_to_mandarin='+chinese_to_mandarin_json+'\n')

def do_variants():
    chinese_to_simplified  = dict()
    chinese_to_traditional = dict()
    h = codecs.open('Unihan_Variants.txt', 'r', encoding='utf8')
    for line in h:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        fields = line.split()
        cp = int('0x'+fields[0][2:], 16)
        if cp > sys.maxunicode:
            continue
        ch = unichr(cp)
        if fields[1] == 'kTraditionalVariant':
            cp = int('0x'+fields[2][2:], 16)
            if cp > sys.maxunicode:
                continue
            trad = unichr(cp)
            if ch not in chinese_to_traditional:
                chinese_to_traditional[ch] = list()
            chinese_to_traditional[ch].append(trad)
        elif fields[1] == 'kSimplifiedVariant':
            cp = int('0x'+fields[2][2:], 16)
            if cp > sys.maxunicode:
                continue
            simp = unichr(cp)
            if ch not in chinese_to_simplified:
                chinese_to_simplified[ch] = list()
            chinese_to_simplified[ch].append(simp)
        else:
            continue
    h.close()
    chinese_to_simplified_json  = json.dumps(chinese_to_simplified,  ensure_ascii=False, sort_keys=True)
    chinese_to_traditional_json = json.dumps(chinese_to_traditional, ensure_ascii=False, sort_keys=True)
    codecs.open('chinese_to_simplified.js',  'w', encoding='utf8').write('var chinese_to_simplified=' +chinese_to_simplified_json +'\n')
    codecs.open('chinese_to_traditional.js', 'w', encoding='utf8').write('var chinese_to_traditional='+chinese_to_traditional_json+'\n')

def main():
    do_cangjie()
    do_jyutping()
    do_mandrain()
    do_variants()

if __name__ == '__main__':
    main()
