import os
from Contatti import Contatti
def ricerca(contatti):
    nome_r=input("inserisci il nome dell'utente: ")
    cognome_r=input("inserisci il cognome dell'utente: ")
    for x in contatti:
        if x["nome"]==nome_r:
            if x["cognome"]==cognome_r:
                stringa="""
                Nome: {}
                Cognome: {}
                email: {}
                numero di telefono: {}""".format(x["nome"], x["cognome"], x["email"], x["telefono"])
                return stringa
    input("spiacente, ma non ci sono presone che corrispondono alla tua ricerca\npremere invio per continuare")
    stringa="nil"
    return stringa
contatti=[
        {"nome": "Mario", "cognome": "Rossi", "email": "mario.rossi@example.com", "telefono": "123456789"},
        {"nome": "Luca", "cognome": "Verdi", "email": "luca.verdi@example.com", "telefono": "987654321"},
        {"nome": "Simona", "cognome": "Bianchi", "email": "simona.bianchi@example.com", "telefono": "555555555"},
        {"nome": "Paolo", "cognome": "Neri", "email": "paolo.neri@example.com", "telefono": "333333333"}]
stringa=ricerca(contatti)
print(stringa)