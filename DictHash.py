import csv
from PokeClassFile import Pokemon


class DictHash:

    def __init__(self):
        self.dictionary = dict()

    def store(self, nyckel, data):
        self.dictionary[nyckel] = data

    def search(self, nyckel):
        try:
            return self.dictionary[nyckel]
        except KeyError:                        # Om man söker för nyckel som inte finns
            return "Nyckel finns ej"

    def __getitem__(self, nyckel):
        return self.dictionary[nyckel]

    def __contains__(self, nyckel):
        return nyckel in self.dictionary.keys()

    def alla(self):
        return [i for i in self.dictionary]

    def __str__(self):
        for i in self.alla():
            print(self.dictionary[i])
        return "**End**"


def pokes_fran_fil(fil):
    with open(fil, "r") as file:
        alla_pokes = csv.reader(file)       # Läser in itererbar fil
        pokes = DictHash()                  # Skapar DictHash objekt för att lägga in pokes
        next(alla_pokes)
        for row in alla_pokes:
            pokenamn = row[1]               # Pokenamn som nyckel
            pokeobjekt = Pokemon(row[0], row[1], row[2], row[3], row[4], row[5],
                                 row[6], row[7], row[8], row[9], row[10], row[11], row[12])     # Pokeobjekt som data
            pokes.store(pokenamn, pokeobjekt)   # Lägger in i DictHash
    return pokes


def main():
    fil = "pokemon.csv"
    x = pokes_fran_fil(fil)
    print(x.search("Caterpie"))  # Ska hittas
    print(x.search("PokeSomInteFinns"))  # Ska inte hittas


if __name__ == '__main__':
    main()





