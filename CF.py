import PySimpleGUI as sg

mese = []
lettera_mesi = []
elenco_mesi = ["A Gennaio", "B Febbraio", "C Marzo", "D Aprile", "E Maggio", "H Giugno", "L Luglio", "M Agosto", "P Settembre", "R Ottobre", "S Novembre", "T Dicembre"]

for riga in elenco_mesi:
        x = riga.split(' ')
        mese.append(x[1])
        lettera_mesi.append(x[0])

def CF(dati):
    codice = (nome_cognome(dati) + nascita(dati)).upper()
    return(codice)

def nome_cognome(dati):
    codice_c =''
    contatore = 0
    cognome = dati['cognome'].lower()
    nome = dati['nome'].lower()
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
            if contatore == 3:
                continue
            else:
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
    giorno = '{}'.format(dati['gg'])
    if len(giorno) == 1:
        codice = codice + '0' + giorno
    else:
        codice = codice + giorno
    return(codice)

def main():

    giorno = tuple(range(1, 32))

    comuni = []
    codici = []

    with open('comuni.txt') as i:
        for riga in i:
            x = riga.split(' -- ')
            comuni.append(x[0])
            codici.append(x[1])   

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