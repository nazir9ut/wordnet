  $(function() {


    var $input = $('.typeahead');





        $('.btn_search').click(function(){

             console.log($input.val());



             $.get($SCRIPT_ROOT + '/_get_item', {value: $input.val()}, function(data){

                    console.log('_get_item');
                    console.log(data.giperonims_coll);




                    html = '';

                    if(data.aniktama){
                        html += '<h4> Анықтамасы  </h4>';
                        html += data.aniktama;

                        html += '<br>';
                        html += '<br>';
                    }


                    html += getHtml(data.giperonims_coll, 'Гипероним');

                    html += getHtml(data.giponims_coll, 'Гипоним');

                    html += getHtml(data.holonims_coll, 'Холоним');

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

                    if(value.is_zatesim){
                        html += '<b class="is_zatesim">' + value.lex_form + '</b>';
                    }
                    else{
                        html += value.lex_form;
                    }

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











    $( "#search_input" ).autocomplete({
      source: $SCRIPT_ROOT + '/_get_collection',
      minLength: 1,
      select: function( event, ui ) {

      }
    })
    .autocomplete("instance")._renderItem = function(ul, item){
        var append_text = '';



        if(item.is_zatesim == 1){
            append_text += '<strong>';
            append_text += item.label;
            append_text += '</strong>';
        }
        else{
            append_text += item.label;
        }




        return $('<li>')
        .append('<a>' +  append_text + '</a>')
        .appendTo(ul);
    };






    $('body').on('click', '.is_zatesim', function(){

        console.log('is_zatesim');


        var text = $(this).html();

         console.log(text);


         $('#search_input').val(text);


        $('.btn_submit').trigger('click');

    });




  });






