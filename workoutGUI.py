import webbrowser


class workoutGUI():

    import PySimpleGUI as pg
    import webbrowser
    import json
    pg.theme("DarkAmber")

    def __init__(self) -> None:
        pass

    def main(self):

        layout=[
            [
                [(self.pg.Text('Choose workout type',size=(10, 1), font='Lucida',justification='left',visible=True)),
                self.pg.Listbox(values=["Cardio","Strength"], select_mode='extended', key='fac', size=(20, 4),visible=True)],
                [self.pg.Button('Select', font=('Times New Roman',12),visible=True),
                self.pg.Button("Save",font=('Times New Roman',12),visible=True)] 
            ],
            [
                self.pg.Text("Cardio Workout Details",key="cardio0",visible=False),
                self.pg.Radio("Walk","group1",key="cardio1",visible=False),
                self.pg.Radio("Jog","group1",key="cardio2",visible=False),
                self.pg.Radio("Run","group1",key="cardio3",visible=False),
                self.pg.Text("Choose the amount of minutes",key="cardio5",visible=False),
                self.pg.InputText(1,key="cardio4",visible=False)
            ],
            [
                self.pg.Text("Strength Workout Details",key="strength0",visible=False),
                self.pg.InputText("Enter reps",key="strength1",visible=False),
                self.pg.InputText("Enter sets",key="strength2",visible=False),
                self.pg.InputText("Weight",key="strength3",visible=False) 
            ],
            [
                self.pg.Button("Help",font=("Times New Roman",12),pad=(5,0),visible=True)
            ]
        ]

        window = self.pg.Window("Window",layout,size=(400,600))
        
        run = True
        
        while run:
            event, values = window.read()
            if event == "Cancel" or event == self.pg.WIN_CLOSED:
                run = False
                break

            if event == "Help":
                webbrowser.open("https://www.google.ca")

            elif event == "Save":
                workout_record = {}
            
                if values["fac"][0] == "Cardio":
                    workout_record["workoutType"] = "cardio"
                    if values["cardio1"]:
                        workout_record["cardioType"] = "Walk"
                    elif values["cardio2"]:
                        workout_record["cardioType"] = "Jog"
                    elif values["cardio3"]:
                        workout_record["cardioType"] = "Run"
                    else:
                        self.pg.popup_error("Press select and/or enter appropriate values")
                    # Checking if cardio4 is a valid input
                    if values["cardio4"].isdigit():
                        if int(values["cardio4"]) >= 0:
                            workout_record["intended_duration"] = values["cardio4"]


                elif values["fac"][0] == "Strength":
                    workout_record["workoutType"] = "strength"

                    if values["strength1"].isdigit():
                        if int(values["strength1"]) >= 0:
                            workout_record["reps"] = values["strength1"]
                    else:
                        self.pg.popup_error("Press select and/or enter appropriate values")
                    if values["strength2"].isdigit():
                        if int(values["strength2"]) >= 0:
                             workout_record["sets"] = values["strength2"]
                    else:
                        self.pg.popup_error("Press select and/or enter appropriate values")
                    if values["strength3"].isdigit():
                        if int(values["strength3"]) >= 0:
                            workout_record["weight"] = values["strength3"]
                    else:
                        self.pg.popup_error("Press select and/or enter appropriate values")
                
                print(workout_record)
                with open("workout_tracker.json","w") as fobj:
                    self.json.dump(workout_record,fobj,indent=6)
                    fobj.close()
            
            elif event == "Select" and values["fac"][0] == "Cardio":
                window["cardio1"].Update(visible=True) 
                window["cardio2"].Update(visible=True)
                window["cardio3"].Update(visible=True)
                window["cardio4"].Update(visible=True)
                window["cardio5"].Update(visible=True)
                
                window["strength0"].Update(visible=False)
                window["strength1"].Update(visible=False)
                window["strength2"].Update(visible=False)
                window["strength3"].Update(visible=False)

            elif event == "Select" and values["fac"][0] == "Strength":
                window["cardio1"].Update(visible=False) 
                window["cardio2"].Update(visible=False)
                window["cardio3"].Update(visible=False)
                window["cardio4"].Update(visible=False)
                window["cardio5"].Update(visible=False)

                window["strength0"].Update(visible=True)
                window["strength1"].Update(visible=True)
                window["strength2"].Update(visible=True)
                window["strength3"].Update(visible=True)

        window.close()



W = workoutGUI()
W.main()