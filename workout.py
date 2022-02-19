class Workout():

    workout_dict = {"type" : ""}

    def __init__(self,type) -> None:
        self.type = type
        Workout.workout_dict["type"] = self.type

    def addCardioAttributes(self, time, intensity):
        if self.type.lower() != "cardio":
            raise ValueError ("type is not eqaul to cardio")
        self.time = time
        self.intensity = intensity
        Workout.workout_dict["time"] = self.time
        Workout.workout_dict["intensity"] = self.intensity

    def addStrengthAttributes(self,sets,reps,weight):
        if self.type.lower() != "strength":
            raise ValueError ("type is not equal to strength")
        self.sets = sets
        self.reps = reps
        self.weight = weight
        Workout.workout_dict["reps"] = self.reps
        Workout.workout_dict["sets"] = self.sets
        Workout.workout_dict["weight"] = self.weight


    def toJSON(Self):
        return Workout.workout_dict


w = Workout("cardio")
w.addCardioAttributes(20,"jog")
jsonReturn = w.toJSON()
print(jsonReturn)