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


def rint(m,n):
	return random.randint(m,n)

def rfloat(m,n):
	return round(random.randint(m,n) + random.random(), 2)

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
	context = {
		'report':report,
		'categories': [ i[1] for i in CATEGORIES ],
		'months': [ m[1] for m in MONTHS ],
		# 'income_statement': [ ins[1] for ins in INCOME_STATEMENT.items()],
		'income_statement': INCOME_STATEMENT,
	}
	return context
