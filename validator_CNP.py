lista_judete = [
    (1, 'Alba'), (2, 'Arad'), (3, 'Argeș'), (4, 'Bacău'), (5, 'Bihor'), (6, 'Bistrița-Năsăud'),
    (7, 'Botoșani'), (8, 'Brașov'), (9, 'Brăila'), (10, 'Buzău'), (11, 'Caraș-Severin'),
    (12, 'Cluj'), (13, 'Constanța'), (14, 'Covasna'), (15, 'Dâmbovița'), (16, 'Dolj'), (17, 'Galați'),
    (18, 'Gorj'), (19, 'Harghita'), (20, 'Hunedoara'), (21, 'Ialomița'),
    (22, 'Iași'), (23, 'Ilfov'), (24, 'Maramureș'), (25, 'Mehedinți'), (26, 'Mureș'), (27, 'Neamț'),
    (28, 'Olt'), (29, 'Prahova'), (30, 'Satu Mare'), (31, 'Sălaj'),
    (32, 'Sibiu'), (33, 'Suceava'), (34, 'Teleorman'), (35, 'Timiș'), (36, 'Tulcea'), (37, 'Vaslui'),
    (38, 'Vâlcea'), (39, 'Vrancea'), (40, 'București'), (41, 'București - Sector 1'),
    (42, 'București - Sector 2'), (43, 'București - Sector 3'), (44, 'București - Sector 4'),
    (45, 'București - Sector 5'), (46, 'București - Sector 6'), (51, 'Călărași'), (52, 'Giurgiu')
                 ]
while True:
    cnp = input('Va rugam introduceti CNP: ')
    if len(cnp) != 13:
        print("Codul introdus nu are formatul potrivit! Va rugam verificati!.")
        continue
    elif not cnp.isdigit():
        print("Codul introdus nu are formatul potrivit! Nu are doar cifre.")
        continue
    else:
        s = int(cnp[0])
        aa = int(cnp[1:3])
        ll = int(cnp[3:5])
        zz = int(cnp[5:7])
        jj = int(cnp[7:9])
        nnn = int(cnp[9:12])
        c = int(cnp[12])
        cod = '279146358279'
        suma = 0

        for cifra_cnp in range(12):
            suma += int(cnp[cifra_cnp]) * int(cod[cifra_cnp])
        if suma % 11 == 10:
            cifra_control = 1
        else:
            cifra_control = suma % 11

        if 1 <= s <= 9:
            if 0 <= aa <= 99:
                if 1 <= ll <= 12:
                    if 1 <= zz <= 31:
                        if 1 <= nnn <= 999:
                            if cifra_control == c:
                                if 1 <= jj <= 46 or 51 <= jj <= 52:
                                    if s in [1, 3, 5, 7]:
                                        print(f'CNP valid. \nPersoana este de sex masculin, s-a nascut in judetul '
                                              f'{lista_judete[jj - 1][1]} la data de {zz:0>2d}.{ll:0>2d}.{aa}.')
                                    else:
                                        print(f'CNP valid. \nPersoana este de sex feminin, s-a nascut in judetul '
                                              f'{lista_judete[jj - 1][1]} la data de {zz:0>2d}.{ll:0>2d}.{aa}.')
                                else:
                                    print('CNP invalid')
                            else:
                                print('CNP invalid')
                        else:
                            print('CNP invalid')
                    else:
                        print('CNP invalid')
                else:
                    print('CNP invalid')
            else:
                print('CNP invalid')
        else:
            print('CNP invalid')
    din_nou = input('Doriti sa verificati alt CNP? Da / Nu: ').lower()
    if din_nou != 'da':
        break


""" Am incercat sa introduc CNP-ul meu dar nu imi spune nici daca este valid nici invalid
Aici as fi vrut si o descriere a cnp-ului daca este valid: sex - masculin, nascut la data de...., judet ...
judetele nu sunt doar pana la 46 mai exista si un 51, 52 din cate retin
ca sa spui de unde este persoana poti folosi o lista de tupluri ptr judet ex.: lista_judet = [('01', 'Alba'), 
('02', 'Arad'), ....]
Nu notez acum. Incearca sa mai rafinezi si ma mai uit odata peste el

Altceva! bravo!"""