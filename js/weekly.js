var row_num = 0;
$(function() {
    addRow();
    $('#add-row').click(addRow);
});


function addRow()
{
    var r = $('#hiddenrow').clone();
    var t = $('#report-table').append(r);
    r.show();
    r.attr('id', 'row-' + row_num);
    row_num++;
}
