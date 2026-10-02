# Acetone Boiling Point and Heater Energy Calculation

## Description

This project calculates the boiling temperature of pure acetone
as a function of pressure and estimates the energy required to heat
and vaporize the acetone stream.

## Process Data

- Acetone feed: 38 kg/h
- Inlet temperature: 10 °C
- Inlet pressure: 1 atm
- Fraction sent to the heater: 60 %
- Heater flow rate: 22.8 kg/h
- Pressure range: 0.1 - 3 atm
- Number of pressure points: 25

## Method

The boiling temperature of pure acetone is calculated using the
Antoine equation:

log10(P) = A - B / (T + C)

where:

- P is the vapor pressure in bar
- T is the temperature in K

For acetone:

A = 4.42448
B = 1312.253
C = -32.445

The energy required by the heater is calculated as:

Q_total = Q_sensible + Q_vaporization

where:

Q_sensible = m × Cp × (T_eb - T_in)

Q_vaporization = m × ΔHvap

## Results

At 1 atm, the program calculates the boiling temperature of acetone
and the energy required to heat and vaporize the 60 % stream.

The program also calculates 25 points between 0.1 atm and 3 atm
and plots the boiling temperature as a function of pressure.

## How to Run

Install the required Python packages:

pip install -r requirements.txt

Then run:

python acetone_boiling.py