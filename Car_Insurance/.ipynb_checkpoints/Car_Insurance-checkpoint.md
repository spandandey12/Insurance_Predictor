# Car Insurance Premium Predictor - Documentation

This document explains how the **car_insurance** sub-package works inside the Insurance Premium Predictor. It describers all modules, functions, classes, and how they compute the final car insurance premium.

Insurance_Premium_Predictor/Car_Insurance/preprocessing.py/training.py/init.py

# Module: `preprocessing.py`

This module calculates all **individual risk multipliers** used for pricing car insurance. 

## **1. `age_factor(age)`**
Returns a multiplier based on the driver's age.

- 'Age_Multipliers' calculated from some the data
- 'Unknown age return **1.0**

## **2. `mileage_factor(annual_km)`**
Returns a multiplier based on the yearly mileage.

- Converts km to thousands using 'round(annual_km / 1000)'
- Unknown mileage returns **1.0**

## **3. `car_age_factor(car_age)`**
Returns a multiplier based on vehicle age.

- 'Car_Age_Multiplier' calculated from the data
- Unknown car age returns **1.0**

## **4. `experience_factor(year_driving)`**
Returns a multiplier based on driving experience.

- More years = lower risk
- Unknown values return **1.0**

## **5. `accident_factor(num_accident)`**
Returns a multiplier based on past accidents.

- Discount comes with less accident
- Higher multiplier with more accidents

## **6. `combined_factors(...)`**
Combines all risk factors into a single risk score.

# Module: `training.py`

## **Class: `Insurance` (Parent)**
- `__init__(base_cost)` -> Initiaizes base premium from dataset mean.
- `yearly_premium()` -> Returns the unadjusted base premium

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
Used to compute combined_factors * vehicle_type_factor

### **3. `final_premium(...)`**
Used to compute base_cost * total_risk

### **4. `quote_display(...)`**
Used to display all the data.

