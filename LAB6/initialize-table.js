
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
        newRow = $("<tr>")
                    .append("<td>"+text(country))
                    .append("<td>"+text(capital))
                    .append(("<td>")
                        .append($(<a href="#" id="down">[Down]</a>).click(moveDown))
                        .append($(<a href="#" id="up">[Up]</a>).click(moveUp))
                        .append($(<a href="#" id="del">[Delete]</a>).click(del)));
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