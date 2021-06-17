contacten = {}

def print_menu():
    print("type q om jouw contacten te bekijken")
    print("type w om een contact toe te voegen")
    print("type e om een contact te verwijderen")
    print("type r om een contact aan te passen")
    print("type t om te stoppen")
 
def toon_contacten():
     print(contacten)
def contacten_toevoegen():
    naamcontact = input("wat is de naam van de contact?")
    if naamcontact  not in contacten:
        telefoonnummer = input("wat is de telefoon numer van de contact?")
        contacten[naamcontact] = telefoonnummer
    else:
        print("dit contact zit al in de contactenlijst")    
    
def contacten_verwijderen():
    verwijderen = input("welk contact wilt u verwijderen?")
    del contacten[verwijderen]
def contacten_aanpassen():
    welkeaanpassen = input("welk contact wilt u aanpassen?")
    if welkeaanpassen in contacten:
        aanpassen = input("verander de telefoon nummer")
        contacten[welkeaanpassen] = aanpassen 
    else:
        print("dit contact zit niet in je contactenlijst")
    

def menu():
    doorgaan = True
    
    while doorgaan:
        print_menu()
        keuze = input("wat is uw keuze? ")
        
        if keuze == "t":
            doorgaan = False
        if keuze == "q":
            toon_contacten()
        if keuze == "w":
            contacten_toevoegen()
        if keuze == "e":
            contacten_verwijderen()
        if keuze == "r":
            contacten_aanpassen()
            
menu()