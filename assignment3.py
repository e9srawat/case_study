"""
Assignment 3
"""
import csv


def tbn(data, n):
    """
    calculates the tbn value of data
    """
    bottom_h = []
    top_h = []
    index=[]
    temp = data["price"]
    print(data['price'])
    for _ in range(n):
        top_h.append(max(temp))
        index.append(data["price"].index(top_h[-1]))
        temp = [i for i in data["price"] if i not in top_h]
        
    data["price"] = data["price"][:max(index)][1:]
    
    for i in top_h:
        if i in data["price"]:
          data["price"].remove(i)
    
    print(top_h)
    for _ in range(n):
        if data["price"]:
            bottom_h.append(min(data["price"]))
            data["price"].remove(bottom_h[-1])
        else:
            bottom_h.append(0)
    print(bottom_h)
            
    result = str(sum(top_h) - sum(bottom_h))
    return result[: result.index(".") + 3]


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
