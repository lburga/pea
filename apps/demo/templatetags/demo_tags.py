from django import template
from apps.demo.choices import (EBITDA,)

register = template.Library()

@register.filter()
def key(dictionary, key):
	return dictionary[key]

@register.filter()
def coma(value):
	return "{:,}".format(value)

def value_color(value):
	if value == 0:
		return 'warning'
	elif value > 0:
		return 'info'
	else:
		return 'danger'

@register.simple_tag()
def get_operating_margin(report, month, coma_format=True):
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
	if coma_format:
		return coma(t_revenues - t_cogs - t_expenses)
	else:
		return t_revenues - t_cogs - t_expenses

@register.simple_tag()
def get_operating_margin_class(report, month):
	return value_color(get_operating_margin(report, month, False))

@register.simple_tag()
def get_total_operating_margin(report, coma_format=True):
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
	if coma_format:
		return coma(t_revenues - t_cogs - t_expenses)
	return t_revenues - t_cogs - t_expenses

@register.simple_tag()
def get_data(report, month, category, item):
	for i in report:
		if i['month'] == month and i['category'] == category and i['item'] == item:
			return coma(i['data'])
	return 'None'

@register.simple_tag()
def get_ebitda_item(ebitda_report, month, ebitda):
	for i in ebitda_report:
		if i['month'] == month and i['ebitda'] == ebitda:
			return coma(i['data'])
	return 'None'

@register.simple_tag()
def get_ebitda(report, ebitda_report, month, coma_format=True):
	value = get_operating_margin(report, month, False)
	for i in report:
		for e in ebitda_report:
			if i['month'] == month and e['ebitda'] == 'Depreciation and Amortization':
				if coma_format:
					return coma(value + e['data'])
				else:
					return value + e['data']
	raise Exception

@register.simple_tag()
def get_ebitda_class(report, ebitda_report, month):
	return value_color(get_ebitda(report, ebitda_report, month, False))

@register.simple_tag()
def get_total_ebitda(report, ebitda_report, months, coma_format=True):
	total = 0
	for month in months:
		total += get_ebitda(report, ebitda_report, month, False)
	if coma_format:
		return coma(total)
	return total

@register.simple_tag()
def get_total_ebitda_item(ebitda_report, ebitda, coma_format=False):
	total = 0
	for i in ebitda_report:
		if i['ebitda'] == ebitda:
			total += i['data']
	if coma_format:
		return coma(total)
	return total

def get_month_ebdita(ebitda_report, month):
	total = 0
	for e in ebitda_report:
		if e['month'] == month:
			total += e['data']
	return total

@register.simple_tag()
def get_income_before_tax(report, ebitda_report, month, coma_format=True):
	ebitda = get_ebitda(report, ebitda_report, month, False)
	month_sum = get_month_ebdita(ebitda_report, month)
	if coma_format:
		return coma(ebitda - month_sum)
	return ebitda - month_sum

@register.simple_tag()
def get_total_income_before_tax(report, ebitda_report, months, coma_format=True):
	total = 0
	for month in months:
		total += get_income_before_tax(report, ebitda_report, month, False)
	if coma_format:
		return coma(total)
	return total

@register.simple_tag()
def get_total_month(report, month, category):
	total = 0
	for i in report:
		if i['month'] == month and i['category'] == category:
			total = total + i['data']
	return coma(total)

@register.simple_tag()
def get_total_income_statement(report, item, coma_format=True):
	total = 0
	for i in report:
		if i['item'] == item:
			total = total + i['data']
	if coma_format:
		return coma(total)
	return total

@register.simple_tag()
def get_total_category(report, category, coma_format=True):
	total = 0
	for i in report:
		if i['category'] == category:
			total = total + i['data']
	if coma_format:
		return coma(total)
	return total

@register.simple_tag()
def get_data_by_moth(data:list, month, coma_format=True):
	for d in data:
		if d['month'] == month:
			value = int(d['data'])
			if coma_format:
				return (coma(value))
			return value

@register.simple_tag()
def get_income(report, ebitda_report, iva, rent, month, coma_format=True):
	income = get_income_before_tax(report, ebitda_report, month, False)
	iva_value = get_data_by_moth(iva, month, False)
	rent_value = get_data_by_moth(rent, month, False)
	if coma_format:
		return coma(income - iva_value - rent_value)
	return income - iva_value - rent_value

@register.simple_tag()
def get_total_income(report, ebitda_report, iva, rent, months, coma_format=True):
	total = 0
	for month in months:
		total += get_income(report, ebitda_report, iva, rent, month, False)
	if coma_format:
		return coma(total)
	return total

