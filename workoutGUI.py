from multiprocessing.sharedctypes import Value


class workoutGUI():

    import PySimpleGUI as pg
    pg.theme("DarkAmber")

    def __init__(self) -> None:
        pass

    def main(self):

        layout=[
            [
                self.pg.Text('Choose workout type',size=(30, 1), font='Lucida',justification='left',visible=True),
                self.pg.Listbox(values=["Cardio","Strength"], select_mode='extended', key='fac', size=(30, 6),visible=True),
                self.pg.Button('Next', font=('Times New Roman',12),visible=True)
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
               self.pg.Text("Strength Worout Details",key="strength0",visible=False),
               self.pg.InputText("Enter reps",key="strength1",visible=False),
               self.pg.InputText("Enter sets",key="strength2",visible=False),
               self.pg.InputText("Weight",key="strength3",visible=False) 
            ]
        ]

        window = self.pg.Window("Window",layout)
        
        run = True
        
        while run:
            event, values = window.read()
            if event == "Cancel" or event == self.pg.WIN_CLOSED:
                run = False
                break
            elif event == "Next" and values["fac"][0] == "Cardio":
                window["cardio1"].Update(visible=True) 
                window["cardio2"].Update(visible=True)
                window["cardio3"].Update(visible=True)
                window["cardio4"].Update(visible=True)
                window["cardio5"].Update(visible=True)
                
                window["strength0"].Update(visible=False)
                window["strength1"].Update(visible=False)
                window["strength2"].Update(visible=False)
                window["strength3"].Update(visible=False)

            elif event == "Next" and values["fac"][0] == "Strength":
                window["cardio1"].Update(visible=False) 
                window["cardio2"].Update(visible=False)
                window["cardio3"].Update(visible=False)
                window["cardio4"].Update(visible=False)
                window["cardio5"].Update(visible=False)

                window["strength0"].Update(visible=True)
                window["strength1"].Update(visible=True)
                window["strength2"].Update(visible=True)
                window["strength3"].Update(visible=True)

            print(values)

        window.close()



W = workoutGUI()
W.main()