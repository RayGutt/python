def make_car(manufacturer, model, **features):
	"""store a car info into a dictionary"""
	car_dict = {}
	car_dict['manufacturer'] = manufacturer
	car_dict['model'] = model
	for key, value in features.items():
		car_dict[key] = value
	return car_dict

car = make_car('renault', 'kangoo', tow_package=True, color='red')

print(car)
