# Import the required modules
from astropy import units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time
import pandas as pd
import datetime


# date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # Format is yyyy/mm/dd hh:mm:ss
date = '2023-4-29 16:20:41'


# Read the csv file
df = pd.read_csv('G:\pythoncodenew\Deepscope getting all planets and stars positions\stars data\list-of-iau-approved-star-names2.csv')
# print(df)
# Define the observer's time, date, and location
obs_time =date
obs_loc =EarthLocation(lat=30.0444*u.deg, lon=31.2357*u.deg, height=0*u.m)


# Loop over each row in the csv file
for index, row in df.iterrows():
    if index ==20:
        break
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
    print(star_name,'\t\t ', ': RA DEC -> ', star_cirs.to_string('decimal', precision=8), ' : ALT AZ -> ',star_altaz.to_string('decimal', precision=8))




# Star:Sulafat  RA: 114.84651947969562, Dec: 72.92681921149837, Alt: 47.01082260426918, Az: 357.37270945177556
# Star:Taiyi  RA: 128.23041888710395, Dec: 30.575016666530374, Alt: 83.70340820299432, Az: 83.33802040315531
# Star:Misam  RA: 194.60108336472413, Dec: 50.022283537110965, Alt: 32.7288560686375, Az: 47.10670479983782
# Star:Mizar  RA: 175.53134981321506, Dec: -87.12220743271176, Alt: -28.349360970940122, Az: 177.3356574967611
# Sirius : RA DEC ->  101.24764761 -16.74280546  : ALT AZ ->  204.40624232 39.61078330