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

function set_profeessions_col_onchange(){
	var profession_inputs = document.getElementsByClassName('profession_col_change')
	for (let i = profession_inputs.length - 1; i >= 0; i--) {
		profession_inputs[i].onchange = () => {
			set_profeession_col_title(profession_inputs[i])
		}
	}
}
function set_profeession_col_title(el){
	let profession_value = el.value
	let div = el.parentNode.parentNode
	let profession_title_dom = div.childNodes[7].childNodes[1]
	profession_title_dom.innerText = profession_value === 'A' ? 'CAP No.:' : 'CIP No.:'
}

set_profeessions_col_onchange()

function profession_js(){
	set_profeessions_onchange()
}

profession_js();

// Fixs
$(document).ready(()=>{
	setTimeout(()=>{
		var tabs = document.querySelectorAll('[role="tabpanel"]')
		for (var i = tabs.length - 1; i >= 0; i--) {
			tabs[i].classList.add('tab-pane')
		}
		document.getElementById('id_start_time').readOnly = false
		document.getElementById('id_end_time').readOnly = false
	},1000)
})