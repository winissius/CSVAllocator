import pandas as pd
from BasicData import month
#from dataCSV import description, value


def allocate_excel(data):
    '''data = {'Description': description,
             'Value [R$]': value}'''
    dataFrame = pd.DataFrame(data)

    # dataFrame.to_excel('expenses.xlsx', sheet_name=month, index=False, header=False)

    '''filename = 'expenses.xlsx'
    writer = pd.ExcelWriter(filename, engine="openpyxl", mode="a", if_sheet_exists="overlay")
    dataFrame.to_excel(writer, index=False)'''

    with pd.ExcelWriter('expenses.xlsx', mode='a', if_sheet_exists="overlay") as writer:
        dataFrame.to_excel(writer, sheet_name=month, index=False, header=False)



def enterClassificaton(data):
    dataFrame = pd.DataFrame(data)
    with pd.ExcelWriter('expenses.xlsx', mode='a', if_sheet_exists="overlay") as writer:
        dataFrame.to_excel(writer, sheet_name="Classification", index=False, header=False)