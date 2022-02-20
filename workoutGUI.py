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
                window["cardio5"].update(visible=True)

            elif event == "Next" and values["fac"][0] == "Strength":
                pass

            print(values)

        window.close()



W = workoutGUI()
W.main()