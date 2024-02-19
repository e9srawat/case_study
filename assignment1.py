"""
Case Study
"""
import csv


def open_read(file, settlement_point):
    """
    return file contents
    """
    with open(file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [i for i in reader if i["Settlement Point"] == settlement_point]


def open_write(file, dam, rtm, intervals=None):
    """
    write file
    """
    with open(file, "w", encoding="utf-8") as f:
        fieldnames = ["date", "dam", "rtm"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for i in zip(dam, rtm):
            date = i[0]["\ufeffDelivery Date"]
            yyyy = date[-4:]
            mm = date[:2]
            dd = date[3:5]
            hour = f"0{int(i[0]['Delivery Hour'])-1}"[-2:]
            if intervals:
                date = (
                    f"{yyyy}-{mm}-{dd} {hour}:{intervals[i[1]['Delivery Interval']]}:00"
                )
            else:
                date = f"{yyyy}-{mm}-{dd} {hour}:00:00"
            writer.writerow(
                {
                    "date": date,
                    "dam": i[0]["Settlement Point Price"],
                    "rtm": i[1]["Settlement Point Price"],
                }
            )


def task_1():
    """
    task 1
    """
    hb_north_dam = open_read("DAM_Prices_2022.csv", "HB_NORTH")
    hb_north_rtm = open_read("RTM_Prices_2022.csv", "HB_NORTH")
    for i in range(0, len(hb_north_rtm), 4):
        price = (
            float(hb_north_rtm[i]["Settlement Point Price"])
            + float(hb_north_rtm[i + 1]["Settlement Point Price"])
            + float(hb_north_rtm[i + 2]["Settlement Point Price"])
            + float(hb_north_rtm[i + 3]["Settlement Point Price"])
        ) / 4
        hb_north_rtm[i]["Settlement Point Price"] = str(price)[
            : str(price).index(".") + 3
        ]
    hb_north_rtm_hourly = [i for i in hb_north_rtm if int(i["Delivery Interval"]) == 1]
    open_write("task_1.csv", hb_north_dam, hb_north_rtm_hourly)


def task_2():
    """
    task 2
    """
    hb_north_dam = open_read("DAM_Prices_2022.csv", "HB_NORTH")
    hb_north_rtm = open_read("RTM_Prices_2022.csv", "HB_NORTH")
    hb_north_dam_15 = []
    for i in hb_north_dam:
        hb_north_dam_15.append(i)
        hb_north_dam_15.append(i)
        hb_north_dam_15.append(i)
        hb_north_dam_15.append(i)
    open_write(
        "task_2.csv",
        hb_north_dam_15,
        hb_north_rtm,
        {"1": "00", "2": "15", "3": "30", "4": "45"},
    )

task_1()
task_2()