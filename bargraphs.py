#Pandas for connecting to database
#Matplotlib for actually drawing charts like in R

# Pandas for reading CSV
# Matplotlib for drawing graphs
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as mpt

def generate_bar():
    print("Bar graph function start ho chuka hai")
    # Read dataset
    dataframe = pd.read_csv("2015.csv")

    # Factors to plot
    factors = [
        "Economy (GDP per Capita)",
        "Family",
        "Health (Life Expectancy)",
        "Freedom",
        "Trust (Government Corruption)",
        "Generosity",
        "Dystopia Residual"
    ]

    # Function to create one bar graph
    def create_bar_graph(country_name, output_file):

        country = dataframe[dataframe["Country"] == country_name]

        values = [country[col].values[0] for col in factors]

        mpt.figure(figsize=(10, 5))

        mpt.bar(factors, values)

        mpt.xticks(rotation=45, ha="right")
        mpt.xlabel("Happiness Factors")
        mpt.ylabel("Score")
        mpt.title(f"{country_name} Happiness Factors")

        mpt.tight_layout()

        mpt.savefig(f"static/{output_file}")

        mpt.close()

    # Generate all graphs
    create_bar_graph("India", "bargraph1.png")
    create_bar_graph("Israel", "bargraph2.png")
    create_bar_graph("Iceland", "bargraph3.png")