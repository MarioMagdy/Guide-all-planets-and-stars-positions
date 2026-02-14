
import ephem
# import datetime
import math

ephem.default_newton_precision = ephem.second/100. 



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

obj_dict ={}
mags=[]
# print(ephem.stars())
# Loop over the star names and get their positions
for name in is_in_lib:
    try:
        star = ephem.star(name)
    except:print("ignoring: ", name)
    else:
        star.compute(now)
        ra = star.ra
        dec = star.dec
        # az, alt = get_alt_az(star, observer.lat, observer.lon, observer.elev, now)
        # is_in_lib.append(name)
        # print(f'{name}: RA/DEC = {math.degrees(ra)}, {math.degrees(dec)} ; ALT/AZ = {alt}, {az} ')
        obj_dict[name] = [math.degrees(ra), math.degrees(dec),star.mag]


        mags.append(star.mag)



    

        

# print(obj_dict)






# Define the date and time for which to calculate the planet positions
date =  ephem.now()
# date ="2023-04-27 00:00:00"
observer.date = date

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

    
    # print(f'{planet_name},{ra_degrees},{dec_degrees},{planet.mag}',end=',')
    obj_dict[planet_name] = [ra_degrees, dec_degrees,planet.mag]

bright_obj = sorted(obj_dict.items(), key=lambda x:x[1][2])
for i in range(len(obj_dict.items()))[:20]:
  print(bright_obj[i][0]+','+str(bright_obj[i][1][0])+','+str(bright_obj[i][1][1]), end=',')


