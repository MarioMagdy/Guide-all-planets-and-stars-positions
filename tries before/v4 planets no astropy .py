import math
import datetime

# Define some constants
AU = 149597870700  # Astronomical unit in meters
DEG_TO_RAD = math.pi / 180.0
RAD_TO_DEG = 180.0 / math.pi

# Define the observer's location
observer_lat = 30.0444 * DEG_TO_RAD
observer_lon = 31.2357 * DEG_TO_RAD
observer_alt = 0.0  # Assume observer is at sea level

# Define the time of observation
observer_time = datetime.datetime(2023, 4, 16, 17, 20, 0)  # Cairo time

# Define the planets and their orbital elements
planets = {
    'mercury': {
        'a': 0.38709893 * AU,
        'e': 0.20563069,
        'i': 7.00487 * DEG_TO_RAD,
        'L': 252.25084 * DEG_TO_RAD,
        'p': 77.45771 * DEG_TO_RAD,
        'M': 77.45645 * DEG_TO_RAD,
        'N': 48.33076 * DEG_TO_RAD
    },
    'venus': {
        'a': 0.72333199 * AU,
        'e': 0.00677323,
        'i': 3.39471 * DEG_TO_RAD,
        'L': 181.97973 * DEG_TO_RAD,
        'p': 131.60247 * DEG_TO_RAD,
        'M': 131.60044 * DEG_TO_RAD,
        'N': 76.67992 * DEG_TO_RAD
    },
    'earth': {
        'a': 1.00000011 * AU,
        'e': 0.01671022,
        'i': 0.0,
        'L': 100.46435 * DEG_TO_RAD,
        'p': 102.94719 * DEG_TO_RAD,
        'M': 102.94719 * DEG_TO_RAD,
        'N': 0.0
    },
    'mars': {
        'a': 1.52366231 * AU,
        'e': 0.09341233,
        'i': 1.85061 * DEG_TO_RAD,
        'L': -4.553432 * DEG_TO_RAD,
        'p': -23.94363 * DEG_TO_RAD,
        'M': -23.94363 * DEG_TO_RAD,
        'N': 49.55954 * DEG_TO_RAD
    },
    'jupiter': {
        'a': 5.20336301 * AU,
        'e': 0.04839266,
        'i': 1.30530 * DEG_TO_RAD,
        'L': 34.40438 * DEG_TO_RAD,
        'p': 14.72848 * DEG_TO_RAD,
        'M': 14.72848 * DEG_TO_RAD,
        'N': 100.47390 * DEG_TO_RAD
    },
    'saturn': {
        'a': 9.53707032 * AU,
        'e': 0.05415060,
        'i': 2.48446 * DEG_TO_RAD,
        'L': 49.94432 * DEG_TO_RAD,
        'p': 92.59888 * DEG_TO_RAD,
        'M': 92.59888 * DEG_TO_RAD,
        'N': 113.66242 * DEG_TO_RAD
    },
    'uranus': {
        'a': 19.19126393 * AU,
        'e': 0.04716771,
        'i': 0.76986 * DEG_TO_RAD,
        'L': 313.23218 * DEG_TO_RAD,
        'p': 170.95424 * DEG_TO_RAD,
        'M': 170.95424 * DEG_TO_RAD,
        'N': 74.01692 * DEG_TO_RAD
    },
    'neptune': {
        'a': 30.06896348 * AU,
        'e': 0.00858587,
        'i': 1.76917 * DEG_TO_RAD,
        'L': -55.12003 * DEG_TO_RAD,
        'p': 44.96476 * DEG_TO_RAD,
        'M': 44.96476 * DEG_TO_RAD,
        'N': 131.78423 * DEG_TO_RAD
    }
}

# Define some helper functions
def kepler(M, e):
    E = M
    while True:
        E_next = E - (E - e * math.sin(E) - M) / (1 - e * math.cos(E))
        if abs(E_next - E) < 1e-10:
            break
        E = E_next
    return E

def ecliptic_to_equatorial(x, y, z, obl):
    cos_obl = math.cos(obl)
    sin_obl = math.sin(obl)
    x_eq = x
    y_eq = y * cos_obl - z * sin_obl
    z_eq = y * sin_obl + z * cos_obl
    ra = math.atan2(y_eq, x_eq)
    dec = math.atan2(z_eq, math.sqrt(x_eq**2 + y_eq**2))
    return ra, dec

