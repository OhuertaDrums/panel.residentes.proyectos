
//$("#datepicker").datepicker({
//   	onSelect: function(){
//  		var dato = $(this).datepicker('getDate');
//   		console.log("La fecha actual es:" + dato);
//   		//alert($("#datepicker").data("dato"));
//   	}
//});




$("#datepicker").datepicker({
   	onSelect: function(dato){
		minDate: 0

   		//alert(dato);
   		$("#escuela").data(dato);
   		console.log(dato);

   	}
});

