import codecs
import json
import sys

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
            for vari in fields[2:]:
                cp = int('0x'+vari[2:], 16)
                if cp > sys.maxunicode:
                    continue
                trad = unichr(cp)
                if ch not in chinese_to_traditional:
                    chinese_to_traditional[ch] = list()
                chinese_to_traditional[ch].append(trad)
        elif fields[1] == 'kSimplifiedVariant':
            for vari in fields[2:]:
                cp = int('0x'+vari[2:], 16)
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
    do_variants()

if __name__ == '__main__':
    main()
