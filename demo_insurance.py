from Car_Insurance import (
    age_factor,
    mileage_factor,
    car_age_factor,
    experience_factor,
    accident_factor,
    combined_factors,
    CarInsurance,
    result
)

def main():

    print("\n============================")
    print(" CAR INSURANCE DEMO SCRIPT")
    print("============================\n")

    print("Individual Risk Factors:")
    print("-----------------------------")
    
    age = 25
    annual_km = 15000
    car_age = 3
    exp_years = 5
    num_accidents = 0

    print(f"Age factor ({age} years):", age_factor(age))
    print(f"Mileage factor ({annual_km} km/year):", mileage_factor(annual_km))
    print(f"Car age factor ({car_age} years):", car_age_factor(car_age))
    print(f"Experience factor ({exp_years} years):", experience_factor(exp_years))
    print(f"Accident factor ({num_accidents} accidents):", accident_factor(num_accidents))

    combined = combined_factors(age, annual_km, car_age, exp_years, num_accidents)
    print("Combined risk multiplier:", combined)

    print("\n Using CarInsurance Class:")
    print("-------------------------------")

    model = CarInsurance()
    premium = model.final_premium(
        age=age,
        annual_km=annual_km,
        car_age=car_age,
        exp_years=exp_years,
        num_accidents=num_accidents,
        vehicle_type="suv",
    )

    print(f"Final premium (vehicle='suv'):", premium)

    
    print("\n Using the result() Helper Function:")
    print("----------------------------------------")

    quick_premium = result(22, 12000, 4, 1, 0, "sedan")
    
    print("Quick premium for driver age 22, sedan:", quick_premium)


if __name__ == "__main__":
    main()