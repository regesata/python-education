"""Module creates csv file for DB filling"""
import csv

with open("p_customers.csv", "w", encoding="UTF-8") as f:
    writer = csv.writer(f)
    name = "Uris"
    surname = "OakFoot"
    second_name = "StoneHead"
    email_pref = "silver"
    email_postf = "@deepmine.com"
    city = "city "
    id = 1
    for ind in range(17, 20):
        for _ in range(10):
            tmp_lst = []
            tmp_lst.append(id)
            tmp_lst.append(email_pref + str(id) + email_postf)
            tmp_lst.append(name+str(id))
            tmp_lst.append(surname + str(id))
            tmp_lst.append((second_name + str(id)))
            tmp_lst.append(city + str(ind))
            id += 1
            writer.writerow(tmp_lst)
