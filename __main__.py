import sys
import argparse
from functions import grouping_by_state, clean_data
from raw_data import raw_df

DF = clean_data(raw_df)

def main():

    parser = argparse.ArgumentParser(
        description="Analyze frequency of word in hearings per day, or analyze top 5 words and top 5 2-grams of all times "
    )
    parser.add_argument(
        "-s",
        "--state",
        type=str,
        default = "us",
        help="Use us for national results or <State Abbreviation> with capital letter"
    )
    
    parser.add_argument(
        "-n",
        "--top_n",
        type= int,
        default = 10,
        help="Analyze top companies that most required H1B visas"
    )

    try:
        args = parser.parse_args()
    except:
        print("Must indicate --word <word> or --all not both")
        sys.exit(0)



    df = grouping_by_state(DF, args.state, args.top_n)
    
    print(df)
main()
    

    
