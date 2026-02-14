# One approach to calculating the positions of the planets in RA and Dec is to use the J2000.0 coordinate system, which is based on the position of the vernal equinox at 12:00:00 UT on January 1, 2000. You can then use the following formulae to convert the ecliptic longitude (lambda) and latitude (beta) of the planet to RA and Dec:

# tan(alpha) = (sin(lambda) x cos(epsilon) - tan(beta) x sin(epsilon)) / cos(lambda)

# where alpha is the RA of the planet, epsilon is the obliquity of the ecliptic (23.439°), and tan(beta) is the tangent of the planet's ecliptic latitude.

# Dec = arcsin(sin(beta) x cos(epsilon) + cos(beta) x sin(epsilon) x sin(lambda))

# where Dec is the declination of the planet.

# Note that these calculations assume a spherical Earth and a heliocentric model of the solar system.

# I hope this information helps, but please keep in mind that accurate calculations of planetary positions 
# require a deep understanding of astronomy and astrophysics, as well as specialized software and data sources.




import ephem
import math
import datetime
# Define the observer's location
observer = ephem.Observer()
observer.lat = '30.08'  # Latitude of London, UK
observer.lon = '31.2357'  # Longitude of London, UK
observer.elevation = 10   # Elevation of observer in meters

# Define the date and time for which to calculate the planet positions
# date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S') # Format is yyyy/mm/dd hh:mm:ss
date = "2023-04-27 19:00:00"
observer.date = date

# Define the planets to calculate
planets = ['mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']



def get_alt_az(ra, dec, lat, lon, elev, date_time):
    # Create an observer object with the given location and time
    obs = ephem.Observer()
    obs.lat = str(lat)
    obs.lon = str(lon)
    obs.elevation = elev
    obs.date = date_time

    # Create a celestial object with the given RA and Dec values
    obj = ephem.FixedBody()
    obj._ra = ra
    obj._dec = dec

    # Calculate the Alt and Az coordinates for the object
    obj.compute(obs)
    alt = math.degrees(obj.alt)
    az = math.degrees(obj.az)

    # Return the Alt and Az values
    return alt, az



# Calculate the positions of the planets
for planet_name in planets:
    planet = getattr(ephem, planet_name.capitalize())()
    planet.compute(observer)
    ra = planet.ra
    dec = planet.dec
    print(f'{planet_name}: RA={planet.ra}, Dec={planet.dec}')

    # Calculate the Alt and Az coordinates for the planet
    alt, az = get_alt_az(ra, dec, observer.lat , observer.lon, observer.elev, date)

    # Print the results
    print(f'Altitude: {alt:.4f} degrees')
    print(f'Azimuth: {az:.4f} degrees')






