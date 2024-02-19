"""
Assignment 2
"""
import csv


def tbn(data, n):
    """
    calculates the tbn value of data
    """
    bottom_h = []
    top_h = []
    for _ in range(n):
        top_h.append(max(data["price"]))
        bottom_h.append(min(data["price"]))
        data["price"].remove(max(data["price"]))
        data["price"].remove(min(data["price"]))
    result = str(sum(top_h) - sum(bottom_h))
    return result[: result.index(".") + 3]


def answer():
    """
    creates answer csv files
    """
    with open("task_1.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        dam = list(reader)

    day = "01"
    dam_tbn = []
    rtm_tbn = []
    while int(day) < 32:
        date = f"2022-01-{day[-2:]}"
        dam_dicn = {"date": [], "price": []}
        rtm_dicn = {"date": [], "price": []}
        dam_data = [i for i in dam if date in i["date"]]
        for i in dam_data:
            dam_dicn["date"].append(i["date"])
            rtm_dicn["date"].append(i["date"])
            dam_dicn["price"].append(float(i["dam"]))
            rtm_dicn["price"].append(float(i["rtm"]))
        dam_tbn.append({"date": date, "tb2": tbn(dam_dicn, 2)})
        rtm_tbn.append({"date": date, "tb2": tbn(rtm_dicn, 2)})
        day = "0" + str(int(day) + 1)

    with open("dam_tb2.csv", "w", encoding="utf-8") as f:
        fieldnames = ["date", "tb2 value"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for i in dam_tbn:
            writer.writerow({"date": i["date"], "tb2 value": i["tb2"]})

    with open("rtm_tb2.csv", "w", encoding="utf-8") as f:
        fieldnames = ["date", "tb2 value"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for i in rtm_tbn:
            writer.writerow({"date": i["date"], "tb2 value": i["tb2"]})
answer()