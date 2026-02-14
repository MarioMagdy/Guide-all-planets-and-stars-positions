
import ephem
# import datetime
import math

def get_alt_az(star, lat, lon, elev, date_time):
    # Create an observer object with the given location and time
    obs = ephem.Observer()
    obs.lat = str(lat)
    obs.lon = str(lon)
    obs.elevation = elev
    obs.date = date_time

    # Calculate the Alt and Az coordinates for the object
    star.compute(obs)
    alt = math.degrees(star.alt)
    az = math.degrees(star.az)

    # Return the Alt and Az values
    return alt, az




# Set up observer location (you can change these values to your own location)
observer = ephem.Observer()
observer.lon = '30.0444' # longitude in degrees
observer.lat = '31.2357' # latitude in degrees
observer.elevation = 10   # elevation in meters

# now = datetime.datetime.utcnow()
# Set up date and time to now
now = ephem.now()

is_in_lib = ['Sirius', 'Canopus', 'Arcturus', 'Vega', 'Capella', 'Rigel', 'Procyon', 'Achernar',
              'Betelgeuse', 'Hadar', 'Altair', 'Acrux', 'Aldebaran', 'Spica', 'Antares', 'Pollux',
                'Fomalhaut', 'Deneb', 'Mimosa', 'Regulus', 'Adhara', 'Shaula', 'Castor', 'Gacrux', 
                'Bellatrix', 'Elnath', 'Miaplacidus', 'Alnilam', 'Alnair', 'Alphard', 'Mirfak', 
                'Algieba', 'Alioth', 'Mizar', 'Alpheratz', 'Alcyone', 'Hamal', 'Rasalhague', 
                'Alkaid', 'Menkalinan', 'Suhail', 'Naos', 'Avior', 'Dubhe', 'Gienah', 'Algieba',
                  'Diphda', 'Alphard', 'Ankaa', 'Denebola', 'Alshain', 'Caph', 'Electra', 
                  'Eltanin', 'Enif', 'Etamin', 'Izar', 'Kaus Australis', 'Kochab', 'Markab', 
                  'Megrez', 'Menkar', 'Merak', 'Minkar', 'Peacock', 'Sabik', 'Sadalmelik', 
                  'Saiph', 'Scheat', 'Schedar', 'Sheliak', 'Taygeta', 'Thuban', 'Vindemiatrix']


# Loop over the star names and get their positions
for name in is_in_lib:
    try:
        star = ephem.star(name)
    except:print("ignoring: ", name)
    else:
        star.compute(now)
        ra = star.ra
        dec = star.dec
        az, alt = get_alt_az(star, observer.lat, observer.lon, observer.elev, now)
        # is_in_lib.append(name)
        print(f'{name}: RA/DEC = {math.degrees(ra)}, {math.degrees(dec)} ; ALT/AZ = {alt}, {az} ')



# print(is_in_lib,len(is_in_lib))
