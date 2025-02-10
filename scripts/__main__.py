import sys
import argparse
from scripts.functions import grouping_by_state, clean_data
from scripts.functions import grouping_by_industry, grouping_by_company
from scripts.raw_data import raw_df

allowed_numbers= "1234567890"
DF = clean_data(raw_df)

def main():

    print("WELCOME TO THE TOP H1-B EMPLOYERS SEARCH ACCORDING TO YOUR FILTERS")

    state = input("Sect the State in abbrevation form (0 for all): ")
    state = state.upper()
    industry = input("Select keyword for industry (0 for all): ")
    industry = industry.capitalize()

    company_name = input("Select word for company name (0 for no filter): ")
    company_name = company_name.capitalize()

    number = input("How many records you want to see?: ")
    try:
        number = int(number)
    except ValueError:
        print("You need to enter a valid number. Goodbye!")
        sys.exit(0)
    state_df = grouping_by_state(DF, state, 100000)
    industry_df = grouping_by_industry(state_df, industry, 100000)
    company_df = grouping_by_company(industry_df, company_name, number)

    print(company_df)
        
    print("Thanks for coming, bye!")
    sys.exit(0)


main()
    

    
