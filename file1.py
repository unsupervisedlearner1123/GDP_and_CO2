import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)

df.head()

df2 = df[
    [
        "Mortality rate, infant (per 1,000 live births)",
        "GDP per capita (constant 2010 US$)",
        "Country Name",
    ]
]

df2.plot(
    x="Mortality rate, infant (per 1,000 live births)",
    y="GDP per capita (constant 2010 US$)",
    kind="bar",
    figsize=(15, 10),
)
