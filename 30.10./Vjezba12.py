def obrni_rjecnik(rjecnik):
    reversedDict = dict(zip(rjecnik.values(), rjecnik.keys()))
    return reversedDict

rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
print(obrni_rjecnik(rjecnik))
# {'Ivan': 'ime', 'Ivić': 'prezime', 25: 'dob'}
