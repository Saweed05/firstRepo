import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

my_data=pd.read_csv("data02.csv")

sns.set_theme(style="ticks",palette="muted",color_codes=True)
sns.countplot(x="Gender",data=my_data, hue="Location")
plt.title("Data Visualization with Baba_Ammar")
plt.show()
# updated in github to practice pull the code in local directory
