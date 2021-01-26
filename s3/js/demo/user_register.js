// Título de Colegiatura
var profession = document.getElementById('id_profession')

profession.onchange = () => {
	let value = profession.value
	let c_id_title_dom = document.getElementById('c_id_title')
	c_id_title_dom.innerText = value === 'A' ? 'CAP No.:' : 'CIP No.:'
}

// CAP
function set_c_id_oninput(){
	let c_id_input = document.getElementById('id_c_id')
	c_id_input.oninput = (ev) => {
		if (profession.value == 'A') {
			if(ev.target.value.length > 5){
				ev.target.value = ev.target.value.slice(0,5)
			}
		}else if (profession.value == 'I'){
			if(ev.target.value.length > 6){
				ev.target.value = ev.target.value.slice(0,6)
			}		}
	}
}
set_c_id_oninput()

// Celular
let cellphone_input = document.getElementById('id_cellphone')
cellphone_input.oninput = (ev) => {
	if(cellphone_input.value.length > 9){
		cellphone_input.value = cellphone_input.value.slice(0,9)
	}
	if(cellphone_input.value[0] != '9'){
		cellphone_input.value = ''
	}	
}
// Teléfono
let phone_input = document.getElementById('id_phone')
phone_input.oninput = (ev) => {
	if(phone_input.value.length > 8){
		phone_input.value = phone_input.value.slice(0,8)
	}
}

// Firma
let signature_image_input = document.getElementById('id_signature_image')
let preview = document.getElementById("peview")
if (preview) {preview.style.display = 'none'}
signature_image_input.oninput = (ev) => {
	let file = ev.target.files
	if (file.length > 0) {
	    var fileReader = new FileReader();
	    fileReader.onload = function (event) {
			if (preview) {preview.style.display = 'block'}
	    	preview.setAttribute("src", event.target.result);
	    };
	    fileReader.readAsDataURL(file[0]);
	}
}