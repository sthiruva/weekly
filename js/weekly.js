var row_num = 0;
$(function() {
    addRow();
    $('#add-row').click(addRow);
    $('.highlight').live("click", highlight_toggle);
    $('.rag').live("click", update_rag);
    $('#header-ul li').live("click", switch_tab);

});

function switch_tab()
{
    $('#header-ul li').removeClass("selected");
    cl = $(this).attr('class');
    $(this).addClass("selected");
    $('.tab').removeClass('selected');
    $('.' + cl).addClass('selected');
}

function highlight_toggle()
{
    var cname = $(this).attr('class');
    if(cname.indexOf('highlight-off') != -1)
    {
        $(this).removeClass('highlight-off');
        $(this).addClass('highlight-on');
    }
    else
    {
        $(this).removeClass('highlight-on');
        $(this).addClass('highlight-off');
    }
}

var NEXT_COLOR = {
    'red'   : 'orange',
    'orange' : 'green',
    'green' : 'red'
};

function update_rag()
{
    var inp = $('input', this);

    var color = inp.val();

    color = NEXT_COLOR[color];
    inp.val(color);
    $(this).css('background-color', color);
}


function addRow()
{
    var r = $('#hiddenrow').clone();
    var t = $('#report-table').append(r);
    r.show();
    r.attr('id', 'row-' + row_num);
    row_num++;
}

