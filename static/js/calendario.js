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



//Aqui extraemos el valor que esta en el campo de fecha, si esta vacio le avisara al usuario
$(document).ready(function(e){
	$('#btn-agendarcita').click(function(e){
		var fechacita = document.getElementById('datepicker').value;
		if (fechacita == ""){
			e.preventDefault();
			alert('Debes de seleccioanr la fecha de tu cita', 'Aviso')
		}	
	});
});