# Calculate the Julian date
jd = 367 * observer_time.year - \
     int(7 * (observer_time.year + int((observer_time.month + 9) / 12.0)) / 4.0) + \
     int(275 * observer_time.month / 9.0) + \
     observer_time.day + 1721013.5 + \
     ((observer_time.second / 60.0 + observer_time.minute) / 60.0 + observer_time.hour) / 24.0

# Calculate the number of centuries since J2000
T = (jd - 2451545.0) / 36525.0

# Calculate the obliquity of the ecliptic
obl = (23.439291 - 0.0130042 * T - 1.64e-7 * T**2 + 5.04e-7 * T**3) * DEG_TO_RAD

# Calculate the positions of the planets
positions = {}
for planet in planets:
    a = planets[planet]['a']
    e = planets[planet]['e']
    i = planets[planet]['i']
    L = planets[planet]['L']
    p = planets[planet]['p']
    M = planets[planet]['M']
    N = planets[planet]['N']

    # Calculate the mean anomaly
    n = math.sqrt(1.0 / a**3)
    M = L - p
    while M < 0.0:
        M += 2.0 * math.pi
    while M >= 2.0 * math.pi:
        M -= 2.0 * math.pi

    # Calculate the eccentric anomaly
    E = kepler(M, e)

    # Calculate the true anomaly
    v = 2.0 * math.atan2(math.sqrt(1.0 + e) * math.sin(E / 2.0), math.sqrt(1.0 - e) * math.cos(E / 2.0))
    while v < 0.0:
        v += 2.0 * math.pi
    while v >= 2.0 * math.pi:
        v -= 2.0 * math.pi

    # Calculate the distance and position in the orbital plane
    r = a * (1.0 - e * math.cos(E))
    x_orb = r * math.cos(v)
    y_orb = r * math.sin(v)

    # Calculate the position in the ecliptic plane
    x_ecl = x_orb * (math.cos(N) * math.cos(p + v) - math.sin(N) * math.sin(p + v) * math.cos(i))
    y_ecl = x_orb * (math.sin(N) * math.cos(p + v) + math.cos(N) * math.sin(p + v) * math.cos(i))
    z_ecl = x_orb * (math.sin(p + v) * math.sin(i))

    # Convert to equatorial coordinates
    ra, dec = ecliptic_to_equatorial(x_ecl, y_ecl, z_ecl, obl)

    # Save the position
    positions[planet] = {
        'ra': ra,
        'dec': dec,
        'r': r
    }

# Calculate the AltAz positions
altaz_positions = {}
for planet in positions:
    ra = positions[planet]['ra']
    dec = positions[planet]['dec']
    r = positions[planet]['r']

    # Calculate the hour angle
    LST = (observer_time.hour + observer_time.minute / 60.0 + observer_time.second / 3600.0) * 15.0 * DEG_TO_RAD
    HA = LST - ra

    # Calculate the altitude and azimuth
    sin_alt = math.sin(observer_lat) * math.sin(dec) + math.cos(observer_lat) * math.cos(dec) * math.cos(HA)
    alt = math.asin(sin_alt)
    cos_az = (math.sin(dec) - math.sin(observer_lat) * sin_alt) / (math.cos(observer_lat) * math.cos(alt))
    az = math.acos(cos_az)
    if math.sin(HA) > 0.0:
        az = 2.0 * math.pi - az

    # Save the AltAz position
    altaz_positions[planet] = {
        'alt': alt,
        'az': az,
        'r': r
    }

# Print the results
for planet in planets:
    print(f"{planet.title()}:")
    print(f"Altitude: {altaz_positions[planet]['alt'] * RAD_TO_DEG:.5f}")
    print(f"Azimuth: {altaz_positions[planet]['az'] * RAD_TO_DEG:.5f}")
    print(f"Right Ascension: {positions[planet]['ra'] * RAD_TO_DEG:.5f}")
    print(f"Declination: {positions[planet]['dec'] * RAD_TO_DEG:.5f}")
    print()