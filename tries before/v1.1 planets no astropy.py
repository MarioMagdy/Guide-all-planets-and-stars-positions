import math

# Define a function to calculate the position of a planet
def planet_position(planet, t):
    # Set the orbital elements of the planet
    if planet == "mercury":
        N = math.radians(48.3313 + 3.24587E-5 * t)
        i = math.radians(7.0047 + 5.00E-8 * t)
        w = math.radians(29.1241 + 1.01444E-5 * t)
        a = 0.3870986
        e = 0.205635 + 5.59E-10 * t
        M = math.radians(168.6562 + 4.0923344368 * t)
    elif planet == "venus":
        N = math.radians(76.6799 + 2.46590E-5 * t)
        i = math.radians(3.3946 + 2.75E-8 * t)
        w = math.radians(54.8910 + 1.38374E-5 * t)
        a = 0.7233316
        e = 0.006773 - 1.302E-9 * t
        M = math.radians(48.0052 + 1.6021302244 * t)
    elif planet == "mars":
        N = math.radians(49.5574 + 2.11081E-5 * t)
        i = math.radians(1.8497 - 1.78E-8 * t)
        w = math.radians(286.5016 + 2.92961E-5 * t)
        a = 1.5237103
        e = 0.093394 + 2.516E-9 * t
        M = math.radians(18.6021 + 0.5240207766 * t)
    elif planet == "jupiter":
        N = math.radians(100.4542 + 2.76854E-5 * t)
        i = math.radians(1.3030 - 1.557E-7 * t)
        w = math.radians(273.8777 + 1.64505E-5 * t)
        a = 5.202887
        e = 0.048386 - 1.418E-8 * t
        M = math.radians(19.8950 + 0.0830853001 * t)
    elif planet == "saturn":
        N = math.radians(113.6634 + 2.38980E-5 * t)
        i = math.radians(2.4886 - 1.081E-7 * t)
        w = math.radians(339.3939 + 2.97661E-5 * t)
        a = 9.536675
        e = 0.053861 - 1.524E-9 * t
        M = math.radians(316.9670 + 0.0334442282 * t)
    elif planet == "uranus":
        N = math.radians(74.0005 + 1.3978E-5 * t)
        i = math.radians(0.7733 + 1.9E-8 * t)
        w = math.radians(96.6612 + 3.0565E-5 * t)
        a = 19.189164
        e = 0.047257 + 7.45E-9 * t
        M = math.radians(142.5905 + 0.011725806 * t)
    elif planet == "neptune":
        N = math.radians(131.7806 + 3.0173E-5 * t)
        i = math.radians(1.7700 - 2.55E-7 * t)
        w = math.radians(272.8461 - 6.027E-6 * t)
        a = 30.06992276
        e = 0.008590 + 2.15E-9 * t
        M = math.radians(260.2471 + 0.005995147 * t)

    # Calculate the mean anomaly 
    E = M + e * math.sin(M) * (1.0 + e * math.cos(M)) 
    # Calculate the true anomaly
    nu = 2.0 * math.atan2(math.sqrt(1.0 + e) * math.sin(E / 2.0), math.sqrt(1.0 - e) * math.cos(E / 2.0))

    # Calculate the distance from the sun
    r = a * (1.0 - e * e) / (1.0 + e * math.cos(nu))

    # Calculate the position of the planet in ecliptic coordinates
    X = r * (math.cos(N) * math.cos(nu + w) - math.sin(N) * math.sin(nu + w) * math.cos(i))
    Y = r * (math.sin(N) * math.cos(nu + w) + math.cos(N) * math.sin(nu + w) * math.cos(i))
    Z = r * (math.sin(i) * math.sin(nu + w))

    return (X, Y, Z) # Return the calculated position



# Define the time and location of the observer
t = 2459067.0833333  # Julian day
lat = math.radians(30.0444) # Cairo latitude
lon = math.radians(31.2357) # Cairo longitude
r = 1.0 # Distance from observer to center of Earth

# Get the positions of the planets
planets = ["mercury", "venus", "mars", "jupiter", "saturn", "uranus", "neptune"]
positions = {}
for planet in planets:
    (X, Y, Z) = planet_position(planet, t)
    positions[planet] = (X, Y, Z)

# Convert to equatorial coordinates
equatorial_positions = {}
for planet in positions:
    X = positions[planet][0]
    Y = positions[planet][1]
    Z = positions[planet][2]
    xe = X
    ye = Y * math.cos(lat) + Z * math.sin(lat)
    ze = -Y * math.sin(lat) + Z * math.cos(lat)
    ra = math.atan2(ye, xe)
    dec = math.atan2(ze, math.sqrt(xe ** 2 + ye ** 2))
    equatorial_positions[planet] = (ra, dec)

# Print the results
for planet in planets:
    print(f"{planet.title()}:")
    print(f"Right Ascension: {math.degrees(equatorial_positions[planet][0]):.5f}")
    print(f"Declination: {math.degrees(equatorial_positions[planet][1]):.5f}")