// Use Types and Subtypes
const first_use_subtype_select = document.getElementById('id_building_use-0-use_subtype')
const subtypes_options =[...first_use_subtype_select.options]
clear_use_subtypes(first_use_subtype_select);

function set_use_type_inputs_onchange(){
	let use_type_selects = document.getElementsByClassName('use_type_change')
	for (let i = use_type_selects.length - 1; i >= 0; i--) {
		use_type_selects[i].onchange = (ev) => {
			set_use_type_onchange(ev.target)
		}
	}
}

function set_use_type_onchange(el){
	let tr = el.parentNode.parentNode.parentNode
	var use_subtype_input = tr.childNodes[3].childNodes[1].childNodes[4]
	use_subtype_input.disabled = true;
	clear_use_subtypes(use_subtype_input)
	let value = el.value
	if (value == '') {
		use_subtype_input.disabled = true;
	} else{
		for (let i = 0; i<subtypes_options.length; i++) {
			if (subtypes_options[i].value.includes(value)){
				use_subtype_input.add(subtypes_options[i].cloneNode(true))
			}
		}
		use_subtype_input.disabled = false;
	}
	use_subtype_input.selectedIndex = 0;
}

function clear_use_subtypes(el){
	if (!is_set_data) {
		el.options.length = 0;
	}
}

// USE AREA
function set_use_area_inputs_onchange(){
	let use_area_inputs = document.getElementsByClassName('use_area_change')
	for (let i = use_area_inputs.length - 1; i >= 0; i--) {
		use_area_inputs[i].oninput = () => {
			set_use_area_total()
		}
	}
}

function set_use_area_total(){
	let use_total_area_input = document.getElementById('id_total_area')
	let use_area_inputs = document.getElementsByClassName('use_area_change')
	let total_use_area = 0
	for (var i = use_area_inputs.length - 1; i >= 0; i--) {
		let value = use_area_inputs[i].value
		total_use_area = total_use_area + (value == '' ? 0 : parseFloat(value))
	}
	use_total_area_input.value = total_use_area
}

// Work Types and Subtypes
var option_O_note = document.getElementById('option_O_note')

function set_work_type_inputs_onchanges(){
	var work_type_inputs = document.getElementsByClassName('work_type_change')
	for (let i = work_type_inputs.length - 1; i >= 0; i--) {
		work_type_inputs[i].onchange = () => {
			works_types_restrictions(work_type_inputs[i]);
		}
	}
}
function set_budget_inputs_onchanges(){
	let budget_inputs = document.getElementsByClassName('budget_change')
	for (let i = budget_inputs.length - 1; i >= 0; i--) {
		budget_inputs[i].oninput = () => {
			set_total_value()
		}
		budget_inputs[i].onchange = () => {
			set_total_value()
		}
	}
}

function set_unit_value_inputs_onchanges(){
	let unit_inputs = document.getElementsByClassName('unit_value_change')
	for (let i = unit_inputs.length - 1; i >= 0; i--) {
		unit_inputs[i].oninput = () => {
			set_budget_value(unit_inputs[i])
			set_area_onchange(unit_inputs[i])
			set_total_value()
		}
	}
}

function set_area_onchange(unit_value_el){
	let tr = unit_value_el.parentNode.parentNode.parentNode
	var area_input = tr.childNodes[3].childNodes[1].childNodes[4]
	area_input.oninput = () =>{
		set_budget_area_value(area_input)
		set_total_value()
	}
}

function set_budget_area_value(area_el){
	let area_value = area_el.value
	let tr = area_el.parentNode.parentNode.parentNode
	let unit_value_input = tr.childNodes[5].childNodes[1].childNodes[4]
	let unit_value = unit_value_input.value == '' ? 0: parseFloat(unit_value_input.value)
	let budget_input = tr.childNodes[7].childNodes[1].childNodes[4]
	budget_input.value = area_value*unit_value
}

function set_budget_value(unit_value_el){
	let unit_value = unit_value_el.value
	let tr = unit_value_el.parentNode.parentNode.parentNode
	let area_input = tr.childNodes[3].childNodes[1].childNodes[4]
	let area_value = area_input.value == '' ? 0 : parseFloat(area_input.value)
	let budget_input = tr.childNodes[7].childNodes[1].childNodes[4]
	budget_input.value = area_value*unit_value
}

