import streamlit as st
import pandas as pd
from scripts.functions import grouping_by_state, clean_data
from scripts.functions import grouping_by_industry, grouping_by_company
from scripts.raw_data import raw_df

st.set_page_config(page_title="H1-B Dashboard", layout="wide")
# Clean the raw data once
DF = clean_data(raw_df)

# Streamlit UI
st.title("🔍 H1-B Top Employers Explorer (Fiscal Year 2024)")

st.sidebar.header("Apply Filters")

# Filters
state = st.sidebar.text_input("State abbreviation (e.g., CA, NY) (0 for all):", "0").upper()
industry = st.sidebar.text_input("Industry keyword: (0 for all)", "0").capitalize()
company_name = st.sidebar.text_input("Company name keyword: (0 for all)", "0").capitalize()
number = st.sidebar.number_input("Number of records to display:", min_value=1, max_value=1000, value=50, step=1)

# Data filtering pipeline
try:
    filtered_by_state = grouping_by_state(DF, state, 100000)
    filtered_by_industry = grouping_by_industry(filtered_by_state, industry, 100000)
    final_df = grouping_by_company(filtered_by_industry, company_name, number)
    final_df = final_df.reset_index(drop=True)
    final_df.index += 1  # Make it start at 1 instead of 0

    if final_df.empty:
        st.warning("⚠️ No results found with the given filters.")
    else:
        st.success(f"Showing top {min(len(final_df), number)} results")
        st.dataframe(final_df, use_container_width=True)
        st.markdown("""
            ---  
            ### ℹ️ How to read this table:

            - **Approval Rate**: Ratio of approved requests to requests of the employer
            - **Requests/Total**: Ratio of requests of the employer compared to total requests according to the specified filters
                    
            ---
            ###### Original Database:
            - US Citizenship and Inmigration Services (https://www.uscis.gov/tools/reports-and-studies/h-1b-employer-data-hub)""")
        

except Exception as e:
    st.error(f"An error occurred during filtering: {e}")
