#Libraries
import numpy as np
import pandas as pd
import csv
from matplotlib import pyplot as plt

#Questions: Do newer lego sets have more parts than older ones?
#Question: What theme has the most parts?
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
# with open(f'state.csv', 'w', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(['' ])
#         writer.writerows()
# print(Newhamp)
def themes():
        the_themes = pd.read_csv("sets.csv", usecols= ["name", "year",'theme_id', "num_parts"])
        plt.style.use('seaborn')
        plt.title("Lego sets throughout the years(1950-2017)")
        plt.xlabel("Theme ID")
        plt.ylabel("Number of parts")
        plt.scatter(the_themes.theme_id, the_themes.num_parts)
        plt.show()

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

def main():
        choice = input("What would you like to know? 1 = lego throughout the years, 2 = theme_id total parts lookup, 3 = star wars lego information ")
        sets = pd.read_csv("sets.csv", usecols= ["name", "year", "num_parts"])

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