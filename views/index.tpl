%include header
<div id="report-table">
</div>
<div class="clear"></div>
<div id="hiddenrow" class="row">
    <div class='highlight'> 
        <div class="rag"></div>
        <hr/>
        <input type ="text" name="hours" placeholder="Hours"/>
        <div class="clear"></div>
        <input type="checkbox" title="Highlight"/>
        <div class="clear"></div>
        <select>
        	<option>Milestone 1</option>
        	<option>Milestone 2</option> 
        </select>
    </div>
    <div>
        <div class='progress'> 
            <h1> Progress</h1>
            <textarea class="progress-ta" onfocus="this.value=''; setbg('#e5fff3');" onblur="setbg('white')">Enter your progress here...</textarea>
        </div>
        <div class='progress'> 
            <h1>Dependency/Risk/Issues</h1>
            <textarea class="progress-ta" onfocus="this.value=''; setbg('#e5fff3');" onblur="setbg('white')">Enter the dependency/risk/issues...</textarea>
        </div>
    </div>
</div>
<div class="clear"></div>
<div class="report-table-footer">
    <div id='add-row' class="button">Add Row</div>
    <div id='submit-report' class="button">Submit Report</div>
    <div class="clear"></div>
</div>

%include footer
