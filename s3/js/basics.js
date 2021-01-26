try{
	$('.select2').select2();
}catch{
	
}


function cancel_button (){
	var is_confirm = confirm('¿Desea cancelar la operación?')
	if (is_confirm) {
		return true
	}
	return false
}

// Convert Upper

function set_upper_inputs(){
	var upper_inputs = document.getElementsByClassName('upper-case')
	for (var i = upper_inputs.length - 1; i >= 0; i--) {
		upper_inputs[i].oninput = (ev) => {
			ev.target.value = ev.target.value.toUpperCase()
		}
	}
}
// DNI
function set_dni_inputs(){
	var dni_inputs = document.getElementsByClassName('dni-case')
	for (var i = dni_inputs.length - 1; i >= 0; i--) {
		dni_inputs[i].oninput = (ev) => {
			if(ev.target.value.length > 8){
				ev.target.value = ev.target.value.slice(0,8)
			}
		}
	}
}

// RUC
function set_ruc_inputs(){
	var dni_inputs = document.getElementsByClassName('ruc-case')
	for (var i = dni_inputs.length - 1; i >= 0; i--) {
		dni_inputs[i].oninput = (ev) => {
			if(ev.target.value.length > 11){
				ev.target.value = ev.target.value.slice(0,11)
			}
		}
	}
}

set_upper_inputs()
set_dni_inputs()
set_ruc_inputs()