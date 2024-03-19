import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Change the color palette to "RdBu"
sns.set_style("whitegrid")
sns.set_palette("RdBu")

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", 
                  "Often", "Always"]

sns.catplot(x="Parents Advice", 
            data=survey_data, 
            kind="count", 
            order=category_order)

# Show plot
plt.show()
###########################################
# Set the context to "paper"
sns.set_context("paper")


# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Show plot
plt.show()
###########################################
# Set the style to "darkgrid"
sns.set_style("darkgrid")


# Set a custom color palette
color_palette = ['#39A7D0', '#36ADA4']
sns.set_palette(color_palette)
# Create the box plot of age distribution by gender
sns.catplot(x="Gender", y="Age", 
            data=survey_data, kind="box")

# Show plot
plt.show()