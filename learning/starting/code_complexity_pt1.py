speed = 61
kilometer_car = 100

RADAR_1 = 60
KILOMETER_1 = 100
RADAR_RANGE = 1

speed_car_passed_radar = speed > RADAR_1
car_passed_radar_1 = kilometer_car >= (KILOMETER_1 - RADAR_RANGE) and kilometer_car <= (KILOMETER_1 + RADAR_RANGE)
car_fined_radar_1 = car_passed_radar_1 and speed_car_passed_radar

if speed_car_passed_radar:
    print("Car speed passed radar.")

if car_passed_radar_1:
    print('Car passed radar 1')

if  car_fined_radar_1:
    print('You were fined!!!')
