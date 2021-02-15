from password_gen import password_generator
import PySimpleGUI as sg
import pyperclip
from notifypy import Notify


layout = [
    [sg.Text('Enter the length of a password')],
    [sg.Input()],
    [sg.Checkbox('Do you want numbers in your password?') ],
    [sg.Checkbox('Do you want symbols in your password?')],
    [sg.Button('Generate')]]



window = sg.Window('Window Title', layout)
event, values = window.read()

values[0] = int(values[0])

password = password_generator(values[0], values[1], values[2])

notification = Notify()
notification.title = 'PASSWORD GENERATED'
notification.message = "Your password has been successfully generated."

if event == 'Generate':
    sg.popup(password)
    pyperclip.copy(password)
    notification.send()

window.close()





