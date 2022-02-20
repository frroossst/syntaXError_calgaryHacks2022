import PySimpleGUI as sg
import json
from User import User as User


def saveData(values, user_data):
    jsondata = {
        "name": values['name'],
        "weeklyFrequency": values['frequency'],
        "minimumWorkoutDuration": values['minimumWorkout']
    }
    jsonobject = json.dumps(jsondata, indent=6)
    with open("userSettings.json", "w") as outfile:
        outfile.write(jsonobject)

    user_data = User(values['name'], values['frequency'], values['minimumWorkout'])


def runUserGUI(user_data):
    title_text = sg.Text("User Settings", size=(40, 1), font='Any 15', justification="center")
    name_tabel = sg.Text("Name:")
    name_textbox = sg.InputText(key='name', default_text=user_data.get_name())
    values = [1, 2, 3, 4, 5, 6, 7]
    frequency_label = sg.Text("Weekly frequency:")
    frequency_textbox = sg.InputOptionMenu(values, key='frequency', default_value=user_data.get_WOF())
    minimum_workout_label = sg.Text("Minimum Workout")
    hrs_text = sg.Text("hrs")
    minimum_workout_input = sg.InputText(key='minimumWorkout', default_text=user_data.get_minTime())

    layout = [
        [title_text],
        [name_tabel, name_textbox],
        [frequency_label,frequency_textbox],
        [minimum_workout_label, minimum_workout_input, hrs_text],
        [sg.Button("Submit")]
    ]
    window = sg.Window("Demo", layout, size=(400, 600))

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Submit":
            print(event)
            saveData(values, user_data)
        if event == sg.WIN_CLOSED:
            break

    window.close()

