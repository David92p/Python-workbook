#definisco una classe del modello Studente
class Studente:
    ore_settimanali = 36 #Posso accedere a questa variabile attraverso l'istanza, che se non sarà presente sarà definita come variabile di classe
    #definisco il metodo che crea l'oggetto Studente
    def __init__(self, nome,cognome,corso_studi):
        self.nome = nome
        self.cognome = cognome
        self.corso_studi = corso_studi
    #definisco un secondo metodo che ci permette di visualizzare la scheda di un determinato studente(oggetto)
    def scheda_personale(self):
        return f"Scheda Studente:\n Nome: {self.nome}\n Cognome: {self.cognome}\n Corso di Studi: {self.corso_studi}\n Ore settimanali: {self.ore_settimanali}"


#primo oggeto definito dalla classe Studente
primo_studente = Studente("David","Pain","Informatica")
#secondo oggetto definito dalla classe Studente
secondo_studente = Studente("Meredith","Grey","Chirurgia")
#incremento la variabile di classe ore_settimanali di un determinato studente
primo_studente.ore_settimanali += 4

#Il comando print mostra l'oggetto appena creato dalla classe studente 
#print(primo_studente)
#print(secondo_studente)

#di seguito un modo per definire l'istanza di scheda personale sull'oggetto primo_studente
print(primo_studente.scheda_personale())
#di seguito abbiamo richiamato sulla classe stessa il metodo scheda_personale passando l'oggetto secondo_studente
print(Studente.scheda_personale(secondo_studente))



