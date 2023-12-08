# Basic Tax Calculator: Depending on the user's income, calculate the tax owed based on predefined income
# brackets and corresponding tax rates. (измисли 4 граници на доход - без данъц, леки данъци, етс.)
# income1 <= 18484 lv >> tax 9% 

# income2 <= 29780 lv >> tax 12%

# income3 <=39904 lv tax >> tax 18%

# income4 <= 51785 lv tax >> tax 22%

# income5 > 51785 lv tax >> 27 %

def tax_calculator(income_lv):
    if income_lv <= 18484:
        withHolding_tax1 = income_lv - (income_lv * 0.09)
        owed_taxes1 = (income_lv * 0.09)
        return f"your net salary is {withHolding_tax1} and owed taxes {owed_taxes1}"
    
    elif income_lv <= 29780:
        withHolding_tax2 = income_lv - (income_lv * 0.12)
        owed_taxes2 = (income_lv * 0.12)
        return f"your net salary is  {withHolding_tax2} and owed taxes {owed_taxes2}"
    
    elif income_lv <= 39904:
        withHolding_tax3 = income_lv - (income_lv * 0.18)
        owed_taxes3 =  (income_lv * 0.18)
        return f"your net salary is {withHolding_tax3} and owed taxes {owed_taxes3}"
    
    elif income_lv <= 51785:
        withHolding_tax4 = income_lv - (income_lv * 0.22)
        owed_taxes4 =  (income_lv * 0.22)
        return f"your net salary is {withHolding_tax4} and owed taxes {owed_taxes4}"
    
    else:
        withHolding_tax5 = income_lv - (income_lv * 0.27)
        owed_taxes5 = (income_lv * 0.27)
        return f"your net salary is {withHolding_tax5} and owed taxes {owed_taxes5}"
        
insertion = int(input("enter here your salary:"))
verdict = tax_calculator(insertion)
print(verdict)     