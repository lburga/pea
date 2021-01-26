from django import template

register = template.Library()

@register.simple_tag()
def get_data(report, month, category, item):
	for i in report:
		if i['month'] == month and i['category'] == category and i['item'] == item:
			# return i['data']
			return "{:,}".format(i['data'])
	return 'None'

@register.simple_tag()
def get_total_month(report, month, category):
	total = 0
	for i in report:
		if i['month'] == month and i['category'] == category:
			total = total + i['data']
	# return round(total, 2)
	return "{:,}".format(total)


@register.simple_tag()
def get_operating_margin_class(report, month):
	value = get_operating_margin(report, month)
	value = float(value.replace(',',''))
	if value == 0:
		return 'warning'
	elif value > 0:
		return 'info'
	else:
		return 'danger'

@register.simple_tag()
def get_total_income_statement(report, item):
	total = 0
	for i in report:
		if i['item'] == item:
			total = total + i['data']
	return "{:,}".format(total)

@register.simple_tag()
def get_total_category(report, category):
	total = 0
	for i in report:
		if i['category'] == category:
			total = total + i['data']
	return "{:,}".format(total)


@register.simple_tag()
def get_operating_margin(report, month):
	t_revenues = 0
	t_cogs = 0
	t_expenses = 0
	for i in report:
		if i['month'] == month and i['category'] == 'REVENUES':
			t_revenues = t_revenues + i['data']
		if i['month'] == month and i['category'] == 'COGS':
			t_cogs = t_cogs + i['data']
		if i['month'] == month and i['category'] == 'OPERATING EXPENSES':
			t_expenses = t_expenses + i['data']
	# return round(total, 2)
	# return "{:,}".format(t_revenues - t_cogs - t_expenses)
	return "{:,}".format(t_revenues - t_cogs - t_expenses)

@register.simple_tag()
def get_total_operating_margin(report):
	t_revenues = 0
	t_cogs = 0
	t_expenses = 0
	for i in report:
		if i['category'] == 'REVENUES':
			t_revenues = t_revenues + i['data']
		if i['category'] == 'COGS':
			t_cogs = t_cogs + i['data']
		if i['category'] == 'OPERATING EXPENSES':
			t_expenses = t_expenses + i['data']
	# return round(total, 2)
	# return "{:,}".format(t_revenues - t_cogs - t_expenses)
	return "{:,}".format(t_revenues - t_cogs - t_expenses)

@register.filter()
def key(dictionary, key):
	return dictionary[key]

@register.filter()
def floatcoma(value):
	return "{:,}".format(value)
