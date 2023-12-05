import random as rand
from datetime import datetime, timedelta
import string

def createReceipt():
	toReturn = ""
	with open("givennames.csv") as fname:
		fnames = [i.strip().split(",") for i in fname.readlines() if i.strip()!=""]

	with open("surnames.csv") as lname:
		lnames = [i.strip() for i in lname.readlines() if i.strip()!=""]

	with open("items.csv") as item:
		items = [i.strip() for i in item.readlines() if i.strip()!=""]

	with open("countries.csv") as country:
		states = [i.strip().split(",",1)[1] for i in country.readlines() if i.strip()!=""]


	itemsNum = rand.randint(1,15)
	toReturn += "=====START TRANSACTION=====\n\n"

	delta = datetime(2023,11,28) - datetime(2023,1,1)
	int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
	random_second = rand.randrange(int_delta)
	time = datetime(2023,1,1) + timedelta(seconds=random_second)
	toReturn += "TIME: {}\n".format(time)
	

	toReturn += "CUSTOMER: {} {}\n\n".format(
									fnames[rand.randrange(len(fnames))][rand.randrange(2)],
									lnames[rand.randrange(len(lnames))]
									)
	total_tax = 0
	max_item_len = 0
	itemsLis = []
	prices = []
	taxes = []
	for i in range(itemsNum):
		price = round(rand.random()*50,2)
		prices.append(price)
		tax = round(price * rand.random()*.3 if rand.randint(1,4)==1 else 0,2)
		taxes.append(tax)
		itemsLis.append(items[rand.randrange(len(items))])
		total_tax += tax
		if len(itemsLis[-1])>max_item_len: max_item_len=len(itemsLis[-1])
	toReturn += "ITEM{}PRICE\n".format("".join(" " for i in range(max_item_len-2)))
	for i in range(len(itemsLis)):
		toReturn += "{}{}{:05.2f}  {}\n".format(
									itemsLis[i],
									"".join(" " for i in range(max_item_len-len(itemsLis[i])+2)),
									prices[i],
									"N" if taxes[i]==0 else "T"
									)
	toReturn += "".join("-" for i in range(max_item_len+2+5+3))+"\n"
	subtotal = round(sum(prices),2)
	toReturn += "Subtotal{}{:05.2f}\n".format(
								"".join(" " for i in range(max_item_len-7 if subtotal >= 100 else max_item_len-6)),
								subtotal
								)
	toReturn += "Tax{}{:05.2f}\n".format(
								"".join(" " for i in range(max_item_len-2 if total_tax >= 100 else max_item_len-1)),
								total_tax
								)
	toReturn += "".join("-" for i in range(max_item_len+2+5+3))+"\n"
	total = subtotal+total_tax
	toReturn += "Total{}{:05.2f}\n".format(
								"".join(" " for i in range(max_item_len-4 if total >= 100 else max_item_len-3)),
								total
								)
	toReturn += "\nORDER "
	fate = "PICKED UP IN STORE" if rand.randint(1,5)!=1 else "DELIVERED TO CUSTOMER IN {}" 
	toReturn += fate.format(states[rand.randrange(len(states))].upper())+"\n"
	toReturn += "\n=====CLOSE TRANSACTION=====\n"
	return toReturn

def createName():
	toReturn = ""
	for i in range(16):
		toReturn += rand.choice(string.ascii_uppercase + string.digits)
	return toReturn

for i in range(1000):
	with open(createName()+".txt",'w') as fi:
		fi.write(createReceipt())
