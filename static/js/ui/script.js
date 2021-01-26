
$(document).ready(function() {

	try{
		$('.timepicker').mdtimepicker({});
	}catch{

	}


	var datatable = document.querySelector('.datatable')

	if(datatable){
		$('.datatable').DataTable({
		    responsive: true,
		    searching: true,
		    info: true,
		    ordering: false,
		    language: {
			    "decimal":        "",
			    "emptyTable":     "Sin datos",
			    "info":           "Showing _START_ to _END_ of _TOTAL_ entries",
			    "infoEmpty":      "Showing 0 to 0 of 0 entries",
			    "infoFiltered":   "(filtered from _MAX_ total entries)",
			    "infoPostFix":    "",
			    "thousands":      ",",
			    "lengthMenu":     "Mostrar _MENU_ registros",
			    "loadingRecords": "Cargando...",
			    "processing":     "Procesando...",
			    "search":         "Palabra Clave:",
			    "zeroRecords":    "Sin Registros Encontrados",
			    "paginate": {
			        "first":      "Primero",
			        "last":       "Último",
			        "next":       "Siguiente",
			        "previous":   "Anterior"
			    },
			    "aria": {
			        "sortAscending":  ": activate to sort column ascending",
			        "sortDescending": ": activate to sort column descending"
			    }
			}
		});
	}
});


