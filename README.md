# DeepScope: Planets and Stars Positions (No Astropy)
*this project was developed in 2021*
This project is focused on getting celestial positions (mainly **RA/Dec**) for:
- Solar system bodies (planets, Moon, Sun)
- Bright stars

The implementation uses `ephem` (PyEphem) and avoids `astropy`.

## What Is Being Done

- Calculate real-time positions for major planets with observer location settings.
- Calculate positions for a curated list of bright stars.
- Combine stars + planets and rank them by brightness (`mag`) to get top visible objects.
- Keep astronomy datasets (stars/galaxies) in local files for later expansion.

## Main Scripts

- `v8.1 planets no astropy WORKING.py`
  - Computes RA/Dec + magnitude for: Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Moon, Sun.
  - Prints comma-separated values.

- `v6.3 Stars no astropy Working.py`
  - Computes RA/Dec + magnitude for a hardcoded list of bright stars.
  - Prints comma-separated values.

- `top_brightness.py`
  - Builds one dictionary of stars and planets, sorts by magnitude, and prints the top ~20 brightest objects.

- `v6.1 Stars no astropy.py`, `v6.2 Stars no astropy WORKING copy.py`, `v8 planets no astropy WORKING.py`
  - Earlier/alternate working versions.

- `tries before/`
  - Historical iterations and experiments.

## Data Folders

- `stars data/100_stars.txt`
  - Reference list of very luminous stars with RA/Dec strings.
- `stars data/list-of-iau-approved-star-names.csv`
  - Approved star names dataset.
- `galaxies/COMBO17.csv`
  - Galaxy catalog data (COMBO-17).

## Requirements

Python 3.x and:

```bash
pip install ephem
```

If `ephem` install fails in your environment, try:

```bash
pip install pyephem
```

## Run

```bash
python "v8.1 planets no astropy WORKING.py"
python "v6.3 Stars no astropy Working.py"
python "top_brightness.py"
```

## Current Status

- Core scripts are present and structured as working versions.
- In this environment, runs fail until `ephem` is installed (`ModuleNotFoundError: No module named 'ephem'`).
