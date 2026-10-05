def pobierz_oceny():
    oceny = []
 
    for i in range(5):
        punkty = float(input(f"Podaj liczbe punktow z {i + 1} sprawdzianu: "))
        oceny.append(punkty)
 
    return oceny
 
def oblicz_srednia(oceny):
    return sum(oceny) / len(oceny)
 
def wystaw_ocene(srednia):
    if srednia >= 90:
        return 6
    elif srednia >= 80:
        return 5
    elif srednia >= 70:
        return 4
    elif srednia >= 60:
        return 3
    elif srednia >= 50:
        return 2
    else:
        return 1
 
def wyswietl_raport(imie, oceny, srednia, ocena):
   
    print("Imie ucznia:", imie)
    print("punkty:", oceny)
    print("srednia:", round(srednia, 2))
    print("ocena:", ocena)
 
def main():
    imie = input("Podaj imie ucznia: ")
    oceny = pobierz_oceny()
    srednia = oblicz_srednia(oceny)
    ocena = wystaw_ocene(srednia)
    wyswietl_raport(imie, oceny, srednia, ocena)
 
main()