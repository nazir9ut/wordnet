  $(function() {


    var $input = $('.typeahead');


//    $input.typeahead();



    $input.on('input',function(e){
                 $.get($SCRIPT_ROOT + '/_get_collection', {value: $input.val()}, function(data){



                 $input.typeahead({source: data.result});

            },'json');
    });





        $('.btn_search').click(function(){

             console.log($input.val());



//            $input.trigger('input');





//             $.get($SCRIPT_ROOT + '/_get_collection', function(data){
//                $("#mytype").typeahead({ source:data.result });
//            },'json');

        });










//    $input.change(function() {
//
//        console.log('change');
//
//        var current = $input.typeahead("getActive");
//
//        if (current) {
//
//            console.log('current');
//
//
//
////            // Some item from your model is active!
////            if (current.name == $input.val()) {
////                // This means the exact match is found. Use toLowerCase() if you want case insensitive match.
////            }
////            else {
////                // This means it is only a partial match, you can either add a new item
////                // or take the active if you don't want new items
////            }
//
//        }
//        else {
//            // Nothing is active so it is a new value (or maybe empty value)
//        }
//
//    });






//    $('a#calculate').bind('click', function() {

//      $.getJSON($SCRIPT_ROOT + '/_add_numbers', {
//        a: $('input[name="a"]').val(),
//        b: $('input[name="b"]').val()
//      }, function(data) {
//        $("#result").text(data.result);
//      });


//        $.post($SCRIPT_ROOT + '/_add_numbers',
//        {
//            a: $('input[name="a"]').val(),
//            b: $('input[name="b"]').val()
//        },
//        function(result) {
//
//            console.log(result);
//
//        }, "json");




//        $('.typeahead').typeahead();



//        $('#mytype').input(function(){
//
//             console.log('mytype');
//
//             $.get($SCRIPT_ROOT + '/_get_collection', function(data){
//                $("#mytype").typeahead({ source:data.result });
//            },'json');
//
//        });










//    });


  });

