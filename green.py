def calculate_green_bond_investment():
 print("\n--- Welcome to the Sustainable Finance Calculator ---")

# 1. User Inputs
 investment = float(input("Enter amount to invest ($): "))
 years = int(input("Enter investment duration (years): "))

# 2. Sustainable Finance Metrics
 interest_rate = 0.045
 co2_saved_per_dollar = 0.5

# 3. Calculations
 total_interest = investment * interest_rate * years
 total_payout = investment + total_interest
 total_co2_saved = investment * co2_saved_per_dollar * years
 co2_in_tons = total_co2_saved / 1000

# 4. Display Results
 print("\n================ INVESTMENT REPORT ================")
 print(f"Initial Investment: ${investment:,.2f}")
 print(f"Total Interest Earned: ${total_interest:,.2f}")
 print(f"Total Portfolio Value: ${total_payout:,.2f}")
 print("---------------------------------------------------")
 print(f"🌍 Environmental Impact: You prevented {co2_in_tons:.2f} metric tons of CO2!")
 print(f"💡 Equivalent to planting {int(co2_in_tons * 45)} mature trees.")
 print("===================================================\n")

calculate_green_bond_investment()
