#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
tot = 0
#print (enron_data["PRENTICE JAMES"])
#print(enron_data["LAY KENNETH L"]["total_payments"])
#print(enron_data["SKILLING JEFFREY K"]["total_payments"])
#print(enron_data["FASTOW ANDREW S"]["total_payments"])

for x in enron_data:
	if enron_data[x]["poi"]:
	#if enron_data[x]["total_payments"] == "NaN" and enron_data[x]["poi"]:
	#if enron_data[x]["email_address"] != "NaN":
	#if enron_data[x]["salary"] == "NaN":
		#print(enron_data[x]["salary"])
		tot += 1
print(tot)
print(float(tot)/len(enron_data))