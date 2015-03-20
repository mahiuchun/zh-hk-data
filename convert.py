import codecs
import json

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
        in_big5 = (int(fields[3]) != 0)
        in_hkscs = (int(fields[4]) != 0)
        cj3 = fields[11].split(',')
        cj5 = fields[12].split(',')
        order = int(fields[14])
        if not (is_chinese and (in_big5 or in_hkscs)):
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
    chinese_to_cangjie3_json = json.dumps(chinese_to_cangjie3, ensure_ascii=False)
    chinese_to_cangjie5_json = json.dumps(chinese_to_cangjie5, ensure_ascii=False)
    codecs.open('chinese_to_cangjie3.js', 'w', encoding='utf8').write('var chinese_to_cangjie3='+chinese_to_cangjie3_json+'\n')
    codecs.open('chinese_to_cangjie5.js', 'w', encoding='utf8').write('var chinese_to_cangjie5='+chinese_to_cangjie5_json+'\n')

def main():
    do_cangjie()

if __name__ == '__main__':
    main()