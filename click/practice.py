sensors = {"4213": ("STEM Center", 0),
           "4201": ("Foundation Lab", 1),
           "4204": ("CS Lab", 2),
           "4218": ("Workshop Room", 3),
           "4205": ("Tiled Room", 4),
           "Out": ("Outside", 5)
           }

sensor_list = [(key, sensors[key][0], sensors[key][1]) for key in sensors]
print(sensor_list)

for key in sensors:
    sensor_tuple = (key, sensors[key][0], sensors[key][1])
    sensor_list.append(sensor_tuple)
print(sensor_list)
