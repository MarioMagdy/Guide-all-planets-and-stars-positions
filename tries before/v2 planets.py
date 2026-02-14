# Import the required modules
from astropy import units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time
import pandas as pd

# Read the csv file
df = pd.read_csv('G:\pythoncodenew\Deepscope getting all planets and stars positions\stars data\list-of-iau-approved-star-names2.csv')
print(df)
# Define the observer's time, date, and location
obs_time = Time('2023-04-16 16:20:41')
obs_loc =EarthLocation(lat=30.0444*u.deg, lon=31.2357*u.deg, height=0*u.m)

# Loop over each row in the csv file
for index, row in df.iterrows():
    # Get the star name, RA, and Dec from the csv file
    star_name = row['IAU Name']
    star_ra = row['RA (J2000)']
    star_dec = row['Dec (J2000)']

    # Define the star position at J2000 in RA and Dec
    star_coord = SkyCoord(ra=star_ra*u.degree, dec=star_dec*u.degree, obstime=obs_time)

    # Transform the star position from J2000 to CIRS
    star_cirs = star_coord.transform_to('cirs')

    # Transform the star position from CIRS to AltAz
    star_altaz = star_cirs.transform_to(AltAz(location=obs_loc))

    # Print the star name and position in RA, Dec, Alt, and Az
    print(star_name)
    print(star_altaz.to_string('hmsdms'))
    print()



