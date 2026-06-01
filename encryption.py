
class Encrypter:

    keys = []
    values = []
    dictionary = []
    def __init__(self, keys: list[str], values: list[str], dictionary: list[str]):
        self.keys = keys
        self.values = values
        self.dictionary = dictionary

    def encrypt(self, word1: str) -> str:
        result = ""
        for c in word1:
            if c not in self.keys:
                return ""
            result += self.values[self.keys.index(c)]

        return result

    def decrypt(self, word2: str) -> int:

        for i in range(round(len(word2)/2)):
            if word2[2*i:2*i+2] not in self.values:
                print("there is no possible decryption")
                return 0

        
        #print(len(self.dictionary))
        #print(len(list(set(self.dictionary))))
        if len(list(set(self.values))) == 1 and len(self.values) != 1:
            print("all the values are the same, any value in the dictionary with half the length of word2 is possible")
            return len([i for i in self.dictionary if len(word2) / 2 == len(i)])

        
        substrings = []
        for i in range(round(len(word2)/2)):
            if word2[2*i:2*i+2] not in self.values:
                return 0
            substrings.append((self.values[self.values.index(word2[2*i:2*i+2])]))
        possible_decrypts = [[] for i in substrings]
        for i, j in enumerate(substrings):
            substring_decrypts = []
            for index, value in enumerate(self.values):
                if value == j:
                    substring_decrypts.append(index)
            [possible_decrypts[i].append(self.keys[k]) for k in substring_decrypts]

        possible_full_decrypts = [i for i in possible_decrypts[0]]
        for i in possible_decrypts[1:]:
            temp = []#copy.deepcopy(possible_full_decrypts)
            possible_full_decrypts = list(set(possible_full_decrypts)) #remove duplicates

            for k in i:
                for j in possible_full_decrypts:
                    temp.append(j + k)
            possible_full_decrypts = copy.deepcopy(temp)
        print("normal decrypt")
        return len(set(possible_full_decrypts).intersection(set(self.dictionary)))
