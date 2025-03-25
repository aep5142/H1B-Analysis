import sys
from scripts.functions import grouping_by_state, clean_data
from scripts.functions import grouping_by_industry, grouping_by_company
from scripts.raw_data import raw_df

allowed_numbers= "1234567890"
DF = clean_data(raw_df)

def main():
    while True:
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
            print("Try again entering a valid number")
        state_df = grouping_by_state(DF, state, 100000)
        industry_df = grouping_by_industry(state_df, industry, 100000)
        company_df = grouping_by_company(industry_df, company_name, number)

        if len(company_df) == 0:
            print("Oops! We couldn't find anything with your parameters")
        else:
            print(company_df)
            
        leaving = input("Do you want to make another search? (Y/N): ")
        if leaving.upper() == "N":
            print("Thanks for coming!")
            sys.exit(0)


main()
    

    