@register.simple_tag()
def get_income_class(report, ebitda_report, iva, rent, month):
	return value_color(get_income(report, ebitda_report, iva, rent, month, False))
	
@register.simple_tag()
def get_last_totals(last_totals, item, coma_format=True):
	for lt in last_totals:
		if item == lt['item']:
			if coma_format:
				return coma(lt['data'])
			return lt['data']

@register.simple_tag()
def get_last_totals_category(last_totals, category, coma_format=True):
	total = 0
	for lt in last_totals:
		if category == lt['category']:
			total += lt['data']	
	if coma_format:
		return coma(total)
	return total

@register.simple_tag()
def get_last_totals_operating_margin(last_totals):
	t_revenues = 0
	t_cogs = 0
	t_expenses = 0
	for i in last_totals:
		if i['category'] == 'REVENUES':
			t_revenues = t_revenues + i['data']
		if i['category'] == 'COGS':
			t_cogs = t_cogs + i['data']
		if i['category'] == 'OPERATING EXPENSES':
			t_expenses = t_expenses + i['data']
	return coma(t_revenues - t_cogs - t_expenses)

@register.simple_tag()
def get_var_income_statement(report, last_totals, item, coma_format=True):
	total_income = get_total_income_statement(report, item, False)
	last_total_income = get_last_totals(last_totals, item, False)
	if coma_format:
		return coma(total_income - last_total_income)
	return total_income - last_total_income

@register.simple_tag()
def get_var_income_statement_class(report, last_totals, item):
	return value_color(
		get_var_income_statement(report, last_totals, item, False))

@register.simple_tag()
def get_var_total_category(report, category, last_totals, coma_format=True):
	total_income = get_total_category(report, category, False)
	last_total_income = get_last_totals_category(last_totals, category, False)
	if coma_format:
		return coma(total_income - last_total_income)
	return total_income - last_total_income

@register.simple_tag()
def get_var_total_category_class(report, category, last_totals):
	return value_color(
		get_var_total_category(report, category, last_totals, False))

@register.simple_tag()
def get_var_last_totals_operating_margin(report, last_totals, coma_format=True):
	total_operating_margin = get_total_operating_margin(report, False)
	last_total_operating_margin = get_total_operating_margin(last_totals, False)
	if coma_format:
		return coma(total_operating_margin - last_total_operating_margin)
	return total_operating_margin - last_total_operating_margin

@register.simple_tag()
def get_var_last_totals_operating_margin_class(report, last_totals):
	return value_color(
		get_var_last_totals_operating_margin(report, last_totals, False))

@register.simple_tag()
def get_var_total_ebitda(report, ebitda_report, months, last_ebdita, coma_format=True):
	ebitda = get_total_ebitda(report, ebitda_report, months, False)
	if coma_format:
		return coma(ebitda - last_ebdita)
	return ebitda - last_ebdita

@register.simple_tag()
def get_var_total_ebitda_class(report, ebitda_report, months, last_ebdita, coma_format=True):
	return value_color(
		get_var_total_ebitda(report, ebitda_report, months, last_ebdita, False))
	
@register.simple_tag()
def get_var_total_ebitda_item(ebitda_report, last_ebdita_totals, item, coma_format=True):
	total_ebitda = get_total_ebitda_item(ebitda_report, item, False)
	if coma_format:
		return coma(total_ebitda - last_ebdita_totals[item])
	return total_ebitda - last_ebdita_totals[item]

@register.simple_tag()
def get_var_total_ebitda_item_class(ebitda_report, last_ebdita_totals, item):
	return value_color(
		get_var_total_ebitda_item(ebitda_report, last_ebdita_totals, item, False))

@register.simple_tag()
def get_var_total_income_before_tax(report, ebitda_report, months, last_ebdita_totals, coma_format=True):
	total_income_before_tax = get_total_income_before_tax(report, ebitda_report, months, False)
	last_total = last_ebdita_totals['income']
	if coma_format:
		return coma(total_income_before_tax - last_total)
	return total_income_before_tax - last_total

@register.simple_tag()
def get_var_total_income_before_tax_class(report, ebitda_report, months, last_ebdita_totals):
	return value_color(
		get_var_total_income_before_tax(report, ebitda_report, months, last_ebdita_totals, False))

@register.simple_tag()
def get_var_total_income(report, ebitda_report, iva, rent, months, last_ebdita_totals, coma_format=True):
	total_income = get_total_income(report, ebitda_report, iva, rent, months, False)
	if coma_format:
		return coma(total_income - last_ebdita_totals['net'])
	return total_income - last_ebdita_totals['net']

@register.simple_tag()
def substraction(value1, value2):
	return coma(value1 - value2)

@register.simple_tag()
def substraction_class(value1, value2):
	return value_color(value1 - value2)