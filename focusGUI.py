class focusGUI():

    import PySimpleGUI as pg
    from playsound import playsound
    from TrackWorkout import TrackWorkout as TrackWorkout
    import random
    import json
    import time
    pg.theme("DarkAmber")

    def __init__(self) -> None:
        pass

    def main(self):

        with open("quotes.json","r") as fobj:
            quotes = self.json.load(fobj)
            fobj.close()

        start_time = int(round(self.time.time()))
        index = self.random.randint(0,len(quotes["quotes"])-1)

        t = self.TrackWorkout({})

        layout = [
            [
                self.pg.Text("Time elapsed : ")
            ],
            [
                 self.pg.Text("",size=(8,2),key="timerObj")
            ],
            [
                self.pg.Text(quotes["quotes"][index])
            ],
            [
                self.pg.Button("Play") 
            ],
            [
                self.pg.Button("End Timer",font=("Times New Roman",12),pad=(5,0),visible=True)
            ]
        ]           

        window = self.pg.Window("Window",layout,size=(400,600),element_justification="c")
        
        run = True
        
        while run:
            event, values = window.read()
            if event == "Cancel" or event == self.pg.WIN_CLOSED:
                run = False
                break
            if event == "End Timer":
                t.endTime()
            if event == "Play":
                songs = ["escape.mp3","AgapeOceanSound.mp3","OneDanceDrakefeatWizkidKyla.mp3","TheRockRapFaceOff.mp3"]
                index = self.random.choice(songs)
                self.playsound(index)

            current_time = int(round(self.time.time()))
            window.FindElement("timerObj").Update(current_time - start_time)
            window.Refresh()

            jso = t.toJSON()
            print(jso)
            window.close()

        window.close()
        



f = focusGUI()
f.main()