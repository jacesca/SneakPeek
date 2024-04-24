import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset('tips')

sns.scatterplot(tips[['total_bill', 'tip', 'size']])
plt.show()