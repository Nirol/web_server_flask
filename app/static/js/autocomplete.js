//$(document).ready(function() {
//            $.ajax({
//                url: "http://rest-service.guides.spring.io/greeting"
//            }).then(function(data) {
//               $('.greeting-id').append(data.id);
//               $('.greeting-content').append(data.content);
//            });
//         });



$(function() {



    $("#autocomplete").autocomplete({
        source:function(request, response) {

            $.getJSON(view_autocomplete_path,{
                q: request.term,
            }, function(data) {
                response(data.matching_results);
            });
        },
        minLength: 2,
        select: function(event, ui) {
            console.log(ui.item.value);
        }
    });
})