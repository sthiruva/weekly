%include header
<form>

<div id="report-table">
    <div id="row-1" class="row">
        <div class='highlight'> 
            <h1> Highlight</h1>
            <input type="checkbox" />
        </div>
        <div>
            <div class='progress'> 
                <h1> Progress</h1>
                <textarea class="progress-ta" onfocus="this.value=''; setbg('#e5fff3');" onblur="setbg('white')">Enter your progress here...</textarea>
            </div>
            <div class="clear"></div>
            <div class='progress'> 
                <h1> Progress</h1>
                <textarea class="progress-ta" onfocus="this.value=''; setbg('#e5fff3');" onblur="setbg('white')">Enter your progress here...</textarea>
            </div>
        </div>

    </div>
        <th> Progress </th>
        <th> Hours </th>
        <th> DRI </th>
        <th> RAG </th>
        <th> Milestone </th>
    <tr>
    <tr>
        <td> <input type="checkbox" /> </td>
        <td> <input type="textbox"  /> </td>
        <td> <input type="textbox"  /> </td>
        <td> <input type="textbox"  /> </td>
        <td> <input type="hidden"  value="green" /> <div> </div></td>
        <td> <select> </select> </td>
    <tr>

</table>

</form>
%include footer
