class Contatti:
    def __init__(self):
        self.__contatti = [
        {"nome": "Mario", "cognome": "Rossi", "email": "mario.rossi@example.com", "telefono": "123456789"},
        {"nome": "Luca", "cognome": "Verdi", "email": "luca.verdi@example.com", "telefono": "987654321"},
        {"nome": "Simona", "cognome": "Bianchi", "email": "simona.bianchi@example.com", "telefono": "555555555"},
        {"nome": "Paolo", "cognome": "Neri", "email": "paolo.neri@example.com", "telefono": "333333333"}]

    def AggiungiContatti(self, nome, cognome, email, telefono):
        contatto = {
            "nome" : nome,
            "cognome" : cognome,
            "email" : email,
            "telefono" : telefono
        }
        self.__contatti.append(contatto)

    def RimuoviContatto(self, nome, cognome):
        for ricerca in self.__contatti:
            if ricerca["nome"] == nome and ricerca["cognome"] == cognome:
                self.__contatti.remove(ricerca)

    def ricerca(self):
        nome_r=input("inserisci il nome dell'utente: ")
        cognome_r=input("inserisci il cognome dell'utente: ")
        for x in self.__contatti:
            if x["nome"]==nome_r:
                if x["cognome"]==cognome_r:
                    stringa="""
                    Nome: {}
                    Cognome: {}
                    email: {}
                    numero di telefono: {}""".format(x["nome"], x["cognome"], x["email"], x["telefono"])
                    print(stringa)
                    return stringa
        input("spiacente, ma non ci sono presone che corrispondono alla tua ricerca \n premere invio per continuare")
        print(stringa)
        return stringa
    
    