import PySimpleGUI as sg      

layout = [[sg.Text('Workout Motivator!')],                   
                 [sg.Button("Start Workout")],
                 [sg.Button("Settings")],
                 [sg.CalendarButton('calendar')]
                                 
                 ]      

window = sg.Window('App', layout, size=(800,600), element_justification='center')    
while True:
    event, values = window.read()
    print(event,values)
    
    if event == sg.WINDOW_CLOSED:
        break

        
event, values = window.read()    
window.close()  