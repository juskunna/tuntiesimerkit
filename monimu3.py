# esimerkki, lista dictionaryn sisällä
book = {
    "name":  "My Lady Jane",
    "year":  2016,
    "authors": ["Cynthia Hand", "Brodi Ashton", "Jodi Meadows"]
}
# tulostetaan eka nimi
print(book["authors"][0])
print()

for author in book['authors']:
    print(author)