%include header
<div class='tab weekly'>
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

<div class='tab settings selected'>
    <div class='ms-settings'>
        <h1> MileStones</h1>
        <select id="ms-select" title="Add your milestones" size=3></select>
        <div class="clear"></div>
        <input type="text" id='ms-input'> </input>
        <div class="button" id="ms-add">Add Milestone</div>
        <div class="clear"></div>
    </div>

    <div class='ms-settings'>
        <h1> Add Project codes of project you are working on</h1>
        <select id="pc-select" title="Project Codes" size=3></select>
        <div class="clear"></div>
        <input type="text" id='pc-input'> </input>
        <div class="button" id="pc-add">Add Project Code</div>
        <div class="clear"></div>
    </div>

    <div class='ms-settings'>
        <h1> Add Email ids of people who you want to send the Weekly to</h1>
        <select id="email-select" title="Project Codes" size=3></select>
        <div class="clear"></div>
        <input type="text" id='email-input'> </input>
        <div class="button" id="email-add">Add Email ids</div>
        <div class="clear"></div>
    </div>
</div>

<div class='tab help'>
</div>

%include footer
