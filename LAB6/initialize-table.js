
function initializeTable() {
    // TODO
    $("#createLink").click(createCountry);
    
    
    function createCountry() {
        let country = $('#newCountryText').val();
        let capital = $('#newCapitalText').val();
        addCountryCapital(country, capital, true);
        $('#newCountryText').val('');
        $('#newCapitalText').val('');
        actionSetting();
    }
    function addCountryCapital(country, capital){
        let Row = $('<tr>')
                    .append($("<td>").text(country))
                    .append($("<td>"+text(capital))
                    .append($("<td>")
                        .append($("<a href='#'>id='down'</a>").click(moveDown))
                        .append(" ")
                        .append($("<a href='#' id='up'>[Up]</a>").click(moveUp))
                        .append(" ")
                        .append($("<a href='#' id='del'>[Delete]</a>").click(del)));
        Row.css('display', 'none');
        $("#countriesTable").append(Row);
        Row.fadeIn();
                    }

    function moveUp(){

    }
    function moveDown(){
        
    }
    function del(){
        
    }

    function actionSetting(){

    }
}