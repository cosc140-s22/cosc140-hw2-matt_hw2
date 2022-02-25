#######################################################
#
# COSC 140 Homework 2, "bus trip planner" problem
#
#######################################################

dep_time = int(input("When will your bus depart? HHMM "))
travel_dis = int(input("How far is your destination (in kilometers)? "))
stop_num = int(input("How many stops are there? "))

sec_traveled = 3600*(travel_dis/40) + 30*stop_num 
hours, minutes = divmod(dep_time, 100)

hours_traveled = sec_traveled // 3600
min_traveled = (sec_traveled % 3600) // 60
seconds = sec_traveled % 60

hours += hours_traveled
minutes += min_traveled 
if minutes >= 60:
  minutes = minutes % 60 
  hours += 1
if hours >= 24:
  hours = 0

print(f"Your predicted arrival time is {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}")

