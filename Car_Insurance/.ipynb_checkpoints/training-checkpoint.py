"""
training.py
------------------------------------
This module calculates the final car insurance premium by combining all the risk factors present in preprocessing.py. Here we can notice inheritance -> CarInsurance extends the parent class Insurance.
"""
from . import preprocessing
class Insurance:
""" Parent class storing the base_cost. """
    def __init__(self,base_cost=493.74225):
        self.base_cost=base_cost
""" Returns the base premium before risk adjustments. """    
    def yearly_premium(self):
        return self.base_cost
class CarInsurance(Insurance):
""" Child class extending Insurance. """
    Vehicle_Type_Multipliers={
        "sedan": 1.00,
        "suv": 1.05,
        "sports": 1.15,
        "truck": 1.08
    }
    def __init__(self,base_cost=493.74225):
        super().__init__(base_cost)
    
    def vehicle_type_factor(self, vehicle_type):
""" Returns vehicle type multiplier. """
        if vehicle_type is None:
            return 1.0
        return self.Vehicle_Type_Multipliers.get(vehicle_type.lower(), 1.0)
    
    def total_risk(self, age, annual_km, car_age, year_driving, num_accident,vehicle_type=None):
        """ Combining all risk factors. """
        base_risk = preprocessing.combined_factors(age, annual_km, car_age, year_driving, num_accident)
        type_risk = self.vehicle_type_factor(vehicle_type)
        return type_risk*base_risk
    
    def final_premium(self, age, annual_km, car_age, exp_years, num_accidents, vehicle_type=None):
""" base premium × combined risk """
        risk = self.total_risk(age, annual_km, car_age, exp_years, num_accidents, vehicle_type)
        return round(self.base_cost * risk, 2)
    
    def quote_display(self, age, annual_km, car_age, exp_years, num_accidents, vehicle_type=None):
""" Summary """
        premium = self.final_premium(age, annual_km, car_age, exp_years, num_accidents, vehicle_type)
        return (
            f"-----Car Insurance Quote-----\n"
            f"Driver Age: {age}\n"
            f"Years of Experience: {exp_years}\n"
            f"Previous Accidents: {num_accidents}\n"
            f"Annual Mileage: {annual_km} km\n"
            f"Car Age: {car_age} years\n"
            f"Vehicle Type: {vehicle_type if vehicle_type else 'Not provided'}\n\n"
            f"Estimated Car Insurance Premium: ${premium}\n"
            f"--------------------------------"
        )
    