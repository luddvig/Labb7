import csv
from PokeClassFile import Pokemon
from hashtable import Hashtable


def pokes_fran_fil(fil):
    with open(fil, "r") as file:
        alla_pokes = csv.reader(file)       # Läser in itererbar fil
        next(alla_pokes)
        alla_pokes_list = list(alla_pokes)
        poke_hash = Hashtable(len(alla_pokes_list)*2)                  # Skapar DictHash objekt för att lägga in pokes
        for row in alla_pokes_list:
            pokeobjekt = Pokemon(row[0], row[1], row[2], row[3], row[4], row[5],
                                 row[6], row[7], row[8], row[9], row[10], row[11], row[12])     # Pokeobjekt som data
            pokenamn = row[1]               # Pokenamn som nyckel
            poke_hash.store(pokenamn, pokeobjekt)   # Lägger in i DictHash
    return poke_hash


def main():
    fil = "pokemon.csv"
    testpoke = pokes_fran_fil(fil)
    print(testpoke.search("Caterpie"))      # Ska finnas
    print(testpoke.search("Alakazam"))      # Ska finnas
    print(testpoke.search("Donphan"))       # Ska finnas
    print(testpoke.search("Bulbasaur"))     # Ska finnas
    print(testpoke.search("FakePoke"))      # Ska inte finnas, ge KeyError


if __name__ == '__main__':
    main()