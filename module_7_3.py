from pprint import pprint
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for punctuation in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(punctuation, '')
                text = text.split()
                all_words[file_name] = text
        return all_words

    def find(self, word):
        self.word = str(word)
        word = word.lower()
        dict_ = {}
        for key, all_words in self.get_all_words().items():
            if word in all_words:
                dict_[key] = all_words.index(word) + 1
        return dict_

    def count(self, word):
        self.word = str(word)
        word = word.lower()
        dict_ = {}
        for key, all_words in self.get_all_words().items():
            if word in all_words:
                dict_[key] = all_words.count(word)
        return dict_

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
