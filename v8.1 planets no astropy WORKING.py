import ephem
import datetime
import math

ephem.default_newton_precision = ephem.second/100. 

# Set the precision parameter to 0.01 arcseconds
ephem.separation_precision = 0.01 / 3600.0

# Define the observer's location
observer = ephem.Observer()
observer.lat = '30.08'  # Latitude of London, UK
observer.lon = '31.2357'  # Longitude of London, UK
observer.elevation = 10   # Elevation of observer in meters

# Define the date and time for which to calculate the planet positions
date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S') # Format is yyyy/mm/dd hh:mm:ss
# date ="2023-04-27 00:00:00"
observer.date = date

# Define the planets to calculate
planets = ['mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune','moon','sun']


# Calculate the positions of the planets
for planet_name in planets:
    planet = getattr(ephem, planet_name.capitalize())()
    planet.compute(observer)
    ra = planet.ra 

    Dec_hours = planet.dec 
    ra_degrees = float(planet.ra)*180/math.pi

    dec_degrees = planet.dec * 180 / math.pi # Convert Dec from hour angle to degrees

    # print(f'{planet_name}: RA={ra_deg:.2f}°, Dec={dec_deg:.2f}°')
    if dec_degrees > 90:
        dec_degrees = 180 - dec_degrees
        ra_degrees += 180
    elif dec_degrees < -90:
        dec_degrees = -180 - dec_degrees
        ra_degrees += 180
    # print(f'{planet_name}: RA={ra_degrees:.4f}, Dec={dec_degrees:.4f}')

    
    print(f'{planet_name},{ra_degrees},{dec_degrees},{planet.mag}',end=',')


