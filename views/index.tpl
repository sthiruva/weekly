%include header
<div id="report-table">
</div>
<div class="clear"></div>
<div id="hiddenrow" class="row">
    <div class='report'>
        <select>
        	<option>Milestone 1</option>
        	<option>Milestone 2</option> 
        </select>
        <div class="clear"></div>
        <div class='progress'> 
            <h1> Progress</h1>
            <textarea class="progress-ta" onfocus="this.value=''; setbg('#e5fff3');" onblur="setbg('white')">Enter your progress here...</textarea>
        </div>
        <div class='progress'> 
            <h1>Dependency/Risk/Issues</h1>
            <textarea class="progress-ta" onfocus="this.value=''; setbg('#e5fff3');" onblur="setbg('white')">Enter the dependency/risk/issues...</textarea>
        </div>
    </div>
    <div class='status'> 
        <div class="rag" title="RAG"></div>
        <div class="clear"></div>
        <div class="hours">
            <input type ="text" name="hours" title="Hours";>
        </div>
        <div class="clear"></div>
        <div title="Highlight" class="highlight-off highlight"> Highlight</div>
        <div class="clear"></div>
    </div>
</div>
<div class="clear"></div>
<div class="report-table-footer">
    <div id='add-row' class="button">Add Row</div>
    <div id='submit-report' class="button">Submit Report</div>
    <div class="clear"></div>
</div>

%include footer
