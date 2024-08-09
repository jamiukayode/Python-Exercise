# # pip install astropy       9/8/2024

# from astropy.coordinates import get_body, EarthLocation
# from astropy.time import Time

# now = Time.now()
# location = EarthLocation.of_site('greenwich')
# planet_name = input("Enter the name of the planet: ").lower()
# planet_position = get_body(planet_name, now, location)

# print(f"{planet_name.capitalize()} "
#       f"position:RA = {planet_position.ra},"
#       f"August = {planet_position.dec}"
#       )


# pip install astropy

from astropy.coordinates import get_body, EarthLocation
from astropy.time import Time

# Get the current time
now = Time.now()

try:
    # Try to get the location for Greenwich
    location = EarthLocation.of_site('greenwich')
except KeyError:
    # If the site is not recognized, manually set the coordinates for Greenwich
    location = EarthLocation(lat=51.4769, lon=0.0005, height=0)  # Greenwich coordinates

# Get the planet name from the user
planet_name = input("Enter the name of the planet: ").lower()

try:
    # Get the position of the planet
    planet_position = get_body(planet_name, now, location)

    # Print the position in RA (Right Ascension) and Dec (Declination)
    print(f"{planet_name.capitalize()} position: RA = {planet_position.ra}, Dec = {planet_position.dec}")
except AttributeError:
    # Handle cases where the planet name is not recognized
    print(f"Could not find information for the planet: {planet_name.capitalize()}. Please check the name and try again.")
