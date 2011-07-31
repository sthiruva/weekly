var row_num = 0;
$(function() {
    addRow();
    $('#add-row').click(addRow);
    $('.highlight').live("click", highlight_toggle);
    $('.rag').live("click", update_rag);
    $('#header-ul li').live("click", switch_tab);

    $('.sub-settings-option').live("click", show_sub_settings_del);
    $('.sub-settings-input').click(show_sub_settings_add);
    $('.sub-settings-input').bind('keypress', trigger_sub_settings_add);
    $('.sub-settings-add').click(sub_settings_add);
    $('.sub-settings-del').click(sub_settings_del);

});

function sub_settings_del()
{
    var sib = $(this).parent().find('.sub-settings-select option:selected').remove();
}

function show_sub_settings_del()
{
    if($(this).parent().siblings('.sub-settings-del').css('display') == 'none')
    {
        $(this).parent().siblings('.sub-settings-del').css('display', 'block')
        $(this).parent().siblings('.sub-settings-add').css('display', 'none')
    }
}

function show_sub_settings_add()
{
    if($(this).siblings('.sub-settings-add').css('display') == 'none')
    {
        $(this).siblings('.sub-settings-del').css('display', 'none')
        $(this).siblings('.sub-settings-add').css('display', 'block')
    }
}

function trigger_sub_settings_add(e)
{
    var code = (e.keyCode ? e.keyCode : e.which);
    if(code == 13) { //Enter keycode
        $(this).siblings('.sub-settings-add').trigger('click')
        sub_settings_add();
    }
}

function sub_settings_add()
{
    var pc = $(this).siblings('.sub-settings-input').val();

    if(pc != "")
    {
        var url = window.location.pathname;
        var action = $(this).siblings('.sub-settings-action').val();
        $.ajax({
            url: url + "/" + action ,
            async: false
        });
        var opt = "<option class='sub-settings-option' value=" + pc + ">" + pc + "</option>";
        $(this).siblings('.sub-settings-select').prepend(opt);
        $(this).siblings('.sub-settings-input').val("");
    }
}

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

