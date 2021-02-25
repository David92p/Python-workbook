class Persona:
    istituto = "Grace Hospital "
    def __init__(self, nome, cognome, età, residenza):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.residenza = residenza
    
    @classmethod #questo è un decoratore per creare un medoto di classe, ci permette così di passare la classe invece dell'istanza
    def oggetto_da_stringa(cls,string,*args):#passiamo come metodo costruttore la classe stessa ovvero cls - il parametro *arg ci permette di passare correttamente la fuzione alle classi figlie
        nome,cognome,età,residenza = string.split("-")
        return cls(nome,cognome,età,residenza,*args)
    
    def scheda_personale(self):
        scheda = f"""
        Nome: {self.nome}
        Cognome: {self.cognome}
        Età: {self.età}
        Residenza: {self.residenza}
        Istituto = {self.istituto}\n"""
        return scheda
    
    def modifica_scheda(self):
        print("""
        Modifica Sheda: 
        1 - Nome
        2 - Cognome
        3 - Età
        4 - Residenza
        5 - Isituto
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
        if scheda == "5":
            self.istituto = input("Nuovo istituto: ")


class Studente(Persona):
    profilo = "Studente"
    def __init__(self, nome, cognome, età, residenza, corso_studio):
        super().__init__(nome, cognome, età, residenza)
        self.corso_studio = corso_studio
    
    def scheda_personale(self):
        scheda = f"""
        Profilo: {Studente.profilo}
        Corso di studio: {self.corso_studio}
        """
        return super().scheda_personale()+scheda
    
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
        return super().scheda_personale()+scheda 

    def aggiorno_materie(self,nuova):
        if nuova not in self.materia:
            self.materia.append(nuova)

meredith_grey = "Meredith-Grey-51-Seattle"
derek_shepherd = "Derek-Shepper-55-Seattle"
#di seguito utiliziamo gli oggetti creati da Persona sui metodi delle classi figlie
studente1 = Studente.oggetto_da_stringa(meredith_grey, "Neurosurgery")
insegnante1 = Insegnante.oggetto_da_stringa(derek_shepherd, "Neurochirurgia")
studente1.cambio_corso("General surgery")
print(insegnante1.scheda_personale())
print(studente1.scheda_personale())