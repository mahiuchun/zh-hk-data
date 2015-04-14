import codecs
import json
import sys

def do_cangjie():
    chinese_to_cangjie = dict()
    cangjie_to_chinese = dict()
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
        is_big5 = (int(fields[3]) != 0)
        is_hkscs = (int(fields[4]) != 0)
        cj3 = fields[11].split(',')
        cj5 = fields[12].split(',')
        if not is_chinese:
            continue
        if (not is_big5) and (not is_hkscs):
            continue
        chinese_to_cangjie[ch] = list()
        if cj5[0] != 'NA':
            for cj in cj5:
                # forward mapping
                chinese_to_cangjie[ch].append(cj)
                # inverse mapping
                if cj not in cangjie_to_chinese:
                    cangjie_to_chinese[cj] = list()
                if ch not in cangjie_to_chinese[cj]:
                    cangjie_to_chinese[cj].append(ch)
        if cj3[0] != 'NA':
            for cj in cj3:
                # forward mapping
                if cj in chinese_to_cangjie[ch]:
                    continue
                chinese_to_cangjie[ch].append(cj)
                # inverse mapping
                if cj not in cangjie_to_chinese:
                    cangjie_to_chinese[cj] = list()
                if ch not in cangjie_to_chinese[cj]:
                    cangjie_to_chinese[cj].append(ch)
        if len(chinese_to_cangjie[ch]) == 0:
            del chinese_to_cangjie[ch]
    h.close()
    chinese_to_cangjie_json = json.dumps(chinese_to_cangjie, ensure_ascii=False, sort_keys=True)
    codecs.open('chinese_to_cangjie.js', 'w', encoding='utf8').write('var chinese_to_cangjie='+chinese_to_cangjie_json+'\n')
    cangjie_to_chinese_json = json.dumps(cangjie_to_chinese, ensure_ascii=False, sort_keys=True)
    codecs.open('cangjie.js', 'w', encoding='utf8').write('var cangjie='+cangjie_to_chinese_json+'\n')

def main():
    do_cangjie()

if __name__ == '__main__':
    main()
