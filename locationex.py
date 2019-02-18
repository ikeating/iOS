

import location
import time
import console
import datetime
import webbrowser
import urllib
console.clear()
console.show_activity()
# Start getting the location
location.start_updates()
for i in range(5):
	time.sleep(5)
	my_loc = location.get_location()
	acc = my_loc['horizontal_accuracy']
	
	# First run
	if i == 0:
		best_loc = my_loc
		best_acc = my_loc['horizontal_accuracy']
		# Setup the alert box
		title = 'Accuracy: {} meters.'.format(acc)
		msg = "Take more time to try to improve accuracy?"
		butt1 = "Good enough."
		butt2 = "Try harder (~25 secs)."
		answer = console.alert(title, msg, butt1, butt2)
		
		# If initial accuracy is good enough, give user the chance to break
		if answer == 1:
						break
						
						
		# If initial accuracy is not good enough, loop 4 more times and try
		# to improve.
		elif answer == 2:
					pass
					
	if acc < best_acc:
		best_loc = my_loc
		best_acc = my_loc['horizontal_accuracy']
	
	print('Best accuracy is now {} meters.'.format(best_acc))

location.stop_updates()


# example output of location.get_location()
# 'vertical_accuracy': 14.31443007336287
# 'horizontal_accuracy': 1414.0
# 'timestamp': 1408639887.267081
# 'altitude': 1514.9893798828125
# 'longitude': -146.64942423483025
# 'course': -1.0
# 'latitude': 39.10669415937833
# 'speed': -1.0


datestamp = datetime.datetime.fromtimestamp(best_loc['timestamp'])
time_str = datestamp.strftime('%Y-%m-%d %H:%M:%S')
lat = best_loc['latitude']
lon = best_loc['longitude']

output = ('My location as of {} was lat: {}, lon: {}, with an accuracy '
'of about {} meters.'.format(time_str, lat, lon, best_acc))

print(output)

#quoted_output = urllib.quote(output)
#cmd = 'launch://messaging?#body={}'.format(quoted_output)
#webbrowser.open(cmd)
