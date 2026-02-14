import ephem

# Set the time and location of the observer
observer = ephem.Observer()
observer.lon = ephem.degrees('10') # longitude
observer.lat = ephem.degrees('60') # latitude
observer.elevation = 200 # elevation in meters
observer.date = '2023/04/16 17:20:00' # date and time in UTC

# Get the positions of the 100 most luminous stars from a text file
stars = []

def ra_to_float(ra):
    # ra is a string in the format 'hhmmss.sss'
    h = ra[:2]
    m = ra[3:5]
    s = ra[6:-1]
    return float(h) + float(m) / 60 + float(s) / 3600

with open(r'G:\pythoncodenew\Deepscope getting all planets and stars positions\stars data\100_stars.txt', 'r') as f:
    for line in f:
        name, ra, dec = line.split()
        print(ra)
        star = ephem.FixedBody()
        star._ra = ephem.hours(ra_to_float(ra)) # right ascension
        star._dec = ephem.degrees(dec) # declination
        star._epoch = ephem.J2000 # epoch
        star.name = name # name
        stars.append(star)

# Compute the positions of the stars for the observer
for star in stars:
    star.compute(observer)

# Print the results
for star in stars:
    print(f"{star.name}:")
    print(f"Altitude: {star.alt:.2f}")
    print(f"Azimuth: {star.az:.2f}")
    print(f"Right Ascension: {star.ra:.2f}")
    print(f"Declination: {star.dec:.2f}")
    print()