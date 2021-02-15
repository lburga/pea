import random

MONTHS = (
	('1', 'Enero'),
	('2', 'Febrero'),
	('3', 'Marzo'),
	('4', 'Abril'),
	('5', 'Mayo'),
	('6', 'Junio'),
	('7', 'Julio'),
	('8', 'Agosto'),
	('9', 'Septiembre'),
	('9', 'Octubre'),
	('10', 'Noviembre'),
	('11', 'Diciembre'),
)

CATEGORIES = (
	('1','REVENUES'),
	('2','COGS'),
	('3','OPERATING EXPENSES'),
)

INCOME_STATEMENT = {
	'REVENUES': (
		('1','Licenses Sales'),
		('2','Services Sales'),
		('3','Maintenance Sales'),
		('4','Others Sales'),
	),
	'COGS': (
		('1', 'Informatica Cost'),
		('2', 'Services Cost'),
		('3', 'Maintenance Cost'),
	),
	'OPERATING EXPENSES': (
		('1', 'IT/Soporte'),
		('2', 'Finance'),
		('3', 'Delivery and Operations'),
		('4', 'Sales & Marketing'),
	)
}
EBITDA = [
	('1', 'Other Non Operating Income/Expense'),
	('2', 'Interest Expense/Income'),
	('3', 'Depreciation and Amortization'),
	('4', 'Foreign Currency Translation'),
]


def rint(m,n):
	return random.randint(m,n)

def rfloat(m,n):
	return round(random.randint(m,n) + random.random(), 2)

def get_ebitda_data(ebitda):
	for i in EBITDA:
		if ebitda == EBITDA[0][1]:
			return 300
		elif ebitda == EBITDA[1][1]:
			return 200
		elif ebitda == EBITDA[2][1]:
			return 1500
		elif ebitda == EBITDA[3][1]:
			return 200
		else:
			return -1

def get_last_totals():
	totals = []
	for c in CATEGORIES:
		for d in INCOME_STATEMENT[c[1]]:
			totals.append({
				'category': c[1],
				'item': d[1],
				'data': rint(10000, 100000)
			})
	return totals

def get_last_ebdita_totals():
	totals = {}
	for e in EBITDA:
		totals[e[1]] = rint(-5000, 5000)
	totals['income'] = rint(-20000, 20000)
	totals['iva'] = rint(-40000, 40000)
	totals['rent'] = rint(-40000, 40000)
	totals['net'] = rint(-200000, 200000)
	return totals

def get_pea():
	report = []
	for c in CATEGORIES:
		total = 0
		for d in INCOME_STATEMENT[c[1]]:
			for m in MONTHS:
				data = rint(100,10000)
				report.append(
					{
						'category': c[1],
						'item': d[1],
						'month': m[1],
						'data': data,
					}
				)
	ebitda = []
	for e in EBITDA:
		for m in MONTHS:
			ebitda.append({
				'month': m[1],
				'ebitda': e[1],
				'data': get_ebitda_data(e[1])
			})
	IVA = []
	TOTAL_IVA = 0
	for m in MONTHS:
		IVA.append({
			'month': m[1],
			'data': 3026.36833333333,	
		})
		TOTAL_IVA += 3026.36833333333
	RENT = []
	TOTAL_RENT = 0
	for m in MONTHS:
		RENT.append({
			'month': m[1],
			'data': 4539.5525,	
		})
		TOTAL_RENT += 4539.5525
	context = {
		'report':report,
		'categories': [ i[1] for i in CATEGORIES ],
		'months': [ m[1] for m in MONTHS ],
		'income_statement': INCOME_STATEMENT,
		'ebitda_names': [ e[1] for e in EBITDA ],
		'ebitda': ebitda,
		'iva': IVA,
		'total_iva': int(TOTAL_IVA),
		'rent': RENT,
		'total_rent': int(TOTAL_RENT),
		'last_totals': get_last_totals(),
		'last_ebdita': rint(-50000,50000),
		'last_ebdita_totals': get_last_ebdita_totals(),
	}
	return context
