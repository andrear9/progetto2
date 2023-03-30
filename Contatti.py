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
        contatti.append(contatto)

    def RimuoviContatto(self, nome, cognome):
        for ricerca in self.__contatti:
            if ricerca["nome"] == nome and ricerca["cognome"] == cognome:
                self.__contatti.remove(ricerca)

        

