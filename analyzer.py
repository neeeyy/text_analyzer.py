def text_report(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        file_name = f.read()
        #print(f'qqq {file_name}')
        file_split = file_name.split()
        file_lines = file_name.splitlines()
        print(f'qqq {file_lines}')
        count_word = 0
        count_unique = 0
        result_unique = []
        result_word = []
        result_top = {}
        length_words = 0
        max_lengt_word = 0
        max_word = ''
        start_wish = set()
        contain_ir = set()
        count_offer = 0
        for char in file_name:
            if char in '?.!':
                count_offer += 1
        for i in file_split:
            clean = ''.join(char for char in i if char.isalpha())
            if not clean:
                continue
            clean = clean.lower()
            length_words += len(clean)
            if clean not in result_top:
                result_top[clean] = 1
            else:
                result_top[clean] += 1

            if max_lengt_word < (len(clean)):
                max_lengt_word = len(clean)
                max_word = clean
            if clean[:1] == 'п':
                start_wish.add(clean)
            if 'ир' in clean:
                contain_ir.add(clean)
            if clean != "":
                result_word.append(clean)
                result_unique.append(clean.lower())
            count_unique = len(set(result_unique))
            count_word = len(result_word)
        sort_re = sorted(result_top.items(), key=lambda x: x[1], reverse=True)
        return {
            'Всего слов': count_word,
            'Уникальных слов':  count_unique,
            'Топ-3 слова': sort_re[:3],
            'Средняя длина слова': length_words / count_word,
            'Самое длинное слово': max_word,
            'Cлова начинается на п': start_wish,
            'Слово содержит ир': contain_ir,
            'Количество предложение': count_offer
        }


report = text_report('text.txt')

with open('report.txt', 'w', encoding='utf-8') as f:
    for key, value in report.items():
        print(f"{key}: {value}")
        f.write(f"{key}: {value}\n")
