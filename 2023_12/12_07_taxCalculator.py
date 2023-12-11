# Basic Tax Calculator: Depending on the user's income, calculate the tax owed based on predefined income
# brackets and corresponding tax rates. (измисли 4 граници на доход - без данъц, леки данъци, етс.)
# income1 <= 18484 lv >> tax 9% 

# income2 <= 29780 lv >> tax 12%

# income3 <=39904 lv tax >> tax 18%

# income4 <= 51785 lv tax >> tax 22%

# income5 > 51785 lv tax >> 27 %

def tax_calculator(income_lv):
    withHolding_tax = 0
    owed_taxes = 0
    txt = "your net salary and owed taxes in lv are: "
    if income_lv <= 18484:
        withHolding_tax += income_lv - (income_lv * 0.09)
        owed_taxes += (income_lv * 0.09)
        return txt + f"{withHolding_tax:,}" + " and " + f"{owed_taxes:,}"
    
    elif income_lv <= 29780:
        withHolding_tax += income_lv - (income_lv * 0.12)
        owed_taxes += (income_lv * 0.12)
        return txt + f"{withHolding_tax}" + " and " + f"{owed_taxes}"
    
    elif income_lv <= 39904:
        withHolding_tax += income_lv - (income_lv * 0.18)
        owed_taxes +=  (income_lv * 0.18)
        return txt + f"{withHolding_tax}" + " and " + f"{owed_taxes}"
    
    elif income_lv <= 51785:
        withHolding_tax += income_lv - (income_lv * 0.22)
        owed_taxes +=  (income_lv * 0.22)
        return txt + f"{withHolding_tax}" + " and " + f"{owed_taxes}"
    
    else:
        withHolding_tax += income_lv - (income_lv * 0.27)
        owed_taxes += (income_lv * 0.27)
        return txt + f"{withHolding_tax}" + " and " + f"{owed_taxes}"
    
        
insertion = int(input("enter here your salary per year:"))
verdict = tax_calculator(insertion)
print(verdict)

# ZDR kato na koraba - fix repeating, predefine var in begining