class TrackWorkout(): 

    from datetime import datetime

    TrackWorkout_dict = {}

    def __init__(self,workout_dict) -> None:
        self.workout_dict = workout_dict
        self.start = self.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        TrackWorkout.TrackWorkout_dict["startTime"] = self.start

    def endTime(self) -> None:
        self.end = self.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        TrackWorkout.TrackWorkout_dict["endTime"] = self.end
        startDTobj = self.datetime.strptime(self.start,"%d/%m/%Y %H:%M:%S")
        endDTobj = self.datetime.strptime(self.end,"%d/%m/%Y %H:%M:%S")
        delta = endDTobj - startDTobj
        TrackWorkout.TrackWorkout_dict["duration"] = delta

    def toJSON(self) -> dict:
       return TrackWorkout.TrackWorkout_dict  