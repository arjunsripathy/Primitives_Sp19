import json
from datetime import datetime
import dateutil.parser

file = json.loads(open('W1_shireen-2017-09-17T19:38:21.json').read())
stroke_data = file['results']

#Note file['sequence'] = 3 I don't know what this number is.
print(f"Number of Characters: {len(stroke_data)} written by {file['name']} at time {file['time']}")
#Note replacing 'data' with raster gets raster data.
single_char_data = stroke_data[0]['data']['']
print(f"Number of strokes in character: {len(single_char_data)}")
#Single_char_data is a 3d list.  First dimension is strokes second is substrokes third is single points.
init_time = single_char_data[0][1][0]
print(f"Time drawing began: {init_time}")

init_time_index = dateutil.parser.parse(init_time)

def rel_time_index(time):
	td =  dateutil.parser.parse(time) - init_time_index
	ms = int(td.microseconds/1000)
	return ms

f = open('strokes.txt','w')
f.write("START\n")

for stroke in single_char_data:
	for point in stroke:
		time_index = rel_time_index(point[0])
		x = point[1]['x']
		y = point[1]['y']
		f.write(f"{x},{y},{time_index}\n")
	f.write("BREAK\n")



