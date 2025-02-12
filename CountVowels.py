class CountVowels:
    def __init__(self):
        print("----------Count Vowels and Consonant in Your String----------")
        # self.string = "SehAubhiamauuu"
        self.string = input("Enter your String: ")
        self.countVowel()

    def countVowel(Self):
        vowel = "aeiou"
        count_a = 0
        count_e = 0
        count_i = 0
        count_o = 0
        count_u = 0
        count_consonant = 0
        count_vowel = 0
        text = Self.string.lower().strip().split()
        result = ''.join(text)
        # for i in Self.string.strip().lower():
        for i in result:
            if i in 'a':
                count_a += 1
            if i in 'e':
                count_e += 1
            if i in 'i':
                count_i += 1
            if i in 'o':
                count_o += 1
            if i in 'u':
                count_u += 1
            if i in vowel:
                count_vowel += 1
            else:
                count_consonant += 1
        header = "-" *50
        print(header)
        print(f"Total {count_vowel} Vowels Present in your string.")
        print(header)
        print(f"Vowel A Present {count_a} times in your string.")
        print(f"Vowel E Present {count_e} times in your string.")
        print(f"Vowel I Present {count_i} times in your string.")
        print(f"Vowel O Present {count_o} times in your string.")
        print(f"Vowel U Present {count_u} times in your string.")
        print(header)
        print(f"Total {count_consonant} Consonants Present in your string.")
        print(header)

obj = CountVowels()