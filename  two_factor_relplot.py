import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Adjust further to add subplots based on family support
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter", 
            col="schoolsup",
            col_order=["yes", "no"],
            row = "famsup",
            row_order = ["yes", "no"])

# Show plot
plt.show()
##############################################
# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg", 
            data=mpg, kind="scatter", 
            size="cylinders",
            hue = "cylinders")

# Show plot
plt.show()
##############################################
# Create a scatter plot of acceleration vs. mpg
sns.relplot(data = mpg, x = "acceleration", y = "mpg", style = "origin", hue = "origin", kind = "scatter")

# Show plot
plt.show()