import requests
from bs4 import BeautifulSoup


def extract_ircc(URL):
    ircc = []
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "html.parser")
    table = soup.find('table', attrs={'class': "table table-md table-striped text-center"})
    for row in table.find_all('tr'):
        columns = row.find_all("td")
        if columns:
            ircc.append(f"{columns[0].text}   {columns[1].text}\n")
    ircc.reverse()
    return ircc




URL = "https://www.cursbnr.ro/ircc"



with open ('data.txt','r+') as file:
    last_line = file.readlines()[-1]
    date = last_line.split("  ")[0]
    while True:
        print(f"Ultima data la care IRCC a fost extras este: {date}")
        option = input("Daca doriti extragerea datelor curente apasati orice tasta, altfel apasati n:  ")
        if option.lower() == 'n':
            break
        else:
            ircc = extract_ircc(URL)
            index = [index for index, s in enumerate(ircc) if date in s]
            if index:
                ircc_add = ircc[index[0] + 1:]
                for line in ircc_add:
                    file.write(line)
            break
