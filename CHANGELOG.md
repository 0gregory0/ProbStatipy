# Changelog

## [0.0.4] -> 2023-12-27
### Fixed
- fixed more import issues on spread.py I hope this is the last one.

## [0.0.3] -> 2023-12-27
### Fixed
- fixed more import issues on spread.py

## [0.0.2] -> 2023-12-27
### Fixed
- spread.py was importing from `pystats_central`. This module doesn't exist as it was renamed to `statspro_central` then `central`.

## [0.0.1] -> 2023-12-27
### Initial Release
A package for statistical analysis containing the following modules:
- central.py - Computes measures of Central Tendancy such as:
    - mean
    - median
    - mode

- spread.py - Computes measures of dispersion/spread such as:
    - variance
    - standard deviation
    - mean absolute deviation
    - range
    - interquartile range