mbti_dict = {
            "INTJ": "The Mastermind",
            "INTP": "The Thinker",
            "Estp": "The Enterpreneur",
            }
word = input('Masukkan kata gaul: ')
if word.upper() in mbti_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print(mbti_dict[word.upper()])
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print('Error!')
