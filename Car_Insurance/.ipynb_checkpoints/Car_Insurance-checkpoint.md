# Car Insurance Premium Predictor - Documentation

The Car Insurance sub=package is one of the three components of the Insurance_Premium_Predictor package.
Its purpose is to compute a driver's yearly car insurance premium using:

1) Driver related risk factor
2) Vehicle related risk factor
3) A combined multiplier based scoring system
4) A class based design using inheritance

The subpackages consists of two modules:

1) preprocessing.py -> handles all individual risk multipliers
2) training.py -> applies inheritance and computes the final premium

# Module: `preprocessing.py`

This module defines all individual risk factors that contribute to the overall risk score. Each factor converts a real world variable into a numberic multiplier

# Function

## **1. `age_factor(age)`**
Returns a multiplier based on the driver's age.

- 'Age_Multipliers' calculated from some the data
- 'Unknown age return **1.0**
- Younger drivers typically have slightly higher multipliers due to higher risk.

## **2. `mileage_factor(annual_km)`**
Returns a multiplier based on the yearly mileage.

- Converts km to thousands using 'round(annual_km / 1000)'
- Unknown mileage returns **1.0**
- Higher yearly mileage means increased risk

## **3. `car_age_factor(car_age)`**
Returns a multiplier based on vehicle age.

- 'Car_Age_Multiplier' calculated from the data
- Unknown car age returns **1.0**
- Newer vehicle -> slightly lower multiplier
- Older vehicles -> slightly higher multiplier

## **4. `experience_factor(year_driving)`**
Returns a multiplier based on driving experience.

- More years = lower risk
- Unknown values return **1.0**
- First year drivers have highest multipliers

## **5. `accident_factor(num_accident)`**
Returns a multiplier based on past accidents.

- Discount comes with less accident
- Higher multiplier with more accidents

## **6. `combined_factors(...)`**
Combines all risk factors into a single risk score.
The combined value is then used in the premium calculation module.

# Module: `training.py`

The module provides the class-based structure for computing the final premium. It also includes the required inheritance component.

## **Class: `Insurance` (Parent)**

- Stores a base premium (base_cost)
- Provides yearly_premium() method returning the base cost

## **Class: `CarInsurance` (Child Class)**  
Extends the `Insurance` class using inheritance.
CarInsurance package predicts car insurance premiums using real-world risk multipliers from the data.

### Vehicle Type Multipliers
"sedan": 1.00
"suv": 1.05
"sports": 1.15
"truck": 1.08

### **1. `vehicle_type_factor(vehicle_type)`**
Returns the type_base multipliers.
- Converts type to lower case
- Default **1.0** if unknown

### **2. `total_risk(...)`**
Used to compute combined_factors * vehicle_type_factor. combined_factors is from preprocessing.py.

### **3. `final_premium(...)`**
Used to compute base_cost * total_risk. It is rounded to 2 decimals.

### **4. `quote_display(...)`**
Used to display all the data.

### result()
The function allows users to compute a premium in one line.

