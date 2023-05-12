"""
Tyler Spring
Lab 3
SDEV 300
"""
# Import statements needed to display image and bar chart
import os
import sys
from matplotlib import pyplot as plt
import matplotlib.image as mpimg


# List of all the states, capitals, population number, and state flower
list_States = [['Alabama', 'Montgomery', 4918689, 'Camellia'],
               ['Alaska', 'Juneau', 727951, 'Forget Me Not'],
               ['Arizona', 'Phoenix', 7399410, 'Saguaro Cactus Blossom'],
               ['Arkansas', 'Little Rock', 3025875, 'Apple Blossom'],
               ['California', 'Sacramento', 39562858, 'California Poppy'],
               ['Colorado', 'Denver', 5826185, 'White and Lavender Columbine'],
               ['Connecticut', 'Hartford', 3559054, 'Mountain Laurel'],
               ['Delaware', 'Dover', 982049, 'Peach Blossom'],
               ['Florida', 'Tallahassee', 21711157, 'Orange Blossom'],
               ['Georgia', 'Atlanta', 10723715, 'Cherokee Rose'],
               ['Hawaii', 'Honolulu', 1411151, 'Hibiscus'],
               ['Idaho', 'Boise', 1823594, 'Syringa'],
               ['Illinois', 'Springfield', 12620571, 'Purple Violet'],
               ['Indiana', 'Indianapolis', 6768941, 'Peony'],
               ['Iowa', 'Des Moines', 3161522, 'Wild Prairie Rose'],
               ['Kansas', 'Topeka', 2915269, 'Sunflower'],
               ['Kentucky', 'Frankfort', 4474193, 'Goldenrod'],
               ['Louisiana', 'Baton Rouge', 4637898, 'Magnolia'],
               ['Maine', 'Augusta', 1349367, 'White Pine Cone and Tassel'],
               ['Maryland', 'Annapolis', 6055558, 'Black-Eyed Susan'],
               ['Massachusetts', 'Boston', 6902371, 'Mayflower'],
               ['Michigan', 'Lansing', 9989642, 'Apple Blossom'],
               ['Minnesota', 'Saint Paul', 5673015, 'Pink and White Lady Slipper'],
               ['Mississippi', 'Jackson', 2971278, 'Magnolia'],
               ['Missouri', 'Jefferson City', 6153233, 'White Hawthorn Blossom'],
               ['Montana', 'Helena', 1076891, 'Bitterroot'],
               ['Nebraska', 'Lincoln', 1943202, 'Goldenrod'],
               ['Nevada', 'Carson City', 3132971, 'Sagebrush'],
               ['New Hampshire', 'Concord', 1365957, 'Purple Lilac'],
               ['New Jersey', 'Trenton', 8878355, 'Violet'],
               ['New Mexico', 'Santa Fe', 2100917, 'Yucca Flower'],
               ['New York', 'Albany', 19376771, 'Rose'],
               ['North Carolina', 'Raleigh', 10594553, 'Dogwood'],
               ['Ohio', ' Columbus', 11701859, 'Scarlet Carnation'],
               ['Oklahoma', 'Oklahoma City', 3973707, 'Mistletoe'],
               ['Oregon', 'Salem', 4253588, 'Oregon Grape'],
               ['Pennsylvania', 'Harrisburg', 12803056, 'Mountain Laurel'],
               ['Rhode Island', 'Providence', 1060435, 'Violet'],
               ['South Carolina', 'Columbia', 5213272, 'Yellow Jessamine'],
               ['North Dakota', 'Bismarck', 766044, 'Wild Prairie Rose'],
               ['South Dakota', 'Pierre', 890, 620, 'Pasque Flower'],
               ['Tennessee', 'Nashville', 6886717, 'Iris'],
               ['Texas', 'Austin', 29363096, 'Bluebonnet'],
               ['Utah', 'Salt Lake City', 3258366, 'Sego Lily'],
               ['Vermont', 'Montpelier', 623620, 'Red Clover'],
               ['Virginia', 'Richmond', 8569752, 'Dogwood'],
               ['Washington', 'Olympia', 7705917, 'Pink Rhododendron'],
               ['West Virginia', 'Charleston', 1780003, 'Rhododendron'],
               ['Wisconsin', 'Madison', 5837462, 'Wood Violet'],
               ['Wyoming', 'Cheyenne', 579917, 'Indian Paintbrush']]
# How the list is displayed
int_count = 0
while int_count < len(list_States):
    list_States.sort()
    print(list_States[int_count])
    int_count += 1


# The method used to search the list for a user inputted state. Validates input and displays image
def list_search(state):
    """
    List search function
    :rtype: object
    """
    r = 0
    for row in list_States:
        for col in row:
            if state == col:
                print(row)
                plt.imshow(mpimg.imread(col + ".jfif"))
                (os.path.join(sys.path[0] + "\\" + col + ".jfif"))
                print("Close photo of state flower to continue.")
                plt.show()

                return
    if r == 0:
        searcher2 = input("Incorrect. ReEnter.")
        list_search(searcher2)


# Function used to update population count
def popUpdate(value):
    """
    Population updator function
    :rtype: object
    """
    for row in list_States:
        for col in row:
            if value == col:
                int_new_pop = int(input("Enter the new population number."))
                row[2] = int_new_pop
                print(row)
                if int_new_pop < 0:
                    int_new_pop = int(input("Incorrect Value. Enter the new population number."))


# Function used to sort and display populations in bar chart. Did not work very well for me.
def plot():
    """
    plotting function
    :rtype: object
    """
    state_pop = []
    state_name = []
    for i in list_States:
        pop = i[2]
        name = i[0]
        state_pop.append(pop)
        state_name.append(name)
    state_pop.sort(reverse=True)
    state_popped = state_pop[0:5]
    state_name2 = state_name[0:5]

    plt.figure(figsize=(9, 5))
    plt.bar(state_name2, state_popped)

    plt.suptitle('Top 5 populations')
    plt.show()


# Asks user if they would like to update a state's population, if not, exits.
def popMess(valueS1):
    """
    Function that validates to update population
    :rtype: object
    """
    for row in list_States:
        for col in row:
            if valueS1 == col:
                popUpdate(valueS1)
                plot()
                return
    if valueS1 == "no":
        sys.exit()
    else:
        valueS1 = input("Incorrect. Enter a state")
        popMess(valueS1)


# Where user inputs for state to be searched
searcher = input("Please enter state that you would like to search.")
list_search(searcher)
# Call for state search after user inputs it
valueS = input("Would you like to update a state's population? If so, enter the state,"
               " if not, enter no.")
popMess(valueS)
