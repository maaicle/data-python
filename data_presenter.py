# 1 Create a new file called data_presenter.py.

# 2 Open the CupcakeInvoices.csv.
cupcake = open('CupcakeInvoices.csv')

# 3 Loop through all the data and print each row.
# for line in cupcake:
    # print(line)

# 4 Loop through all the data and print the type of cupcakes purchased.
# cupcake.seek(0)
# for line in cupcake:
#     # print(line.strip().split(',')[2])

# # 5 Loop through all the data and print out the total for each invoice 
# # (Note: this data is not provided by the csv, you will need to calculate it. 
# # Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).
# cupcake.seek(0)
# for line in cupcake:
#     qty = int(line.strip().split(',')[3])
#     price = float(line.strip().split(',')[4])
#     # print(round(qty * price, 2))
    

# # 6 Loop through all the data, and print out the total for all invoices combined.
# cupcake.seek(0)
# total = 0
# for line in cupcake:
#     qty = int(line.strip().split(',')[3])
#     price = float(line.strip().split(',')[4])
#     total = total + (qty * price)
# print(round(total))

# 7 Close your open file.
# cupcake.close()


#get totals for cupcakes
# cupcake.seek(0)
total = 0
choc_total = 0
van_total = 0
straw_total = 0
for line in cupcake:
    split_line = line.strip().split(',')
    qty = int(split_line[3])
    price = float(split_line[4])
    total = total + (qty * price)
    if split_line[2] == 'Chocolate':
        choc_total = choc_total + (qty * price)
    elif split_line[2] == 'Vanilla':
        van_total = van_total + (qty * price)
    elif split_line[2] == 'Strawberry':
        straw_total = straw_total + (qty * price)
            
print(round(total), round(choc_total), round(van_total), round(straw_total))


# create graph
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
fig, ax = plt.subplots()
flavors = ['strawberry', 'chocolate', 'vanilla', 'total']
totals = [straw_total, choc_total, van_total, total]
ax.bar(flavors, totals)

plt.show()