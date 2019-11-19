

def convert_minutes_to_seconds(minutes):
	result = minutes * 60;
	return result;

def convert_hours_to_minutes(hours):
	return hours * 60;

def convert_days_to_hours(days):
	return days * 24;

def convert_hours_to_seconds(hours):
	return hours * 60 *60;



a = 0;

while(a != 5):
	
	print("1 . convert_minutes_to_seconds")
	print("2 . convert_hours_to_minutes")
	print("3 . convert_days_to_hours")
	print("4 . convert_hours_to_seconds")
	print("5 . Quitter")
	
	try :
		a = input()
	except:
		a=5

	if a==5:
		print("On quitte le programme")
	elif a==4:
		print("2 hours = " + str(convert_hours_to_seconds(2)) + " seconds")
	elif a==3:
		print("2 days = " + str(convert_days_to_hours(2)) + " hours")
	elif a==2:
		print("2 hours = " + str(convert_hours_to_minutes(2)) + " minutes")
	elif a==1:
		print("2 minutes = " + str(convert_minutes_to_seconds(2)) + " seconds")







