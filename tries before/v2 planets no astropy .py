import math 
import datetime

# Set the time and location of the observer
timestr = "2023-04-16 17:20:00"  
t = datetime.datetime.strptime(timestr, "%Y-%m-%d %H:%M:%S")
lat = 30.0444 # Cairo latitude in degrees  
lon = 31.2357 # Cairo longitude in degrees

# Calculate the Julian day   
a = (14 - t.month) // 12  
y = t.year + 4800 - a 
m = t.month + 12*a - 3
jd = t.day + (153*m + 2)//5 + 365*y + y//4 - y//100 + y//400 - 32045  

# Calculate the geometric positions of the planets   
planets = {"mercury": [], "venus": [], "mars": [], "jupiter": [], "saturn": [], "uranus": [], "neptune": []}

# Mercury
n = jd - 2451545    # Number of days since J2000
L = 225.4443083 + 29.10535693 * n  # Ecliptic longitude
w = 281.75 + 0.3225 * n             # Argument of perihelion 
E = 0.01670 * math.sin(math.radians(n*359.2242/36525))    # Eccentricity of Mercury's orbit
M = math.radians(L - w - E)        # Mean anomaly  
v = math.degrees(M)                # True anomaly      
x = 0.3870986 * math.cos(math.radians(v)) * (1 - E)       # X coordinate in AU  
y = 0.3870986 * math.sin(math.radians(v)) * (1 - E)       # Y coordinate in AU
planets["mercury"] = [x, y]   

# Venus
n = jd - 2451545   # Number of days since J2000
L = 181.97973 + 58519.213030 * n # Ecliptic longitude
w = 292.74 + 1.182 * n           # Argument of perihelion
E = 0.00677 * math.sin(math.radians(n*359.2376/36525))   # Eccentricity of Venus's orbit 
M = math.radians(L - w - E)     # Mean anomaly  
v = math.degrees(M)             # True anomaly  
x = 0.72333 * math.cos(math.radians(v)) * (1 - E)        # X coordinate in AU 
y = 0.72333 * math.sin(math.radians(v)) * (1 - E)        # Y coordinate in AU
planets["venus"] = [x, y]

# Rest of the planets...

# Convert to equatorial and horizontal coordinates
ra = []  # Right ascension  
dec = [] # Declination  
alt = [] # Altitude  
az = []  # Azimuth

# Equatorial to horizontal
HA = lon    # Hour angle  
alt = math.degrees(math.asin(math.sin(math.radians(dec[0])) * math.sin(math.radians(lat)) + 
                     math.cos(math.radians(dec[0])) * math.cos(math.radians(lat)) * 
                     math.cos(math.radians(HA))))  
az = math.degrees(math.atan2(math.sin(math.radians(HA)), math.cos(math.radians(HA)) *  
                     math.sin(math.radians(lat)) - math.tan(math.radians(dec[0])) *  
                     math.cos(math.radians(lat))))

# Print the results
for planet in planets:
    print(f"{planet.title()}:") 
    print(f"Altitude: {alt[planets.index(planet)]:.5f}")  
    print(f"Azimuth: {az[planets.index(planet)]:.5f}")
    print(f"Right Ascension: {ra[planets.index(planet)]:.5f}")
    print(f"Declination: {dec[planets.index(planet)]:.5f}")
    print()