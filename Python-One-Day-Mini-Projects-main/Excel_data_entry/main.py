import PySimpleGUI as sg
import pandas as pd

sg.theme('DarkTeal9')

EXCEL_FILE = 'Data.xlsx'
df = pd.read_excel(EXCEL_FILE)

layout = [
    [sg.Text('Please Fill out the Following Fields: ')],
    [sg.Text('Name', size=(15,1)), sg.InputText(key='Name')],
    [sg.Text('Favourite Color', size=(15,1)), sg.Combo(['blue','red','black'], key='Favourite Color')],
    [sg.Text('Favourite Sports', size=(15,1)),
                                        sg.Checkbox('Cricket', key='Criket'),
                                        sg.Checkbox('Football', key='Football'),
                                        sg.Checkbox('Sit alone', key='Sit alone')],
    
    [sg.Submit(), sg.Exit()]
]

window = sg.Window('Simple Data Entry App', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Submit':
        df = df.append(values, ignore_index= True)
        df.to_excel(EXCEL_FILE, index= False)
        sg.popup('Data Submitted')
window.close()