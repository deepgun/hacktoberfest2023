import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# links, reading and stuff
fifa = r'C:\Users\suyash\Desktop\KACHRA\laohub\Smile in Pain\zzz...zzz\Matplotlib\data.csv'
FIFA = pd.read_csv(fifa)

FIFA['Weight'] = [float(str(x).strip('lbs')) for x in FIFA['Weight']]

# CONSTANTS
# You made a blunder here as yu used 'and' a logical operator instead of a '&' a bitwise operator
#COL = ['red', 'blue', 'green']
VLO = FIFA.loc[FIFA['Weight'] <= 130].count()[0]
LOW = FIFA.loc[(130 < FIFA["Weight"]) & (FIFA["Weight"] <= 150)].count()[0]
MED = FIFA.loc[(150 < FIFA["Weight"]) & (FIFA["Weight"] <= 170)].count()[0]
HIG = FIFA.loc[(170 < FIFA["Weight"]) & (FIFA["Weight"] <= 190)].count()[0]
VHI = FIFA.loc[FIFA["Weight"] > 190].count()[0]

LAB = ['very low','low', 'medium', 'high','very high']
EXP = [.2, 0.1, 0, 0, .2]


# Plotting stuff of the program
# GGPLOT is OP
# Explode function is to split the pi chart a bit appert
# pctdistance is the parameter that determines the distance from the centre and is reative
# autopct is to write the percentage
plt.style.use("ggplot")
plt.pie([VLO, LOW, MED, HIG, VHI], labels = LAB, autopct = '%.2f %%', pctdistance = 0.9, explode = EXP)  

# Labels
plt.title("Player Weight")

# Showing
plt.show()
