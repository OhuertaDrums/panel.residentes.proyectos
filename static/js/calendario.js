
//$("#datepicker").datepicker({
//   	onSelect: function(){
//  		var dato = $(this).datepicker('getDate');
//   		console.log("La fecha actual es:" + dato);
//   		//alert($("#datepicker").data("dato"));
//   	}
//});




$("#datepicker").datepicker({
   	onSelect: function(dato){
   	}
});


$(document).on('ready', function(){
	
		var token = csrftoken;
		var data = new FotmData();
		data.append('csrfmiddlewaretoken', token);
		data.append('esc', esc);
		data.append('user', residente);
		data.append('fecha', fecha);

		$.ajax({
			type: 'POST',
			url: '/agendar/',
			data: data,
			dataType: 'json',
			cache: false,
			contentType: false,
			processData: false,
		}).done(function(al){
			if(al.success){
				alert('todo bien');
			}else{
				alert('ago salio mal');
			}
			
		});
		
	});


