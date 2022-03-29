import PySimpleGUI as sg

giorno = tuple(range(1, 32))

mese = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]

comuni = []
codici = []

with open('comuni.txt') as i:
	for riga in i:
		x = riga.split(' -- ')
		comuni.append(x[0])
		codici.append(x[1])
		

def main():

    
    layout = [  [ sg.Text("Cognome\t"), sg.Input()],
                [ sg.Text("Nome\t"), sg.Input()],
                [ sg.Text("Sesso\t"), sg.Radio('Maschio', 'sesso', default = True), sg.Radio('Femmina', 'sesso', default = False)],
                [ sg.Text("Data\t"), sg.Combo(giorno, default_value = 1), sg.Combo(mese, default_value = 'Gennaio'), sg.Input(size=(5,1))],
                [ sg.Text("Comune\t"), sg.Combo(comuni)]  ]
                
    
    window = sg.Window('Calcolo Codice Fiscale',layout)
    
    while True:
        event, values = window.read(100)
        if event == sg.WIN_CLOSED:
            break
    window.close()


main()