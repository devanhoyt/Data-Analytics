#Libraries
import numpy as np
import pandas as pd
import csv
from matplotlib import pyplot as plt

#Question: Do newer lego sets have more parts than older ones?
#Question: What theme has the most parts?
#Question: Which star wars set has the most parts?


#Function that populates the graph for lego parts over the years
def lego_year():
        sets = pd.read_csv("sets.csv", usecols= ["name", "year", "num_parts"])
        plt.style.use('seaborn')
        plt.title("Lego sets throughout the years(1950-2017)")
        plt.xlabel("Year")
        plt.ylabel("Number of parts")
        plt.axis([1950, 2020, 0, 6000] )
        plt.scatter(sets.year, sets.num_parts)
        plt.tight_layout()
        plt.show()


# function that populates the graph for lego theme's by id and parts per set
def themes():
        the_themes = pd.read_csv("sets.csv", usecols= ["name", "year",'theme_id', "num_parts"])
        plt.style.use('seaborn')
        plt.title("Lego sets throughout the years(1950-2017)")
        plt.xlabel("Theme ID")
        plt.ylabel("Number of parts")
        plt.scatter(the_themes.theme_id, the_themes.num_parts)
        plt.show()

        # function that populates the graph for star wars specific sets and how many parts they have
def starwars():
        starwars_sets = pd.read_csv("sets.csv", usecols= ["name", "year",'theme_id', "num_parts"])
        starwars_themes = starwars_sets[starwars_sets.theme_id.eq(range(158, 185))]
        plt.style.use('seaborn')
        plt.title("Star wars Lego sets")
        plt.xlabel("Theme ID")
        plt.ylabel("Number of parts")
        #print(starwars_themes)
        plt.scatter(starwars_themes, starwars_sets.num_parts)
        plt.show()

        
        #Main to run everything
def main():
        choice = input("What would you like to know? 1 = lego throughout the years, 2 = theme_id total parts lookup, 3 = star wars lego information ")
        sets = pd.read_csv("sets.csv", usecols= ["name", "year", "num_parts"])

        #Checks to see which choice was selected and will put out the corresponding graph.
        if choice == "1":
                lego_year()
        elif choice == '2':
                themes()
        elif choice == '3':
                starwars()
        else:
                print("there was an error with your choice. Try again!")
                main()




main()
