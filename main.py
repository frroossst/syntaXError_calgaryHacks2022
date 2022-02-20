# Initial test
from FrontEnd import usersettings as us
from User import User as User
import os
import json
# test
user_data = None
userDataPath = "userSettings.json"

if os.path.isfile(userDataPath):
    with open(userDataPath, 'r') as openfile:
        user_json = json.load(openfile)
        user_data = User(user_json['name'], user_json['weeklyFrequency'], user_json['minimumWorkoutDuration'])
else:
    user_data = User()

us.runUserGUI(user_data)
