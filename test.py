# Import the necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

cupcake_invoices = open('CupcakeInvoices.csv')

cupcake = []
for data in cupcake_invoices:
    data = data.strip()
    values = data.split(",")
    first_name, last_name, type, quantity, price = values
    myTuple = (first_name,last_name,type,quantity,price)
    cupcake.append(myTuple)
# print(cupcake)
index = []
for i in range(len(cupcake)):
    index.append(str(i + 1))
# print(index)

cupcake_df = pd.DataFrame(cupcake, columns = ['first_name', 'last_name', 'type', 'quantity', 'price'], index = index)
# print(cupcake_df.shape)
for index in range(cupcake_df.shape[1]):
    columnSeriesObj = cupcake_df.iloc[:, index]
    print('Column Contents: ', columnSeriesObj.values)

# plt.show()