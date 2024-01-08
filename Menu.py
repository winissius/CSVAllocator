import Excel
import dataCSV
from Tools import merge_dictionaries

while True:
    opt = int(input("IMPORTATION ALLOCATOR MENU:\n"
                    "1 - Select your Bank\n"
                    "2 - Expenses classification\n"
                    "3 - Logout\n"))
    if opt == 1:
        bankOpt = ""
        dataImp = {}
        while bankOpt != 0:
            bankOpt = int(input("   1 - XP Investments\n"
                                "   2 - Nubank\n"
                                "   0 - Cancel\n"))
            if bankOpt == 1:
                bankArq = input("Entre com o arquivo do seu banco\n")
                bank = "XP"
                dataXP = dataCSV.data_creation(bank, bankArq)
                dataImp = merge_dictionaries(dataXP, dataImp)
            if bankOpt == 2:
                bankArq = input("Entre com o arquivo do seu banco\n")
                bank = "Nubank"
                dataNubank = dataCSV.data_creation(bank, bankArq)
                dataImp = merge_dictionaries(dataNubank, dataImp)
            if bankOpt == 0:
                break
    if opt == 2:
        answer = ""
        Classification = []
        while answer != 'n':
            expenseClassification = str(input("Enter the classification\n")).title()
            Classification.append((expenseClassification))
            answer = str(input('Would you like to continue [S/N]'))
            dataClassification = {'Classification': Classification}
            print(dataClassification)
            Excel.enterClassificaton(dataClassification)
    if opt == 3:
        print('Thank you')
        Excel.allocate_excel(dataImp)
        break
