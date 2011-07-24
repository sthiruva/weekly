%include header
<div class='tab weekly selected'>
    <div id="report-table">
    </div>
    <div class="clear"></div>
    <div id="hiddenrow" class="row">
        <div class='report'>
            <select class="milestones">
                    <option>Milestone 1</option>
                    <option>Milestone 2</option> 
            </select>
            <div class="clear"></div>
            <div class='progress'> 
                <h1> Progress</h1>
                <textarea class="progress-ta" title="Enter your progress here..."></textarea>
            </div>
            <div class='progress'> 
                <h1>Dependency/Risk/Issues</h1>
                <textarea class="progress-ta" title="Enter the dependency/risk/issues..."></textarea>
            </div>
        </div>
        <div class='status'> 
            <select class="project">
                    <option>Holiday</option>
                    <option>PR431</option> 
            </select>
            <div class="clear"></div>
            <div class="rag" title="RAG"><input type="hidden" value="red" /></div>
            <div class="clear"></div>
            <div class="hours">
                <input type ="text" name="hours" title="Hours" value="0h" />
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
</div>
<div class='tab older-weekly'>
</div>

<div class='tab settings'>
</div>

<div class='tab help'>
</div>

%include footer
