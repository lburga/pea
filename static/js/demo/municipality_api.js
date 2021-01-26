var municipality_select = document.getElementById('id_municipality')
var provinces_dataset = []

async function lima_data() {
	const response = await fetch(ubigeo_url)
	if (response.ok) {
		return response.json();
	} else {
		alert("HTTP-Error: " + response.status);
	}
}

function append_empty_value(select){
	let option = document.createElement('option')
	option.value = ''
	option.text = '-'
	select.appendChild(option)
}

lima_data().then(data => {
	provinces_dataset = [...data.provincias]
	append_empty_value(municipality_select)
    for (var i = 0; i < data.provincias.length; i++) {
    	for (var j = data.provincias[i].distritos.length - 1; j >= 0; j--) {
			let option = document.createElement('option')
			option.value = data.provincias[i].distritos[j].iddist
			option.text = data.provincias[i].distritos[j].nom_dist
			municipality_select.appendChild(option)
    	}
    }
}).then(()=>{
	try{
		set_intial(initial_municipality)
	}catch{

	}
})

function set_intial(initial){
	municipality_select.value = initial
	$(municipality_select).trigger("change")
}

$('.select2').select2()

// $(".red-border").each(function() {
//   $(this).siblings(".select2-container").css('border', '0.1px solid red');
//   $(this).siblings(".select2-container").css('border-radius', '4px');
// });