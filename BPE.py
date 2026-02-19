# Класс токенизатора
class BPE():
    def __init__(self, vocab_size):
        self.vocab_size = vocab_size # Сохраняем размер словаря как атрибут класса
        self.id2token = dict()
        self.token2id = dict()
        self.token_list = dict()

    # Преобразование строки текста в список идентификаторов токенов
    def fit(self, text):
        split_text = list(text)
        token_set = set(split_text)
        while len(token_set) < self.vocab_size:
            freq_dict = {}
            for i in range (0, len(split_text)-1):
                pair = (split_text[i], split_text[i+1])
                if pair in freq_dict:
                    freq_dict[pair] += 1
                else:
                    freq_dict[pair] = 1
            # Находим ключ с максимальным значением
            max_freq_key = max(freq_dict, key=freq_dict.get)
            #print(max_freq_key)
            token_set.add(max_freq_key[0]+max_freq_key[1])
            new_split_text = list()
            i = 0
            while i<len(split_text) - 1:
                pair = (split_text[i], split_text[i + 1])
                if max_freq_key == pair:
                    new_split_text.append(pair[0]+pair[1])
                    i+=1
                else:
                    new_split_text.append(split_text[i])
                i += 1
            split_text = new_split_text
        token_list = sorted(list(token_set))
        self.token_list = token_list
        self.id2token = {i:token for i, token in enumerate(token_list)}
        self.token2id = {token: i for i, token in enumerate(token_list)}

    def encode(self, text):
        split_text = list(text)
        encode_list = list()
        i = 0
        while i<len(split_text):
            token = split_text[i]
            idx = self.token2id.get(token)
            while self.token2id.get(token + split_text[i]) is not None:
                i += 1
                token += split_text[i]
                idx = self.token2id.get(token)
            encode_list.append(idx)
            i += 1
        return encode_list


#tokenizer = BPE(30)
#tokenizer.fit("Из кузова в кузов шла перегрузка арбузов. В грозу в грязи от груза арбузов развалился кузов.")

#tokenizer = BPE(31)
#tokenizer.fit("Однажды был случай в далёком Макао: макака коалу в какао макала, коала лениво какао лакала, макака макала, коала икала.")
#print(tokenizer.encode("Однажды был случай в далёком Макао: макака коалу в какао макала, коала лениво какао лакала, макака макала, коала икала."))





