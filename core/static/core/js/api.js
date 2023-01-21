$(document).ready(function(){
    $("#enviar").click(function(){
    $.get("https://www.themealdb.com/api/json/v1/1/categories.php",
        function(data){
        //En data se capturan todos los datos del servicio
        $.each(data.categories, function(i, item){
            //por cada elemento agrgaremos una nueva fila en la tabla categorias
            $("#categoria").append("<tr><td>"+item.idCategory+"</td>"+
                                    "<td>"+item.strCategory+"</td>"+
                                    '<td><img src="'+item.strCategoryThumb+'"></img>'+"</td>"+
                                    "<td>"+item.strCategoryDescripcion+"</td></tr>");

                                });
                            });
                        });
                    })

