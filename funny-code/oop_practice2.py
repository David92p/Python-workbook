#definisco una classe padre 
class Persona:
    def __init__(self, nome, cognome, età, residenza):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.residenza = residenza
    
    def scheda_personale(self):
        scheda = f"""
        Nome: {self.nome}
        Cognome: {self.cognome}
        Età: {self.età}
        Residenza: {self.residenza}\n"""
        return scheda
    
    def modifica_scheda(self):
        print("""
        Modifica Sheda: 
        1 - Nome
        2 - Cognome
        3 - Età
        4 - Residenza
        """)
        scheda = input("Cosa devi modificare? ")
        if scheda == "1":
            self.nome = input("Nuovo nome: ")
        if scheda == "2":
            self.cognome = input("Nuovo cognome: ")
        if scheda == "3":
            self.età = input("Nuova età: ")
        if scheda == "4":
            self.residenza = input("Nuova residanza: ")


class Studente(Persona):
    #pass il comando pass ci aiuta a ereditare le funzioni espresse nella classe padre
    profilo = "Studente"
    #la classe studente ha ora una nuova versione di __init__, che avrà solo il parametro corso_studio
    #la funzione super() ci permette di ereditare determinati parametri dalla classe principale
    def __init__(self, nome, cognome, età, residenza, corso_studio):
        super().__init__(nome, cognome, età, residenza)
        self.corso_studio = corso_studio
    #questa funzione definisce il corso di studi e richiama tramite la funzione super() i parametri di scheda personale della classe padre 
    def scheda_personale(self):
        scheda = f"""
        Profilo: {Studente.profilo}
        Corso di studio: {self.corso_studio}
        """
        return super().scheda_personale()+scheda
    
    #definiamo una funzione che ci permette di cambiare il parametro corso_studio di __init__
    def cambio_corso(self,corso):
        self.corso_studio = corso

class Insegnante(Persona):
    profilo = "Insegnante"
    def __init__(self, nome, cognome, età, residenza, materia=None):
        super().__init__(nome, cognome, età, residenza)
        if materia == None:
            self.materia = []
        else:
            self.materia= materia
    
    def scheda_personale(self):
        scheda = f"""
        Profilo: {Insegnante.profilo}
        Materie insegnate: {self.materia}
        """
        return super().scheda_personale()+scheda # in questo caso la funz. super() andrà a richiamare i parametri mancanti alla classe padre + parametri scheda sulla classe chiamante
    
    #definisco una funziona che mi permette di aggiungere una materia al parametro lista materie di __init__
    def aggiorno_materie(self,nuova):
        if nuova not in self.materia:
            self.materia.append(nuova)

studente_uno = Studente("Cristina", "Yang", 28, "First Avenue","Cardiac surgery")
insegnante_uno = Insegnante("Miranda", "Bailey", 47, "Second Avenue", ["General surgery"])
#utilizzo la funzione aggiorno_materie della classe Insegnante per aggiungere un elemento alla lista
insegnante_uno.aggiorno_materie("Emergency room")
#stampo la scheda personale dell'oggetto insegnante_uno dopo aver aggiunto un nuovo elemento al parametro materie
print(insegnante_uno.scheda_personale())
#la funzione help ci aiuta ad avere un quadro generale dell'ereditarietà 
#print(help(Studente))

