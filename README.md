# H1-B Sponsors Search:

Being an international student is hard. Besides having to study in a foreing language, most of us need to create a new network to find a job or intership, while there are many companies that don't sponsor international people.

To make life easier to international students, I developed a seamless tool to find the companies that sponsor H1-B visas for international students. You can search by State, Industry and company name.

## How to run run this project? :arrow_forward:

1. [Install UV to Local Machine](https://docs.astral.sh/uv/getting-started/installation/)

2. Clone the Project
```bash
git clone git@github.com:aep5142/H1B-Analysis.git
```

3. Install Virtual Environment and Dependencies
```bash
uv sync
```

4. Run the application

```bash
uv run python -m scripts
```

## Data Sources :computer:

### Data Source #1: Zillow - Marketplace for housing [US Citizenship and Inmigration Services](https://www.uscis.gov/tools/reports-and-studies/h-1b-employer-data-hub)

Database posted by this federal agency for 2024 granted visas.

### Data Source #2: Community Data Snapshots 2024 from the Chicago Metropolitan Agency for Planning [CMAP](https://datahub.cmap.illinois.gov/datasets/CMAPGIS::community-data-snapshots-2024/explore?layer=0)

The Community Data Snapshots (CDS) project collects a variety of demographic, housing, employment, land use, and other data for northeastern Illinois. These tables contain information for counties, municipalities, and Chicago community areas (CCAs). The primary source is data from the U.S. Census Bureau’s 2022 American Community Survey program.

### Data Source #3: Livability Index from American Association of Retired Persons [AARP](https://livabilityindex.aarp.org/search/Chicago,%20Illinois,%20United%20States)

The AARP Livability Index is created from more than 50 unique sources of data across the seven livability categories. Using these metrics and policies, the AARP Livability Index scores communities by looking at how livable each neighborhood is within the community. The categories each provide important pieces of the picture of livability in a community: Housing, Neighborhood characteristics, Transportation, Environment, Health, Engagement and Opportunities.

## Scraping Details :computer:

Requesting data from Zillow requires to update the headers form the website.
Last update 03.09.2025

Once you have valid headers, we include a script to regularly scrape data from Zillow. Although we scraped listings by zipcode. Each zipcode may include its own scraper for listings that cointaing multiple apparments and prices. 

Update the listings database using uv run python -m extracting/zillow.py . This will scrape all zipcodes from Chicago and update the data in Zillow.csv file

## Testing ✅

There are tests associated with key functionalities of the program. These ones are: test_cmap.py, test_livability.py, test_utils.py, test_utilsapp.py, test_zillow_details.py, test_zillow.py.

To run these tests run the following command:

```bash
uv run pytest tests/<test_to_run>
```

## Final Thoughts

CAPP 122 Instructor - James Turk

CAPP 122 Project TA - Stacey George

[^1]: https://www.illinoispolicy.org/press-releases/housing-unaffordability-on-the-rise-one-third-of-illinoisans-pay-over-30-of-their-income-on-housing/
