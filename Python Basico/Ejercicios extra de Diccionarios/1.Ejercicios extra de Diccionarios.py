#Dada una lista de ventas con la siguiente información:
#date
#customer_email
#items
#Y cada item teniendo la siguiente información:
#name
#upc
#unit_price
#Cree un diccionario que guarde el total de ventas de cada UPC.

sales = [
	{
		'date': '15/03/25',
		'customer_email': 'john.smith@gmail.com',
		'items': [
			{
				'name': 'Oakley Radar EV Path Sunglasses',
				'upc': 'ITEM-453',
				'unit_price': 185.00,
			},
			{
				'name': 'Oakley Factory Pilot Gloves',
				'upc': 'ITEM-324',
				'unit_price': 45.00,
			},
			{
				'name': 'Oakley Water Bottle',
				'upc': 'ITEM-432',
				'unit_price': 22.50,
			},
		],
	},
	{
		'date': '22/05/25',
		'customer_email': 'sarah.johnson@hotmail.com',
		'items': [
			{
				'name': 'Oakley Radar EV Path Sunglasses',
				'upc': 'ITEM-453',
				'unit_price': 185.00,
			},
			{
				'name': 'Oakley ARO5 MIPS Helmet',
				'upc': 'ITEM-23',
				'unit_price': 220.00,
			},
		],
	},
	{
		'date': '08/07/25',
		'customer_email': 'michael.brown@outlook.com',
		'items': [
			{
				'name': 'Oakley ARO5 MIPS Helmet',
				'upc': 'ITEM-23',
				'unit_price': 220.00,
			},
			{
				'name': 'Oakley Water Bottle',
				'upc': 'ITEM-432',
				'unit_price': 22.50,
			},
		],
	},
]

total_sales_by_upc = {}
for sale in sales:
    for item in sale['items']:
        upc = item['upc']
        price = item['unit_price']
        if upc in total_sales_by_upc:
            total_sales_by_upc[upc] += price
        else:
            total_sales_by_upc[upc] = price 
print(total_sales_by_upc)        