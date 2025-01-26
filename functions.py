import pandas as pd

def splits_industry(df):
    industries = []
    for industry in df["Industry"]:
        if industry != None and type(industry) == str:
            industries.append(industry.split(" - ")[1])
        else:
            industries.append(None)
    df["Industry"] = industries
    return df


def clean_data(df):
    """
    Takes the database and converts strings to float.
    Input:
        - df: pandas dataframe
    """
    columns_to_int = ["Petitioner Zip Code", "Initial Approval",
                      "Continuing Approval"]
    for column in columns_to_int:
        df[column] = pd.to_numeric(df[column], errors='coerce')

    #renaming columns
    change_names = ['Employer (Petitioner) Name',
                  'Industry (NAICS) Code', 'Petitioner City',
                  'Petitioner State', 'Petitioner Zip Code']
    new_names = ["Employer", "Industry", "City", "State", "Zip Code"]
    renaming_dict = {}
    for i, oldname in enumerate(change_names):
        renaming_dict[oldname] = new_names[i]
    df = df.rename(columns = renaming_dict)

    #cleaning industry name
    df = splits_industry(df)
    
    #creating new columns
    quali_columns = ["Employer", "Industry", "City", "State"]
    quanti_columns = ['Initial Approval',
                    'Initial Denial']

    useful_columns = quali_columns + quanti_columns
    df = pd.DataFrame(df[useful_columns])
    df["total_requests"] = df[quanti_columns].sum(axis=1)
    df["approval_rate"] = df["Initial Approval"]/df["total_requests"]
    df = df[df['total_requests'] > 0]
    df = df.drop(columns = quanti_columns, axis=1)

    df["Employer"] = df["Employer"].str.title()
    df["City"] = df["City"].str.title()
    
    return df

def sort_proportion_df(df, top):
    filtered_df = df.sort_values(by= "total_requests",
                                              ascending = False)
    filtered_df["Requests / total (%)"] = filtered_df["total_requests"]/sum(filtered_df["total_requests"]) * 100
    return filtered_df.head(top)

    

def grouping_by_state(df, state = "us", top = 10):
    if state == "us":
        return sort_proportion_df(df, top)
        
    else:
        filtered_df = df[df["State"] == state]
        return sort_proportion_df(filtered_df, top)

    
    
                     