function set_total_value(){
	var total_budget = document.getElementById('id_total_budget')
	let budget_inputs = document.getElementsByClassName('budget_change')
	let total_value = 0
	for (var i = budget_inputs.length - 1; i >= 0; i--) {
		let budget_value = budget_inputs[i].value === '' ? 0 : parseFloat(budget_inputs[i].value)
		let value = parseFloat(budget_value)
		total_value = total_value + value
	}
	if (total_budget.value === '') {total_budget.value = 0}
	total_budget.value = total_value
}

function works_types_restrictions(el){
	let value = el.value
	let tr = el.parentNode.parentNode.parentNode
	let area_input = tr.childNodes[3].childNodes[1].childNodes[4]
	let unit_value_input = tr.childNodes[5].childNodes[1].childNodes[4]
	if (value === 'RM' || value === 'RF' || value === 'CP' || value === 'O') {
		area_input.readOnly = true
		unit_value_input.readOnly = true
		area_input.value = ''
		unit_value_input.value = ''
	}else if(value === 'PV'){
		area_input.readOnly = false
		unit_value_input.readOnly = true
		unit_value_input.value = ''
	}else{
		area_input.readOnly = false
		unit_value_input.readOnly = false		
	}
	if (value === 'O') {
		option_O_note.style.display = 'block'
	}else{
		option_O_note.style.display = 'none'
	}
}

// Profession Change

function set_profeessions_onchange(){
	var profession_inputs = document.getElementsByClassName('profession_change')
	for (let i = profession_inputs.length - 1; i >= 0; i--) {
		profession_inputs[i].onchange = () => {
			set_profeession_title(profession_inputs[i])
		}
	}
}
function set_profeession_title(el){
	let profession_value = el.value
	let tr = el.parentNode.parentNode.parentNode
	let profession_title_dom = tr.childNodes[5].childNodes[1].childNodes[1]
	profession_title_dom.innerText = profession_value === 'A' ? 'CAP No.:' : 'CIP No.:'
}

// RUC and DNI
var ruc_input = document.getElementById('id_ruc')
var dni_input = document.getElementById('id_dni')

ruc_input.oninput = () =>{
	if (ruc_input.value !== '') {
		dni_input.readOnly = true
	}else{
		dni_input.readOnly = false
	}
}
dni_input.oninput = () =>{
	if (dni_input.value !== '') {
		ruc_input.readOnly = true
	}else{
		ruc_input.readOnly = false
	}
}

// First Arquitect
function set_disable_first_arch(){
	document.getElementById('id_architects-0-full_name').readOnly = true;
	document.getElementById('id_architects-0-profession').disabled = true;
	document.getElementById('id_architects-0-c_id').readOnly = true;
	document.getElementById('id_architects-0-sign').disabled = true;
	document.getElementById('id_architects-0-phone').readOnly = true;
	document.getElementById('id_architects-0-email').readOnly = true;
}

function set_enable_first_arch(){
	document.getElementById('id_architects-0-full_name').readOnly = false;
	document.getElementById('id_architects-0-profession').disabled = false;
	document.getElementById('id_architects-0-c_id').readOnly = false;
	document.getElementById('id_architects-0-sign').disabled = false;
	document.getElementById('id_architects-0-phone').readOnly = false;
	document.getElementById('id_architects-0-email').readOnly = false;
}

// TYPICAL PLANTS File Input
var is_typical_plants = document.getElementById('id_is_typical_plants')
var file_input = document.getElementById('file_input')
function set_typical_plants_input(){
	if (is_typical_plants.checked) {
		file_input.style.display = 'block'
	}else{
		file_input.style.display = 'none'
	}
}
is_typical_plants.onchange = () =>{
	set_typical_plants_input()
}

option_O_note.style.display = 'none'
file_input.style.display = 'none'

function profession_js(){
	// set_enable_first_arch()
	set_profeessions_onchange()
}

function review_reqest_js(){
	set_work_type_inputs_onchanges();
	set_budget_inputs_onchanges();
	set_unit_value_inputs_onchanges();
} 

function use_type_js(){
	set_use_type_inputs_onchange();
	set_use_area_inputs_onchange();

}


// First Load

profession_js();
review_reqest_js();
use_type_js();
set_typical_plants_input();

// set_disable_first_arch()

// Fixs
$(document).ready(()=>{
	setTimeout(()=>{
		document.getElementById('id_time_sttlement').readOnly = false
	},1000)
})