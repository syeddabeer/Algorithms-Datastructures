import matplotlib.pyplot as plt
# %matplotlib inline


data.plot();
data.plot(kind='bar', color='red', figsize=(5,5));
data.plot(kind='barh');
data.plot(kind='pie', colormap='Pastel1');



# seaborn basic plotting
import seaborn as sns
sns.countplot(x='Medal', data=df, hue='categoricalVariable')
sns.countplot(x='Medal', data=df, hue='Gender')