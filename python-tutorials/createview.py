# %%
# import a Python package that helps us connect to the new database
import sqlite3
import pandas as pd

# connect to the billing database
con = sqlite3.connect('billing.db')
cur = con.cursor()

# show us the three tables that exist there
table_list = [a[0] for a in cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]

for table in table_list:
  print('Existing table named ' + table + '\n')

# build a query to create the new billing view

# first, we'll include some code that tells the database we're creating a new view of the data
query = 'CREATE VIEW billing AS'

# next, we'll tell the database which columns we want in our final table
query += ' SELECT BillingEvent.ID AS ID, username, Date, Event FROM BillingEvent'

# lastly, we'll explain how to connect the three tables
query += ' INNER JOIN Customer on BillingEvent.CustomerID = Customer.ID'
query += ' INNER JOIN BillingEventTypes on BillingEvent.EventType = BillingEventTypes.ID'

# now that the query in SQL is built, we'll use Python to send it to the database. We've added some code to catch an error if you run the exercise more than once!

print("Creating new billing view combining the three: ")
try:
  cur.execute(query)
except sqlite3.OperationalError:
  print("You've already run this exercise! Here's the table: ")
  
# finally, let's take a look at our table!
# we'll do this the way a data scientist might - using the package pandas!
billing = pd.read_sql('SELECT * FROM billing',con)
print(billing)

# close our connection to the database
con.close()

# %%
x = 0

if x == 0:
  print("x is equal to zero")
elif x >= 0:
  print("x is greater than zero")
else:
  print("x is less than zero")
  
# %%
x = 5

if x <= 2:
  print("This is printed")
if x <= 4:
  print("This is also printed")
if x <= 6:
  print("Is this printed?")
if x <= 8:
  print("This might be printed.")
  
# %%
for i in range(3):
  print(i)
  
# %%
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key: value for key, value in zipped_drinks}

print(zipped_drinks)

zipped_drinks_list = list(zip(drinks, caffeine))
print(zipped_drinks_list)

print(drinks_to_caffeine)

# %%
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {song:playcount for [song, playcount] in zip(songs, playcounts)}

print(plays)

plays["Respect"] = 94
plays["Purple Haze"] = 1

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)

# dictionaries common methods: .keys(), .values(), .items(), get(), .update(), .pop(), .popitem(), .clear(), .copy()

# %%
oscars = {"Best Picture": "Moonlight", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

for element in oscars:
  print(element)
  
# %%
inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}

print(12 in inventory)

# %%
inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}

print("the peacemaker" in inventory)

# %%
def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name
  
    
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password


# %%
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ','.join(reapers_line_one_words)

# .strip() removes leading and trailing whitespace
# .split() splits a string into a list
# .join() joins a list into a string
# .replace() replaces a substring with another substring
# .find() finds the first occurrence of a substring
# .format() formats a string

# %%
def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date = publishing_date, author = author, title = title, original_work = original_work)
  return poem_desc

my_beard_description = poem_description("1974", "Shel Silverstein", "My Beard", "Where the Sidewalk Ends")
print(my_beard_description)

# %%
with open('welcome.txt') as text_file:
  text_data = text_file.read()
  print(text_data)
  
with open('cool_dogs.txt', 'a') as cool_dogs_file:
  cool_dogs_file.write('Air Buddy\n')

with open('cool_dogs.txt', 'r') as cool_dogs_file:
  for line in cool_dogs_file.readlines():
    print(line)
    

# %%
import csv

list_of_email_addresses = []
with open('users.csv', newline='') as users_csv:
  user_reader = csv.DictReader(users_csv)
  for row in user_reader:
    list_of_email_addresses.append(row['Email'])

# %%
import csv

with open('books.csv') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = [book['ISBN'] for book in books_reader]

print(isbn_list)

# %%
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv

with open('logger.csv', 'w') as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames=fields)
  log_writer.writeheader()
  for line in access_log:
    log_writer.writerow(line)

# Now, read and print the contents of logger.csv
with open('logger.csv', 'r') as logger_csv:
    content = logger_csv.read()
    print(content)
    

# %%
import json

with open('message.json') as message_json:
  message = json.load(message_json) # == message = message_json.read()
  print(message['text'])
  
# %%
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

import json

with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json) # == data_json.write(json.dumps(data_payload))