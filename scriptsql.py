#This portion of the project was used to create faux data for the use of future projects
import csv
from faker import Faker
import random
from timeit import default_timer as timer ##performance measuring
from random import randrange
#### SETUP #####

#Faker instances
name_faker = Faker(["en-US","fr_FR", "it_IT", "de_DE", "es_CO","de_CH", "de_DE", "es_MX" ])
fake = Faker()

#Timer start for performance testing
start = timer()

#All "base" data will go in here
master_list = []

def get_first_name():
        return name_faker.unique.first_name()

def get_last_name():
        return name_faker.unique.last_name()

def get_address():
        return fake.address()

#### ROGUE DATA ####
#We use this to further increase our ability to see rogue data in 
def rogue_data(lst):
    choice = random.choice(['fname', 'lname', 'address123'])
    if choice == 'fname':
        r_fname = ''
        lst[0] = r_fname
    elif choice == 'lname':
        r_lname = ''
        lst[1] = r_lname
    elif choice == 'address123':
        lst[2] = '123 candy lane'
    
    
    return lst

#### MASTER_LIST_CONSTRUCTOR #####

def construct_master_list(row_count):
    for _ in range(1, row_count):
        row = []

        

        first_name = get_first_name()
        last_name = get_last_name()
        address=get_address()

        row.append(first_name)
        row.append(last_name)
        row.append(address)

        #This goes after all the function calls/value assignments

        master_list.append(row)
def create_csv_data():
        construct_master_list()
        #A simple header for the file
        header = ['first name',
                  'last name', 
                  'address'
                  ]
        
        with open('order_data.csv', 'w', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                # write the header
                writer.writerow(header)
                random_order = []
                #I have decided to write this to a file 15000 times
                random_total = 15000
                for n in range(0, random_total):
                        
                        #Randomly generate a user from master list
                        random_user = random.choice(master_list)
                        userfname = random_user[0]
                        userlname = random_user[1]
                        useraddress = random_user[2]
                        
                        random_order = [userfname, userlname, useraddress]
                        
                        rogue_chance = random.choices([1, 0], weights=(100,5))[0]
                        
                        if rogue_chance == 0:
                            random_order = rogue_data(random_order)
                                  

                        # write 1 row
                        writer.writerow(random_order)

create_csv_data()
#Timer end
end = timer()

#Print elapsed time (seconds)
print(f"Approximate Processing Time: {end - start}")
