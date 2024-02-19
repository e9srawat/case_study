import csv


dam_path = "DAM_Prices_2022.csv"
rtm_path = "RTM_Prices_2022.csv"
with open(dam_path, 'r') as f:
    reader = csv.DictReader(f)
    hb_north_dam=[i for i in reader  if i['Settlement Point']=='HB_NORTH']

with open(rtm_path, 'r') as f:
    reader = csv.DictReader(f)
    hb_north_rtm=[i for i in reader if i['Settlement Point']=='HB_NORTH']

for i in range(0,len(hb_north_rtm),4):
    price = (float(hb_north_rtm[i]['Settlement Point Price'])+float(hb_north_rtm[i+1]['Settlement Point Price'])+float(hb_north_rtm[i+2]['Settlement Point Price'])+float(hb_north_rtm[i+3]['Settlement Point Price']))/4
    hb_north_rtm[i]['Settlement Point Price'] = str(price)[:str(price).index('.')+3]
    
hb_north_rtm_hourly = [i for i in hb_north_rtm if int(i['Delivery Interval'])==1]    

with open("/home/fenix/Documents/Assignments/Project2/task_1.csv", 'w') as f:
    fieldnames = ['date', 'dam', 'rtm']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in zip(hb_north_dam, hb_north_rtm_hourly):
        date = i[0]['\ufeffDelivery Date']
        yyyy = date[-4:]
        mm = date[:2]
        dd=date[3:5]
        writer.writerow({'date': f"{yyyy}-{mm}-{dd} {int(i[0]['Delivery Hour'])-1}:00:00", 'dam': i[0]['Settlement Point Price'], 'rtm':i[1]['Settlement Point Price']})

with open(rtm_path, 'r') as f:
    reader = csv.DictReader(f)
    hb_north_rtm=[i for i in reader if i['Settlement Point']=='HB_NORTH']
    
hb_north_dam_15 = [] 
for i in hb_north_dam:
    hb_north_dam_15.append(i)
    hb_north_dam_15.append(i)
    hb_north_dam_15.append(i)
    hb_north_dam_15.append(i)
 
with open("/home/fenix/Documents/Assignments/Project2/task_2.csv", 'w') as f:
    fieldnames = ['date', 'dam', 'rtm']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in zip(hb_north_dam_15, hb_north_rtm):
        date = i[0]['\ufeffDelivery Date']
        yyyy = date[-4:]
        mm = date[:2]
        dd=date[3:5]
        intervals = {'1':'00' ,'2':'15' ,'3':'30' ,'4':'45'}
        writer.writerow({'date': f"{yyyy}-{mm}-{dd} {int(i[0]['Delivery Hour'])-1}:{intervals[i[1]['Delivery Interval']]}:00", 'dam': i[0]['Settlement Point Price'], 'rtm':i[1]['Settlement Point Price']})