import os
import csv
import trie

ST_DICT = "data/dict/s2t.txt"
TS_DICT = "data/dict/t2s.txt"
ST_PHRASE = "data/phrase/STPhrases.txt"
TS_PHRASE = "data/phrase/TSPhrases.txt"
IDIOM = "data/idiom"


class Converter:
    def __init__(self, init_str, np):
        self.init_str = init_str
        if init_str == "st":
            self.dict = self.get_dict(ST_DICT)
            self.phrase = self.get_phrase(ST_PHRASE)
        elif init_str == "ts":
            self.dict = self.get_dict(TS_DICT)
            self.phrase = self.get_phrase(TS_PHRASE)

        self.idiom = None
        if not np:
            self.idiom = self.get_idiom(IDIOM)

    def get_dict(self, dict_str):
        dict = {}
        d_path = os.path.join(dict_str)
        f = open(d_path)
        for line in csv.reader(f, dialect="excel-tab"):
            dict[line[0]] = line[1]
        return dict

    def get_phrase(self, phrase_str):
        p_path = os.path.join(phrase_str)
        f = open(p_path)
        t = trie.Trie()
        for line in csv.reader(f, dialect="excel-tab"):
            t.insert(line[0], line[1])
        return t

    def get_idiom(self, idiom_str):
        key = 0
        val = 1
        if self.init_str == "ts":
            key = 1
            val = 0

        t = trie.Trie()
        idioms = [fname for fname in os.listdir(idiom_str) if fname.endswith(".txt")]
        idioms.sort()
        for idiom in idioms:
            i_path = os.path.join(idiom_str, idiom)
            f = open(i_path)
            for line in csv.reader(f, dialect="excel-tab"):
                t.insert(line[key], line[val])
            f.close()
        return t

    def convert_idiom_ts(self, input):
        ilen = len(input)
        index = 0
        output = ""

        while index < ilen:
            char = input[index]
            if char not in self.dict:
                output += char
                index = index + 1
                continue
            tup = self.idiom.match(input, index)

            if tup[0] is None:
                output += self.dict[char]
                index = index + 1
            else:
                output += tup[0]
                index = tup[1]

        return output

    def convert_idiom_st(self, input):
        ilen = len(input)
        index = 0
        output = ""

        while index < ilen:
            tup = self.idiom.match(input, index)

            if tup[0] is None:
                output += input[index]
                index = index + 1
            else:
                output += tup[0]
                index = tup[1]

        return output

    def convert(self, input):
        if self.idiom is not None and self.init_str == "ts":
            input = self.convert_idiom_ts(input)

        ilen = len(input)
        index = 0
        output = ""
        while index < ilen:
            char = input[index]
            if char not in self.dict:
                output += char
                index = index + 1
                continue
            tup = self.phrase.match(input, index)

            if tup[0] is None:
                output += self.dict[char]
                index = index + 1
            else:
                output += tup[0]
                index = tup[1]

        if self.idiom is not None and self.init_str == "st":
            output = self.convert_idiom_st(output)

        return output
