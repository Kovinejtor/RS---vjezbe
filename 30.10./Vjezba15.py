def count_vowels_consonants(tekst):
    vowelsCount = 0
    consonantsCount = 0

    for x in tekst:
        if x in vowels:
            vowelsCount+=1
        elif x in consonants:
            consonantsCount+=1
    
    return {'vowels': vowelsCount, 'consonants': consonantsCount}

vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(count_vowels_consonants(tekst))
# {'vowels': 30, 'consonants': 48}
