import codecademylib3
import pandas as pd

inventory = pd.read_csv('inventory.csv')

print(inventory.head(20))

staten_island = inventory[(inventory['location'] == 'Staten Island')]

print(staten_island)

product_request = staten_island.product_description

seed_request = inventory[(inventory['location'] == 'Brooklyn') & (inventory['product_type'] == 'seeds')]

print(seed_request)

inventory['in_stock'] = inventory.quantity.apply(
  lambda x: 'True'
  if x > 0
  else False
)

print(inventory.head(20))

inventory['total_value'] = inventory.price * inventory.quantity

print(inventory.head(20))

combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)

inventory['full_description'] = inventory.apply(combine_lambda, axis = 1)

print(inventory.head(20))