while "true":
    spiegazione = '''
    Benvenuto o benvenuta nel programma della carcolatrice virtuale
    Autore: Davide Panetta\n
    Se vuoi eseguire un'addizione digita 1
    Se vuoi eseguire una sottrazione digita 2
    Se vuoi eseguire una moltiplicazione digita 3
    Se vuoi eseguire una divisione digita 4
    Se vuoi eseguire un calcolo esponenziale digita 5 
    Se vuoi uscire dal programma digita ESC\n
    Buon calcolo
    '''
    print('*****************************************************************')
    print(spiegazione)
    print('*****************************************************************')

    digita = input('\nInserisci il numero dell\'operazione desiderata ---> ')
    digita = digita.lower()
    if digita == str("1"):
        a = input('inserisci il primo numero ')
        b = input('inserisci il secondo numero ')
        print('il risultato di', a, '+', b, 'e =', float(a)+float(b))
    elif digita == str("2"):
        a = input('inserisci il primo numero ')
        b = input('inserisci il secondo numero ')
        print('il risultato di', a, '-', b, 'e =', float(a)-float(b))
    elif digita == str("3"):
        a = input('inserisci il primo numero ')
        b = input('inserisci il secondo numero ')
        print('il risultato di', a, 'x', b, 'e =', float(a)*float(b))
    elif digita == str("4"):
        a = input('inserisci il primo numero ')
        b = input('inserisci il secondo numero ')
        print('il risultato di',a,'/',b,'e =',float(a)/float(b))
    elif digita == str("5"):       
        a = input('inserisci la base del numero ')    
        b = input('inserisci l\'esponte della base ')
        print('il risultato di', a, 'elavato a', b, 'e =', float(a)**float(b))
    elif digita == 'esc':
        break
    print('*****************************************************************')
    loop = input("Vuoi effettuare un'altra operazione all'interno del programma? Si/No ")
    loop = loop.lower()
    if loop == "si":
        continue
    else:
        break

print('*****torna presto a trovarci*****')

