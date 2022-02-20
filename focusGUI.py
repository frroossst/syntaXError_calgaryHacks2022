class focusGUI():

    import PySimpleGUI as pg
    from TrackWorkout import TrackWorkout as TrackWorkout
    import random
    import json
    import time
    import vlc
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
                self.pg.Button("Play"), self.pg.Button("Stop") 
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
                songs = {"escape.mp3" : 192,"AgapeOceanSound.mp3" : 165,"OneDanceDrakefeatWizkidKyla.mp3" : 175,"TheRockRapFaceOff.mp3" : 51}
                index = self.random.choice(list(songs.keys()))
                p = self.vlc.MediaPlayer(index)
                p.play()
                self.time.sleep(songs[index])
                p.stop()
            if event == "Stop":
                break 


            current_time = int(round(self.time.time()))
            window.FindElement("timerObj").Update(current_time - start_time)
            window.Refresh()

            jso = t.toJSON()
            print(jso)
            window.close()

        window.close()
        



f = focusGUI()
f.main()