import PySimpleGUI as sg
from numpy import empty

giorno = tuple(range(1, 32))
mese = []
lettera_mesi = []
elenco_mesi = ["A Gennaio", "B Febbraio", "C Marzo", "D Aprile", "E Maggio", "H Giugno", "L Luglio", "M Agosto", "P Settembre", "R Ottobre", "S Novembre", "T Dicembre"]

comuni = []
codici = []
with open('comuni.txt') as i:
    for riga in i:
        x = riga.split(' -- ')
        comuni.append(x[0])
        codici.append(x[1])

test = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lettera_controllo = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
algo_pari = [1,0,5,7,9,13,15,17,19,21,1,0,5,7,9,13,15,17,19,21,2,4,18,20,11,3,6,8,12,14,16,10,22,25,24,23]
algo_dispari = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,19,20,21,22,23,24,25]

for riga in elenco_mesi:
        x = riga.split(' ')
        mese.append(x[1])
        lettera_mesi.append(x[0])

def CF(dati):
    incompleto = (nome_cognome(dati) + nascita(dati) + comune(dati)).lower()
    codice = (incompleto + controllo(incompleto)).upper()
    return(codice)

def nome_cognome(dati):
    codice_c =''
    contatore = 0
    cognome = dati['cognome'].lower()
    nome = dati['nome'].lower()
    nome.replace(' ', '')
    vocali = set('aeiou')
    consonanti = set('bcdfghjklmnpqrstvwxyz')
    #cognome
    for x in cognome:
        if x in consonanti:
            codice_c = codice_c + x
            if len(codice_c) >=3:
                break
    if len(codice_c) < 3:
        for x in cognome:
            if x in vocali:
                codice_c = codice_c + x
                if len(codice_c) >=3:
                    break
    while len(codice_c) < 3:
        codice_c = codice_c + 'x'
    codice = codice_c
    #nome
    for x in nome:
        if x in consonanti:
            contatore += 1
            if contatore != 2:
                codice = codice + x
            if len(codice) >=6:
                break
    if len(codice) < 6:
        codice = codice_c
        for x in nome:
            if x in consonanti:
                codice = codice + x
                if len(codice) >=6:
                    break
    if len(codice) < 6:
        for x in nome:
            if x in vocali:
                codice = codice + x
                if len(codice) >=6:
                    break
    while len(codice) < 6:
        codice = codice + 'x'
    
    return(codice)

def nascita(dati):
    anno = '{}'.format(dati['aa'])
    codice = anno[len(anno)-2] + anno[len(anno)-1]
    codice = codice + lettera_mesi[mese.index(dati['mm'])]
    if dati['m'] == True:
        giorno = '{}'.format(dati['gg'])
    else:
        giorno = '{}'.format(dati['gg']+40)
    if len(giorno) == 1:
        codice = codice + '0' + giorno
    else:
        codice = codice + giorno
    return(codice)

def comune(dati):
    codice = codici[comuni.index(dati['comune'])]
    codice = codice.replace('\n', '')
    return(codice)

def controllo(dati):
    i = 0
    c = 0
    for x in dati:
        if i%2 == 0:
            c = c + algo_pari[test.index(x)]
            print(algo_pari[test.index(x)])
        else:
            c = c + algo_dispari[test.index(x)]
            print(algo_dispari[test.index(x)])
        i += 1
    codice = lettera_controllo[c%26]
    return(codice)

def main():

    layout = [  [ sg.Text("Cognome\t"), sg.Input(key='cognome')],
                [ sg.Text("Nome\t"), sg.Input(key='nome')],
                [ sg.Text("Sesso\t"), sg.Radio('Maschio', 'sesso', default = True, key='m'), sg.Radio('Femmina', 'sesso', default = False, key='f')],
                [ sg.Text("Data\t"), sg.Combo(giorno, default_value = 1, key='gg'), sg.Combo(mese, default_value = 'Gennaio', key='mm'), sg.Input(size=(5,1), key='aa')],
                [ sg.Text("Comune\t"), sg.Combo(comuni, key='comune')],
                [ sg.Button('Calcola')],
                [ sg.Text("", key='cf')] ]
                
    window = sg.Window('Calcolo Codice Fiscale',layout)
    
    while True:
        event, values = window.read(100)
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Calcola':
            window['cf'].update('C. F. = {}'.format(CF(values)))

    window.close()

main()