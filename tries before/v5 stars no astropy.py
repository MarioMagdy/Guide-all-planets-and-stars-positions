import ephem
import pandas as pd

# Read the csv file
df = pd.read_csv('G:\pythoncodenew\Deepscope getting all planets and stars positions\stars data\list-of-iau-approved-star-names2.csv')

# Define the observer's time, date, and location
obs_time = ephem.Date('2023-04-16 16:20:41')
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
    star._ra = ephem.hours(star_ra)
    star._dec = ephem.degrees(star_dec)


    # Set the observer's location and time
    obs_loc.date = obs_time

    # Compute the star's altitude and azimuth
    star.compute(obs_loc)
    star_alt = star.alt
    star_az = star.az

    # Print the star name and position in RA, Dec, Alt, and Az
    # print(star_name)
    print(f'{star_name} \t\t RA: {ephem.degrees(star.ra)}, Dec: {star_dec}, Alt: {star_alt}, Az: {star_az}')
    # print()