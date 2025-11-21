import pandas as pd

# Read tables from Wikipedia
url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
tables = pd.read_html(url)

# Check how many tables were found
print(f"Found {len(tables)} tables")

# Select the first one
df = tables[0]
print(df.head())