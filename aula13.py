speed = 40
local_car = 100

SPEED_RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

# if speed > SPEED_RADAR_1:
#     print('The car speed exceeded the radar 1')
#     if local_car >= (LOCAL_1 - RADAR_RANGE) and local_car <= (LOCAL_1 + RADAR_RANGE) :
#         print('The car was fined!')
#     else: print("The car wasn't fined")

def in_local(loc):
    if loc >= (LOCAL_1 - RADAR_RANGE) or loc <= (LOCAL_1 + RADAR_RANGE):
        return True
    False

def fined_speed(vel):
    if vel >= SPEED_RADAR_1:
        return True
    False

if in_local(local_car) and fined_speed(speed):
    print(f'The car speed exceeded the radar 1: {speed}Km/h. The car was fined')

else:
    print("The car wasn't fined")
