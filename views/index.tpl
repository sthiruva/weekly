%include header
<div id="report-table">
</div>

<div id="hiddenrow" class="row">
    <div class='highlight'> 
        <h1> RAG</h1>
        <div class="rag"></div>
        <h1> Highlight</h1>
        <input type="checkbox" />
        <h1> Milestone </h1>
        <select> </select>
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
    <div id='add-row'>Add Row</div>
    <div id='submit-report'>Submit Report</div>
</div>
%include footer
