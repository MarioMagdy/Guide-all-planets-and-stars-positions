import ephem
import datetime
import math
# Set the precision parameter to 0.01 arcseconds
ephem.separation_precision = 0.01 / 3600.0

# Define the observer's location
observer = ephem.Observer()
observer.lat = '30.08'  # Latitude of London, UK
observer.lon = '31.2357'  # Longitude of London, UK
observer.elevation = 10   # Elevation of observer in meters

# Define the date and time for which to calculate the planet positions
# date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S') # Format is yyyy/mm/dd hh:mm:ss
date ="2023-04-27 00:00:00"
observer.date = date


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

# Define the planets to calculate
planets = ['mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']

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

    print(f'{planet_name}: RA={ra_degrees:.6f}, Dec={dec_degrees:.6f}')
    alt, az = get_alt_az(ra, Dec_hours, observer.lat , observer.lon, observer.elev, date)

    # Print the results
    print(f'Altitude: {alt:.4f} degrees')
    print(f'Azimuth: {az:.4f} degrees')
    print('\n')




    import math


print()
# def convert_ha_to_degrees(ha, lat, ra):
#     # Convert HA to Dec in degrees
#     dec_ha = ha
#     dec_degrees = math.degrees(math.asin(math.sin(math.radians(dec_ha)) * math.sin(math.radians(lat)) + math.cos(math.radians(dec_ha)) * math.cos(math.radians(lat)) * math.cos(math.radians(ha))))

#     # Convert RA to degrees
#     ra_degrees = ra * 15.0

#     # Adjust Dec and RA ranges if necessary
#     if dec_degrees > 90.0:
#         dec_degrees = 180.0 - dec_degrees
#         ra_degrees = ra_degrees + 180.0
#     elif dec_degrees < -90.0:
#         dec_degrees = -180.0 - dec_degrees
#         ra_degrees = ra_degrees + 180.0
#     if ra_degrees > 360.0:
#         ra_degrees = ra_degrees - 360.0
#     elif ra_degrees < 0.0:
#         ra_degrees = ra_degrees + 360.0

#     return dec_degrees, ra_degrees