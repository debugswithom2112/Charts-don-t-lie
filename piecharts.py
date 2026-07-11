import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as mpt


def generate_pie():
    print("Pie chart function start ho chuka hai")
    # Read the dataset
    dataframe = pd.read_csv("2015.csv")

    # Filter data for India
    india = dataframe[dataframe["Country"] == "India"]

    # Labels for pie chart
    labels = [
        "Economy (GDP per Capita)",
        "Family",
        "Health (Life Expectancy)",
        "Freedom",
        "Trust (Government Corruption)",
        "Generosity",
        "Dystopia Residual"
    ]

    # Values corresponding to the labels
    values = [india[label].values[0] for label in labels]

    # Create pie chart
    mpt.figure(figsize=(8, 8))

    mpt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    mpt.title("India Happiness Factors")

    # Save inside the static folder

    mpt.savefig("static/piechart.png")
    mpt.close()

    mpt.close()