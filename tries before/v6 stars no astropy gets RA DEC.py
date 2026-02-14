
import ephem
import datetime

# Set up observer location (you can change these values to your own location)
observer = ephem.Observer()
observer.lon = '30.0444' # longitude in degrees
observer.lat = '31.2357' # latitude in degrees
observer.elevation = 10   # elevation in meters

now = datetime.datetime.utcnow()
# Set up date and time to now
now = ephem.now()

# Define a list of the top 10 brightest stars
star_names = ['Sirius', 'Canopus', 'Arcturus', 'Vega', 'Capella', 'Rigel', 'Procyon', 'Achernar', 'Betelgeuse']

# Loop over the star names and get their positions
for name in star_names:
    star = ephem.star(name)
    star.compute(now)
    ra = star.ra
    dec = star.dec
    # az, alt = observer.radec_to_azalt(ra, dec)
    print(f'{name}: RA/DEC = {ra}, {dec} ')


