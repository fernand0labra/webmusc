// Fills the hidden input field with the text of the selected comboBox option
function alterTtype(){
    // Obtain the ComboBox object
    var combObject = document.getElementById('ttypeCombo');

    // Obtain the text of the selected element
    var ttype = combObject.options[combObject.selectedIndex].text;

    // Fill the hidden input field
    document.getElementById('ttype').value = ttype;
}


// When a row of the Query Results is double clicked fills the hidden input fields
// and sends the form
function openDetails(){
    // Object that received the event
    var cell = event.target;
    // Index of the row
    var rowIndex = cell.parentNode.rowIndex;
    // Collection of Row Objects of the Table
    var rows = document.getElementsByClassName("table_row")

    // Information of each cell
    // rowIndex -1 because it counts the heading row
    var nameOutput = rows[rowIndex-1].cells[0]
    var opusOutput = rows[rowIndex-1].cells[1]

    // If there is information in the cells
    if(nameOutput.innerHTML != "" && nameOutput.innerHTML != "NO INFO"){
        // Fill the hidden input fields
        document.getElementById('name').value = nameOutput.innerHTML
        document.getElementById('opus').value = opusOutput.innerHTML

        // Obtain the form object
        var form = document.getElementById("query2")
        // Submit the form
        form.submit()
    }
}