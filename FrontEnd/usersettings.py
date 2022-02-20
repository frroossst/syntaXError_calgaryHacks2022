import PySimpleGUI as sg
import json

def saveData(values):
    jsondata = {
        "name": values['name'],
        "weeklyFrequency": values['frequency'],
        "minimumWorkoutDuration": values['minimumWorkout']
    }
    jsonObject = json.dumps(jsondata, indent = 4)
    print(values['name'])



titleText = sg.Text("User Settings", size=(40, 1), font='Any 15', justification="center")

nameLabel = sg.Text("Name:")
nameTextbox = sg.InputText(key='name')
values = [1, 2, 3, 4, 5, 6, 7]
frequencyLabel = sg.Text("Weekly frequency:")
frequencyTextbox = sg.InputOptionMenu(values, key='frequency')

minimumWorkoutLabel = sg.Text("Minimum Workout")
hrsText = sg.Text("hrs")
minimumWorkoutInput = sg.InputText(key='minimumWorkout')




layout = [
    [titleText],
    [nameLabel, nameTextbox],
    [frequencyLabel,frequencyTextbox],
    [minimumWorkoutLabel, minimumWorkoutInput, hrsText],
    [sg.Button("Submit")]
]
window = sg.Window("Demo", layout, size=(400, 600))


# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Submit":
        saveData(values)
    if event == sg.WIN_CLOSED:
        break



window.close()


