"""
Assignment 3
"""
import csv


def tbn(data, n):
    """
    calculates the tbn value of data
    """
    prices = data["price"]
    result =[]
    for _ in range(2):
        max_dif=0
        for i in prices:
            for j in prices[prices.index(i)+1:]:
                if j-i>max_dif:
                    max_dif = j-i
                    t_b=(j,i)
        result.append(t_b)
        for i in t_b:
            prices.remove(i)

    t=[i[0] for i in result]
    b=[i[1] for i in result]
    tbn=str(sum(t)-sum(b))
    return tbn[: tbn.index(".") + 3]

def writer(file, data):
    """
    Writes data to file
    """
    with open(file, "w", encoding="utf-8") as f:
        fieldnames = ["date", "tb2 value"]
        dictwriter = csv.DictWriter(f, fieldnames=fieldnames)
        dictwriter.writeheader()
        for i in data:
            dictwriter.writerow({"date": i["date"], "tb2 value": i["tb2"]})


def answer():
    """
    creates answer csv files
    """
    with open("task_1.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        dam = list(reader)
    day = "01"
    dam_tbn = []
    while int(day) < 32:
        date = f"2022-01-{day[-2:]}"
        dam_dicn = {"date": [], "price": []}
        data = [i for i in dam if date in i["date"]]
        for i in data:
            dam_dicn["date"].append(i["date"])
            dam_dicn["price"].append(float(i["dam"]))
        dam_tbn.append({"date": date, "tb2": tbn(dam_dicn, 2)})
       
        day = "0" + str(int(day) + 1)
    writer("modified_dam_tb2.csv", dam_tbn)
    #writer("rtm_tb2.csv", rtm_tbn)


answer()
