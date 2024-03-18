import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot
sns.relplot(data = mpg, x = "model_year", y = "mpg", kind = "line");

# Show plot
plt.show()
########################################

# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line", ci="sd")

# Show plot
plt.show()
########################################
# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None, style="origin", 
            hue="origin", markers = True,
            dashes = False)

# Show plot
plt.show()
