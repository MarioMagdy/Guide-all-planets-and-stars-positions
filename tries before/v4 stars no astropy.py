# # Import the required modules
# import pandas as pd
# import math
# import ephem
# import pandas as pd

# def ephem_to_degs(x):
#     return float(x)/math.pi *180


# # Read the csv file
# df = pd.read_csv('G:\pythoncodenew\Deepscope getting all planets and stars positions\stars data\list-of-iau-approved-star-names2.csv')

# # Define the observer's time, date, and location
# obs_time = ephem.Date('2023/4/16 16:20:41')
# obs_loc = ephem.Observer()
# obs_loc.lat = '30.0444'
# obs_loc.lon = '31.2357'
# obs_loc.elevation = 0
# out2 =[]

# # Loop over each row in the csv file
# for index, row in df.iterrows():
#     # Get the star name, RA, and Dec from the csv file
#     star_name = row['IAU Name']
#     star_ra = row['RA (J2000)']
#     star_dec = row['Dec (J2000)']

#     # Define the star position at J2000 in RA and Dec
#     star = ephem.FixedBody()
#     star._ra = ephem.hours(star_ra)
#     star._dec = ephem.degrees(star_dec)
#     star._epoch = ephem.J2000

#     # Compute the star's position at the observer's location and time
#     obs_loc.date = obs_time
#     star.compute(obs_loc)

#     # Print the star name and position in RA, Dec, Alt, and Az
#     # print(star_name)
#     # print(f"RA: {star.ra}, Dec: {star.dec}, Alt: {star.alt}, Az: {star.az}")
#     out2.append(f"Star: {star_name}  RA: {ephem_to_degs(star.ra)}, Dec: {ephem_to_degs(star.dec)}, Alt: {ephem_to_degs(star.alt)}, Az: {ephem_to_degs(star.az)}")
#     # print()


# [print(i) for i in (out2)]


# Import the required modules
import ephem
import pandas as pd
import math
import datetime


def ephem_to_degs(x):
    return float(x)/math.pi *180

# Read the csv file
df = pd.read_csv('G:\pythoncodenew\Deepscope getting all planets and stars positions\stars data\list-of-iau-approved-star-names2.csv')

# Define the observer's time, date, and location

# date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S') # Format is yyyy/mm/dd hh:mm:ss
date = '2023/4/29 16:20:41'

obs_time = ephem.Date(date)
obs_loc = ephem.Observer()
obs_loc.lat = '30.0444'
obs_loc.lon = '31.2357'
obs_loc.elevation = 0

# Loop over each row in the csv file
for index, row in df.iterrows():
    if index ==20:
        break

    # Get the star name, RA, and Dec from the csv file
    star_name = row['IAU Name']
    star_ra = row['RA (J2000)']
    star_dec = row['Dec (J2000)']

    # Define the star position at J2000 in RA and Dec
    star = ephem.FixedBody()
    star._ra = str(star_ra)
    star._dec = str(star_dec)
    star._epoch = ephem.J2000
    star.compute(obs_loc)

    # Print the star name and position in RA, Dec, Alt, and Az
    print(star_name)
    print('RA:', ephem.degrees( star.ra),'Dec:',(star.dec))
    # print()
    print('Alt:', star.alt,'Az:', star.az)
    # print()
    # print()