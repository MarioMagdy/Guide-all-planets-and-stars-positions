
import ephem
import datetime
import math

def get_alt_az(ra, dec, lat, lon, elev, date_time):
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

now = datetime.datetime.utcnow()
# Set up date and time to now
now = ephem.now()

# Define a list of the top 10 brightest stars
star_names = ['Sirius', 'Canopus', 'Arcturus', 'Vega', 'Capella', 'Rigel', 'Procyon', 'Achernar', 'Betelgeuse']
stars_2 = ["Alpha Centauri","Sirius", "Canopus", "Arcturus", "Vega", "Capella", 
           "Rigel", "Procyon", "Achernar", "Betelgeuse", "Hadar", "Altair", "Acrux", 
           "Aldebaran", "Spica", "Antares", "Pollux", "Fomalhaut", "Deneb", "Mimosa", 
           "Regulus", "Adhara", "Shaula", "Castor", "Gacrux", "Bellatrix", "Elnath", "Miaplacidus", 
           "Alnilam", "Alnair", "Alphard", "Mirfak", "Algieba", "Alioth", "Alsephina", "Mizar", 
           "Alpheratz", "Alcyone", "Hamal", "Mira", "Rasalhague", "Aludra", "Alkaid", "Menkalinan", 
           "Suhail", "Naos", "Avior", "Alpherg", "Dubhe", "Gienah", "Algieba", "Diphda", "Alphard", 
           "Ankaa", "Denebola", "Achird", "Alphacca", "Alshain", "Alwaid", "Atik", "Azha", 
           "Baten Kaitos", "Betria", "Caph", "Chara", "Chort", "Cursa", "Diadem", "Dschubba", 
           "Edasich", "Electra", "Eltanin", "Enif", "Etamin", "Gomeisa", "Graffias", "Homam", 
           "Izar", "Kaus Australis", "Kaus Borealis", "Kitalpha", "Kochab", "Lesath", "Marfik", 
           "Markab", "Mebsuta", "Megrez", "Menkar", "Merak", "Minkar", "Navi", "Nekkar", "Peacock", 
           "Phact", "Porrima", "Rastaban", "Sabik", "Sadalbari", "Sadalmelik", "Sadalsuud", "Saiph", 
           "Scheat", "Schedar", "Sham", "Sheliak", "Sheratan", "Sirius B", "Situla", "Talitha", 
           "Taygeta", "Thuban", "Turais", "Vega B", "Vindemiatrix", "Wasat"]


# Loop over the star names and get their positions
not_in_lib = []
is_in_lib = []
for name in stars_2:
    try:
        star = ephem.star(name)
    except:print("ignoring: ", name);  not_in_lib.append(name)
    else:
        star.compute(now)
        ra = star.ra
        dec = star.dec
        az, alt = get_alt_az(ra, dec, observer.lat, observer.lon, observer.elev, now)
        is_in_lib.append(name)
        print(f'{name}: RA/DEC = {math.degrees(ra)}, {math.degrees(dec)} ; ALT/AZ = {alt}, {az} ')


print('\n\n')
print(not_in_lib,len(not_in_lib))
print('\n\n')
print(is_in_lib,len(is_in_lib))
