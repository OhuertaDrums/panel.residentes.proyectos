//token de django
var token = csrftoken;
//URL a donde va mandar la peticion en este caso /ver-citas
var url_page = '/ver-citas'
//Idioma
var idioma = {
  "sProcessing":     "Procesando...",
  "sLengthMenu":     "Mostrar _MENU_ registros",
  "sZeroRecords":    "No se encontraron resultados",
  "sEmptyTable":     "Ningún dato disponible en esta tabla",
  "sInfo":           "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
  "sInfoEmpty":      "Mostrando registros del 0 al 0 de un total de 0 registros",
  "sInfoFiltered":   "(filtrado de un total de _MAX_ registros)",
  "sInfoPostFix":    "",
  "sSearch":         "Buscar:",
  "sUrl":            "",
  "sInfoThousands":  ",",
  "sLoadingRecords": "Cargando...",
  "oPaginate": {
    "sFirst":    "Primero",
    "sLast":     "Último",
    "sNext":     "Siguiente",
    "sPrevious": "Anterior"
  },
  "oAria": {
    "sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
    "sSortDescending": ": Activar para ordenar la columna de manera descendente"
  }
}
$(document).ready(function(){
  // Estableces las dimenciones de las columnas
  var columna_de_la_tabla = [{
      sWidth: '25%',
      'className': 'text-center',
      bSortable: false,
    },{
      sWidth: '25%',
      'className': 'text-center',
      bSortable: false,
    },{
      sWidth: '25%',
      'className': 'text-center',
      bSortable: false,
    }];
  // Estableces los parametros a la datatable
  var datos_residente = $('#_citas').DataTable({
    //propiedades de la tabla esto pede variar de acuerdo de como lo quieres.
    "sDom": 'l<"toolbar">frtip',
    'responsive': true,
    'bProcessing': true,
    'bServerSide': true,
    'columns': columna_de_la_tabla,
    'columnDefs': [
      {
        "targets": [0,1,2],
      },
    ],
    'language': idioma,
    'stateSave': true,
    'searching': false,
    sAjaxSource: url_page, //url de la pagina para pa peticion ajax
    'fnServerData': function(ver_citas, aoData, fnCallback){
      // EL toquen de la seccion
      aoData.push({
        'name': 'csrfmiddlewaretoken',
        'value': token,
      });
      // El parameto opccion para evaluar en la vista
      aoData.push({
        'name': 'opccion',
        'value': 'datable_citras',
      });
      // Aqui haces la peticion ajax de la tabla
      $.ajax({
        'dataType': 'json',
        'type': 'POST',
        'url': ver_citas,
        'data': aoData, 
        'success': function(respuesta){
          //aqui es donde llenas la tabla con el diccionario que regresas con el JsonResponse() en la vista
          fnCallback(respuesta.objecto);
        }
      });
    },
  });
});