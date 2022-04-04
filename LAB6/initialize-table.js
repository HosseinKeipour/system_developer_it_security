
function initializeTable() {
    // TODO
    
    
    
    function createCountry() {
        let country = $('#newCountryText').val();
        let capital = $('#newCapitalText').val();
        addCountryCapital(country, capital, true);
        $('#newCountryText').val('');
        $('#newCapitalText').val('');
        actionSetting();
    }
    function addCountryCapital(country, capital){
        newRow = $("<tr>").append("<td>"+text(country)).append("<td>"+text(capital)).append("<td>"+text(<a href="#" id="down">[Down]</a>))
    }

    function moveUp(){

    }
    function moveDown(){
        
    }
    function del(){
        
    }
    function moveRowUp(){
        
    }
    function actionSetting(){

    }
}