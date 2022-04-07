
function initializeTable() {
    // TODO
    $("#createLink").click(createCountry);
    addCountryCapital("Iran", "Tehran");
    addCountryCapital("Sweden", "Stockholm");
    addCountryCapital("Germany", "Berlin");
    actionSetting();
    
    function createCountry() {
        let country = $('#newCountryText').val();
        let capital = $('#newCapitalText').val();
        addCountryCapital(country, capital, true);
        $('#newCountryText').val('');
        $('#newCapitalText').val('');
        actionSetting();
    }
    function addCountryCapital(country, capital){
        let row = $('<tr>')
                    .append($("<td>").text(country))
                    .append($("<td>").text(capital))
                    .append($("<td>")
                        .append($("<a href='#' id='Down'>[Down]</a>").click(moveDown))
                        .append(" ")
                        .append($("<a href='#' id='up'>[Up]</a>").click(moveUp))
                        .append(" ")
                        .append($("<a href='#' id='del'>[Delete]</a>").click(del)));
        row.css('display', 'none');
        $("#countriesTable").append(row);
        row.fadeIn();
    }

    function moveUp(){

    }
    function moveDown(){
        
    }
    function del() {
        let row = $(this).parent().parent();
        row.fadeOut(function () {
            row.remove();
            actionSetting();
        });
    }

    function actionSetting(){
        $('#countriesTable a').css('display', 'inline');
        let tableRows = $('#countriesTable tr');
        $(tableRows[2]).find("a:contains('Up')")
                .css('display', 'none');
        
        $(tableRows[tableRows.length-1]).find("a:contains('Down')")
                .css('display', 'none');
    }
}