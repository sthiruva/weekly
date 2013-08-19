var row_num = 0;
var week_no;
var year_no;
$(function() {
    add_row();
    add_row();
    add_row();
    $('#add-row').click(add_row);
    $('.highlight').live("click", highlight_toggle);
    $('.rag').live("click", update_rag);
    $('#header-ul li').live("click", switch_tab);

    $('.sub-settings-option').live("click", show_sub_settings_del);
    $('.sub-settings-input').click(show_sub_settings_add);
    $('.sub-settings-input').bind('keypress', trigger_sub_settings_add);
    $('.sub-settings-add').click(sub_settings_add);
    $('.sub-settings-del').click(sub_settings_del);

    $('#save-report').click(save_report);
    $('#week').change(week_changed);


    add_weeks();
});


// On a week change, we should try and get the old weekly up 
// and update the gui
function week_changed()
{
    week_no = $('#week option:selected').val();
    year_no = $('#year option:selected').val();

    // to do.. load up the result
}

function add_weeks()
{

    var d = Date();
    // bad global var
    year_no =  getWeekNumber(d)[0];
    week_no =  getWeekNumber(d)[1];

    var sel = $('#week');

    for(var i = 0; i < 54; i++)
    {
        sel.append("<option value='" + i + "'> Week " + i + "  </option>")
    }

    //set the current week as selected
    sel.val(week_no).attr("selected", "selected");
}

function sub_settings_del()
{
    var url = window.location.pathname;
    var action = $(this).attr('action');
    $.ajax({
        url: url + "/" + action ,
        async: false
    });
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
        var action = $(this).attr('action');
        $.ajax({
            data:"ms=" + pc,
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


function add_row()
{
    var r = $('#hiddenrow').clone();
    var t = $('#report-table').append(r);
    r.show();
    r.attr('id', 'row-' + row_num);
    row_num++;
}

// TODO: 
// 1. get the week details
function save_report()
{
    var all_progress = $("#report-table .progress");

    var report_lines = [];

    for(var i = 0; i < all_progress.length; i++){
        var status_line = all_progress[i].children[1].value;
        var highlight   = (all_progress[i].children[2].className.indexOf("highlight-on") != -1);

        report_lines.push([status_line, highlight]);
    }


    var report_dict = {
        "report_array"  : report_lines,
        "week_no"       : week_no,
        "year_no"       : year_no
    }

    report_dict_string = JSON.stringify(report_dict);

    var url = window.location.pathname;
    var action = $(this).attr('action');
    $.ajax({
        data: "report_dict_string=" + report_dict_string,
        url: url + "/" + action ,
        async: false
    });


}


/* From:  http://stackoverflow.com/questions/6117814/get-week-of-year-in-javascript-like-in-php
 *
 * For a given date, get the ISO week number
 *
 * Based on information at:
 *
 *    http://www.merlyn.demon.co.uk/weekcalc.htm#WNR
 *
 * Algorithm is to find nearest thursday, it's year
 * is the year of the week number. Then get weeks
 * between that date and the first day of that year.
 *
 * Note that dates in one year can be weeks of previous
 * or next year, overlap is up to 3 days.
 *
 * e.g. 2014/12/29 is Monday in week  1 of 2015
 *      2012/1/1   is Sunday in week 52 of 2011
 */
function getWeekNumber(d) {
    // Copy date so don't modify original
    d = new Date(d);
    d.setHours(0,0,0);
    // Set to nearest Thursday: current date + 4 - current day number
    // Make Sunday's day number 7
    d.setDate(d.getDate() + 4 - (d.getDay()||7));
    // Get first day of year
    var yearStart = new Date(d.getFullYear(),0,1);
    // Calculate full weeks to nearest Thursday
    var weekNo = Math.ceil(( ( (d - yearStart) / 86400000) + 1)/7)
    // Return array of year and week number
    return [d.getFullYear(), weekNo];
}
