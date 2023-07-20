import pandas as pd  
import matplotlib.pyplot as plt  
dataset = pd.read_csv("tips.csv")  
plt.scatter(dataset['total_bill'], dataset['tip'])  
plt.title("This is Scatter Plot")  
plt.xlabel('Total_bill')  
plt.ylabel('Tip')  
plt.show()  
