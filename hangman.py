import csv

def citeste_fisier(doccsv):
    pereche_cuvinte = []
    with open(doccsv, newline='', encoding='utf-8') as fisiercsv:
        citeste_cuvant = csv.reader(fisiercsv, delimiter=';')
        for linie in citeste_cuvant:
            if len(linie) == 3:
                pereche_cuvinte.append((linie[1].upper(), linie[2].upper()))
    return pereche_cuvinte

def joc_automat_hangman(cuvant_partial, cuvant_complet):
    utilizate = []
    ghicit_partial = list(cuvant_partial)
    incercari = 0

    while ''.join(ghicit_partial) != cuvant_complet:
        alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZĂÂÎȘȚ'
        litere_ramase = []

        for litera_alfabet in alfabet:
            if litera_alfabet in cuvant_complet and litera_alfabet not in utilizate:
                litere_ramase.append(litera_alfabet) 

        if not litere_ramase:
            break

        litera_ghicita = litere_ramase[0]
        utilizate.append(litera_ghicita)
        incercari += 1

        if litera_ghicita in cuvant_complet:
            for i in range(len(cuvant_complet)):
                if cuvant_complet[i] == litera_ghicita:
                    ghicit_partial[i] = litera_ghicita
        else:
            None 

    return incercari, (''.join(ghicit_partial) == cuvant_complet)

def rulare_hangman_csv(fisier):
    pereche_cuvinte = citeste_fisier(fisier)
    total_incercari = 0
    total_cuvinte_ghicite = 0

    for cuvant_partial, cuvant_complet in pereche_cuvinte:
        incercari, cuvant_ghicit = joc_automat_hangman(cuvant_partial, cuvant_complet)
        total_incercari += incercari
        if cuvant_ghicit:
            total_cuvinte_ghicite += 1
        if total_incercari > 1200:
            break  

    return total_incercari, total_cuvinte_ghicite, len(pereche_cuvinte)

total_incercari, total_cuvinte_ghicite, total_cuvinte = rulare_hangman_csv('cuvinte_de_verificat1.csv')

if total_incercari <= 1200:
    print(f"Numărul total de încercări: {total_incercari}")
    print(f"Numărul de cuvinte ghicite: {total_cuvinte_ghicite} din {total_cuvinte}")
else:
    print(f"Numărul total de încercări depășește 1200. Total încercări: {total_incercari}")
    print(f"Numărul total de cuvinte ghicite: {total_cuvinte_ghicite} din {total_cuvinte}")

