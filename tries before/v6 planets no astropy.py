import math
import datetime
import numpy as np

# Define some constants for the solar system
PLANETS = {
    "mercury": {"a": 0.3871, "e": 0.2056, "i": 7.005, "L": 252.251},
    "venus": {"a": 0.7233, "e": 0.0068, "i": 3.394, "L": 181.979},
    "earth": {"a": 1.0000, "e": 0.0167, "i": 0.000, "L": 100.464},
    "mars": {"a": 1.5237, "e": 0.0934, "i": 1.850, "L": -4.553},
    "jupiter": {"a": 5.2026, "e": 0.0485, "i": 1.305, "L": 34.404},
    "saturn": {"a": 9.5549, "e": 0.0556, "i": 2.485, "L": 50.491},
    "uranus": {"a": 19.2184, "e": 0.0463, "i": 0.772, "L": 314.055},
    "neptune": {"a": 30.1104, "e": 0.0087, "i": 1.770, "L": 304.348},
}
G = 6.6743e-11 # gravitational constant in m^3 kg^-1 s^-2
M_SUN = 1.9885e30 # mass of the Sun in kg
OBLIQUITY = 23.439281 * np.pi / 180 # obliquity of the ecliptic in radians

# Define a function to convert degrees to radians
def deg_to_rad(degrees):
    return degrees * np.pi / 180

# Define a function to convert radians to degrees
def rad_to_deg(radians):
    return radians * 180 / np.pi

# Define a function to calculate the position of a planet
def planet_position(planet, date):
    a = PLANETS[planet]["a"] * 1.496e11 # semi-major axis in meters
    e = PLANETS[planet]["e"] # eccentricity
    i = deg_to_rad(PLANETS[planet]["i"]) # inclination in radians
    L = deg_to_rad(PLANETS[planet]["L"] + 0.9856 * date.toordinal() % 360) # mean longitude in radians
    w = deg_to_rad(0) # argument of perihelion (assumed to be 0 for simplicity)
    M = L - w # mean anomaly in radians
    E = M # initial guess for eccentric anomaly
    while abs(E - e * np.sin(E) - M) > 1e-12:
        E = E - (E - e * np.sin(E) - M) / (1 - e * np.cos(E))
    xv = a * (np.cos(E) - e) # heliocentric x-coordinate of the planet
    yv = a * (np.sqrt(1 - e**2) * np.sin(E)) # heliocentric y-coordinate of the planet
    v = np.arctan2(yv, xv) # true anomaly in radians
    r = np.sqrt(xv**2 + yv**2) # heliocentric distance of the planet in meters
    xh = r * (np.cos(w) * np.cos(v + w) - np.sin(w) * np.sin(v + w) * np.cos(i)) # heliocentric x-coordinate of the planet in the ecliptic plane
    yh = r * (np.sin(w) * np.cos(v + w) + np.cos(w) * np.sin(v + w) * np.cos(i)) # heliocentric y-coordinate of the planet in the ecliptic plane
    zh = r * np.sin(v + w) * np.sin(i) # heliocentric z-coordinate of the planet in the ecliptic plane
    return np.array([xh, yh, zh])

# Define a function to get the positions of all the planets
def get_planet_positions(date, lat, lon):
    positions = {}
    observer_pos = np.array([0, 0, 0])
    observer_pos[0] = np.cos(lat) * np.cos(lon)
    observer_pos[1]= np.cos(lat) * np.sin(lon)
    observer_pos[2] = np.sin(lat)
    for planet in PLANETS:
        pos = planet_position(planet, date)
        # Convert heliocentric coordinates to geocentric coordinates
        pos = pos - observer_pos
        # Convert geocentric ecliptic coordinates to equatorial coordinates
        x_eq = pos[0]
        y_eq = np.cos(OBLIQUITY) * pos[1] - np.sin(OBLIQUITY) * pos[2]
        z_eq = np.sin(OBLIQUITY) * pos[1] + np.cos(OBLIQUITY) * pos[2]
        # Convert equatorial coordinates to (Right Ascension, Declination)
        ra = np.arctan2(y_eq, x_eq)
        dec = np.arcsin(z_eq / np.sqrt(x_eq**2 + y_eq**2 + z_eq**2))
        # Convert (Right Ascension, Declination) to (Altitude, Azimuth)
        sidereal_time = get_sidereal_time(date, lon)
        ha = sidereal_time - ra
        alt = np.arcsin(np.sin(dec) * np.sin(lat) + np.cos(dec) * np.cos(lat) * np.cos(ha))
        az = np.arctan2(-np.sin(ha), np.cos(lat) * np.tan(dec) - np.sin(lat) * np.cos(ha))
        positions[planet] = (rad_to_deg(ra), rad_to_deg(dec), rad_to_deg(alt), rad_to_deg(az))
    return positions

# Define a function to calculate the sidereal time at a given date and longitude
def get_sidereal_time(date, lon):
    julian_day = (date.toordinal() + 1721424.5) + (date.hour - 12) / 24
    centuries_since_1900 = (julian_day - 2415020) / 36525
    mean_sidereal_time = 6.697374558 + 2400.051336 * centuries_since_1900 + 0.000025862 * centuries_since_1900**2
    mean_sidereal_time = mean_sidereal_time % 24
    utc_time = date.hour + date.minute / 60 + date.second / 3600
    sidereal_time = mean_sidereal_time + utc_time * 1.002737909
    sidereal_time = sidereal_time % 24
    sidereal_time = sidereal_time + lon / 15
    sidereal_time = sidereal_time % 24
    return sidereal_time * 15 * np.pi / 180

# Example usage
date = datetime.datetime.utcnow()
lat = deg_to_rad(30.0444) # latitude of San Francisco
lon = deg_to_rad(31.2357) # longitude of San Francisco
positions = get_planet_positions(date, lat, lon)
for planet in positions:
    print(planet.capitalize() + " position (RA, Dec, Alt, Az):", positions[planet])