def location(city, country, population=''):
	if population:
		return f"{city.title()} is in {country.title()} and has a population of {population} people"
	else:
		return f"{city.title()} is in {country.title()}"