<<<<<<< HEAD
=======
# Initial test
from FrontEnd import usersettings as us
from User import User as User
import os
import json

user_data = None
userDataPath = "userSettings.json"

if os.path.isfile(userDataPath):
    with open(userDataPath, 'r') as openfile:
        user_json = json.load(openfile)
        user_data = User(user_json['name'], user_json['weeklyFrequency'], user_json['minimumWorkoutDuration'])
else:
    user_json = ""

us.runUserGUI(user_data)
>>>>>>> 15a0f642a9046918e48a9cb854e5104c49b481da
