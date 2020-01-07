def get_city_country_string(city, country, population=''):
    """Return a single string of the form City, Country - population nnnn"""
    if population:
        string = f"{city.title()}, {country.title()} - population {population}"
    else:
        string = f"{city.title()}, {country.title()}"
        
    return string
