import csv
from collections import Counter


# Functie pentru citirea cuvintelor din fișierul csv
# Am utilizat codificare UTF-8 deoarece folosește pentru codificarea caracterelor un octet (caracterele ASCII) până la 4 octeți.
# Diacriticele românești sunt codificate în UTF-8 pe 2 sau 3 octeți.
def citeste_fisier(doccsv):
    pereche_cuvinte = []
    with open(doccsv, newline='', encoding='utf-8') as fisiercsv:
        citeste_cuvant = csv.reader(fisiercsv, delimiter=';')
        for linie in citeste_cuvant:
            if len(linie) == 3:
                pereche_cuvinte.append((linie[1].upper(), linie[2].upper()))  # sir partial si cuvant complet
    return pereche_cuvinte


# Functie care calculeaza frecventa literelor din lista de cuvinte ramase
def frecventa_litere(cuvinte):
    contor_litere = Counter()
    for cuvant in cuvinte:
        litere_unice = set(cuvant)  # Calculăm frecvența literelor unice din fiecare cuvânt
        contor_litere.update(litere_unice)
    return contor_litere


# Functie care ghicește automat literele si returneaza numarul de incercari
def joc_automat_hangman(cuvant_partial, cuvant_complet, max_greseli=7):
    gresit = 0
    utilizate = []
    ghicit_partial = list(cuvant_partial)  # Cuvant ghicit partial
    incercari = 0

    while gresit < max_greseli and ''.join(ghicit_partial) != cuvant_complet:
        # Calculeaza frecventa literelor din cuvantul complet care nu au fost incă ghicite
        litere_ramase = [l for l in cuvant_complet if l not in utilizate]
        if not litere_ramase:
            break
        # Ghicim litera cu cea mai mare frecventa
        max_frecventa_litera = frecventa_litere([litere_ramase])
        ghicit = max_frecventa_litera.most_common(1)[0][0]

        utilizate.append(ghicit)
        incercari += 1

        if ghicit in cuvant_complet:
            # Inlocuim '*' cu litera ghicita corect
            for i in range(len(cuvant_complet)):
                if cuvant_complet[i] == ghicit:
                    ghicit_partial[i] = ghicit
        else:
            gresit += 1

    return incercari, (''.join(ghicit_partial) == cuvant_complet)


# Functia principala care ruleaza Hangman pentru toate cuvintele din CSV si returneaza numarul total de incercari
def rulare_hangman_csv(fisier):
    pereche_cuvinte = citeste_fisier(fisier)
    total_incercari = 0
    total_cuvinte_ghicite = 0

    for cuvant_partial, cuvant_complet in pereche_cuvinte:
        incercari, ghicit = joc_automat_hangman(cuvant_partial, cuvant_complet)
        total_incercari += incercari
        if ghicit:
            total_cuvinte_ghicite += 1
            print(f"Cuvant ghicit: {cuvant_complet} | Incercari: {incercari}")
        else:
            print(f"Nu a fost ghicit: {cuvant_complet} | Incercari: {incercari}")
        if total_incercari > 1200:
            break  # Oprim daca depasim 1200 de incercari

    return total_incercari, total_cuvinte_ghicite, len(pereche_cuvinte)


# Apelam functia pentru fisierul CSV dat si afisam totalul incercarilor si numarul de cuvinte ghicite
total_incercari, total_cuvinte_ghicite, total_cuvinte = rulare_hangman_csv('cuvinte_de_verificat1.csv')

if total_incercari <= 1200:
    print(f"Numarul total de incercari: {total_incercari}")
    print(f"Numarul total de cuvinte ghicite: {total_cuvinte_ghicite} din {total_cuvinte}")
else:
    print(f"Numarul total de incercari depaseste 1200. Total incercari: {total_cuvinte}")
    print(f"Numarul total de cuvinte ghicite: {total_cuvinte_ghicite} din {total_cuvinte}")
