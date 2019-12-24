def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user"""
	profile = {}
	profile['firt_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('Ray', 'Gutt',
							 loves='bicycle',
							 field='IT')

print(user_profile)
