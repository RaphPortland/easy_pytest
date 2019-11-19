import convertisseurdetemps


def test_convert_minutes_to_seconds():
	assert convertisseurdetemps.convert_minutes_to_seconds(2) == 120;



def test_convert_hours_to_minutes():
	assert convertisseurdetemps.convert_hours_to_minutes(2)== 120

def test_convert_days_to_hours():
	assert convertisseurdetemps.convert_days_to_hours(2) == 48

def test_convert_hours_to_seconds():
	assert convertisseurdetemps.convert_hours_to_seconds(2) == 7200


def test_convert_minutes_to_seconds2():
	assert convertisseurdetemps.convert_minutes_to_seconds(4) == 240;
