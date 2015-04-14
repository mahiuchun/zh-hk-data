import codecs
import json
import sys

def do_cangjie():
    chinese_to_cangjie = dict()
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
        chinese_to_cangjie[ch] = list()
        if cj5[0] != 'NA':
            for cj in cj5:
                chinese_to_cangjie[ch].append(cj)
        if cj3[0] != 'NA':
            for cj in cj3:
                if cj in chinese_to_cangjie[ch]:
                    continue
                chinese_to_cangjie[ch].append(cj)
        if len(chinese_to_cangjie[ch]) == 0:
            del chinese_to_cangjie[ch]
    h.close()
    chinese_to_cangjie_json = json.dumps(chinese_to_cangjie, ensure_ascii=False, sort_keys=True)
    codecs.open('chinese_to_cangjie.js', 'w', encoding='utf8').write('var chinese_to_cangjie='+chinese_to_cangjie_json+'\n')

def main():
    do_cangjie()

if __name__ == '__main__':
    main()
