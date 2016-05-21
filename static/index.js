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



             $.get($SCRIPT_ROOT + '/_get_item', {value: $input.val()}, function(data){

                    console.log('_get_item');
                    console.log(data.giperonims_coll);




                    html = '';
                    html += getHtml(data.giperonims_coll, 'Гипероним');
                    html += getHtml(data.giponims_coll, 'Гипоним');
                    html += getHtml(data.meronims_coll, 'Мероним');
                    html += getHtml(data.sinonims_coll, 'Синоним');
                    html += getHtml(data.omonims_coll, 'Онтоним');
                    html += getHtml(data.ontonims_coll, 'Омоним');


                    $('.content_block').html(html);


            },'json');

        });







        /**
        *
        */
        function getHtml(arr, header){

           html = ''

           if(arr.length){
               html += '<h4>' + header + '</h4>';

               html += '<ul>';

                $.each( arr, function( index, value ){
                    console.log(value);

                    html += '<li>';
                    html += value.lex_form;
                    html += '</li>';

                });

                html += '</ul>';
            }

            return html;

        }












        $(document).ajaxStart(function() {
            $("#loading_div").show();
        });

        $(document).ajaxStop(function() {
            $("#loading_div").hide();
        });








  });

