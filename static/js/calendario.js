// aquí se manda llamar el calendario date picker y se le asignaron algunos valores 
$("#datepicker").datepicker({
		changeMonth:true, 
		changeYear:true,
	   dateFormat: 'dd-mm-yy',
	   firstDay: 1,
	   monthNames: ['Enero', 'Febreo', 'Marzo',
	   'Abril', 'Mayo', 'Junio',
	   'Julio', 'Agosto', 'Septiembre',
	   'Octubre', 'Noviembre', 'Diciembre'],
	   dayNamesMin: ['Dom', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab']
});




$(document).ready(function(e){
	$('#btn-agendarcita').click(function(e){
		var fechacita = document.getElementById('datepicker').value;
		if (fechacita == ""){
			e.preventDefault();
			toastr.warning('Debes de seleccioanr la fecha de tu cita', 'Aviso')
		}	
	});
});


$(document).ready(function(e){

});