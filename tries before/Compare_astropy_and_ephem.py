import ephem
import pandas as pd
import math

# Read the csv file
df = pd.read_csv('G:\pythoncodenew\Deepscope getting all planets and stars positions\stars data\list-of-iau-approved-star-names2.csv')


# Define the observer's time, date, and location
date1 = '2023-04-16 16:20:41'
obs_time = ephem.Date(date1)
obs_loc = ephem.Observer()
obs_loc.lat = '31.0444'
obs_loc.lon = '31.2357'
obs_loc.elevation = 0


# Import the required modules
from astropy import units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time
import pandas as pd
# import datetime


date = '2023-4-29 16:20:41'
# print(df)
# Define the observer's time, date, and location
obs_time =date
obs_loc2 =EarthLocation(lat=31.0444*u.deg, lon=31.2357*u.deg, height=0*u.m)





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





def get_stars_eph(index, row ):

    # Get the star name, RA, and Dec from the csv file
    star_name = row['IAU Name']
    star_ra = row['RA (J2000)']
    star_dec = row['Dec (J2000)']

    # Define the star position at J2000 in RA and Dec
    star = ephem.FixedBody()
    star._ra = ephem.hours(star_ra)
    star._dec = ephem.degrees(star_dec)

    # Set the observer's location and time
    obs_loc.date = obs_time

    # Compute the star's altitude and azimuth
    star.compute(obs_loc)
    star_alt = star.alt
    star_az = star.az

    alt, az = get_alt_az(ra, dec, obs_loc.lat , obs_loc.lon, obs_loc.elev, date1)
    return star_name,star_ra, star_dec,star_alt,star_az

    # # Print the star name and position in RA, Dec, Alt, and Az
    # # print(star_name)
    # print(f'{star_name} \t\t RA: {star_ra}, Dec: {star_dec}, Alt: {star_alt}, Az: {star_az}')
    # # print()








def get_stars_ast(index, row ):
    # Get the star name, RA, and Dec from the csv file
    star_name = row['IAU Name']
    star_ra = row['RA (J2000)']
    star_dec = row['Dec (J2000)']

    # Define the star position at J2000 in RA and Dec
    star_coord = SkyCoord(ra=star_ra*u.degree, dec=star_dec*u.degree, obstime=obs_time)

    # Transform the star position from J2000 to CIRS
    star_cirs = star_coord.transform_to('cirs')

    # Transform the star position from CIRS to AltAz
    star_altaz = star_cirs.transform_to(AltAz(location=obs_loc2))

    R=star_cirs.to_string('decimal', precision=8).split(' ')
    A=star_altaz.to_string('decimal', precision=8).split(' ')

    return star_name,R[0],R[1],A[0],A[1]



    # # # Print the star name and position in RA, Dec, Alt, and Az
    # print(star_name,'\t\t ', ': RA DEC -> ', star_cirs.to_string('decimal', precision=8), ' : ALT AZ -> ',star_altaz.to_string('decimal', precision=8))


for index, row in df.iterrows():
    if index ==20:
        break

    star_name,star_ra, star_dec,star_alt,star_az = get_stars_eph(index, row)
    ast_star_name,ast_star_ra, ast_star_dec,ast_star_alt,ast_star_az = get_stars_ast(index, row)

    print(f'{star_name} \n eph RA: {star_ra}, ast RA:{ast_star_ra} ,\n eph Dec: {star_dec}, ast Dec:{ast_star_dec} \n eph Alt: {star_alt}, ast Alt:{ast_star_alt}, \n eph Az: {star_az}, ast Az:{ast_star_az}\n')