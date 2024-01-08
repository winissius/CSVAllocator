import csv
import locale


def data_creation(bank, bankArq):
    if bank == "XP":
        delimiter = ";"
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    elif bank == "Nubank":
        delimiter = ","
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    else:
        delimiter = ','  # change this for ,

    with open(bankArq, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        counter = 0
        value = []
        description = []

        for line in csv_reader:
            if counter == 0:
                counter += 1
            else:
                description.append(line[1])
                value.append(locale.atof(line[3].replace('R$', '').strip()))

    data = {'Description': description,
            'Value [R$]': value}
    return data
