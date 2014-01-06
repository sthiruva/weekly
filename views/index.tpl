%include header
<div class='tab weekly selected'>

    <div id="report-table">
        <div id="week-info" >
            <select id="week" autofocus>
            </select> 

            <select id="year">
            </select> 

        </div>

    </div>
    <div class="clear"></div>

    <div id="hiddenrow" class="row">
        <div class='report'>
            <div class='progress'> 
                <h1> Progress</h1>
                <textarea class="progress-ta" title="Enter your progress here..."></textarea>

                <button title="Highlight" class="highlight-off highlight"> Highlight</button>

            </div>
        </div>

    </div>
    <div class="clear"></div>

    <div class="report-table-footer">
        <button id='add-row' class="button">Add Row</button>
        <div class="clear"></div>
    </div>

    <div class='dri'> 
        <h1>Dependency/Risk/Issues</h1>
        <textarea id='dri-ta-id' class="dri-ta" title="Enter the dependency/risk/issues..."></textarea>
    </div>
    <div>
        <button id='save-report' class="button" action="save_report">Save Report</button>
    </div>

    <div>
        <button id='send-report' class="button" action="send_report">Send Report</button>
    </div>

    <div class="clear"></div>
    <div>
        <button id='send-consolidated-report' class="button" action="send_consolidate_report">Send Consolidated Report</button>
    </div>
</div>
<div class='tab older-weekly'>
</div>

<div class='tab settings'>
    <div class='ms-settings sub-settings'>
        <h1> MileStones</h1>
        <select id="ms-select" class="sub-settings-select" title="Add your milestones" size=3></select>
        <div class="clear"></div>
        <input type="text" id='ms-input' class="sub-settings-input" > </input>
        <div id="ms-add"  class="button sub-settings-add" action="addms" >Add Milestone</div>
        <div id="ms-del"  class="button sub-settings-del" action="delms" >Del Milestone</div>
        <div class="clear"></div>
    </div>

    <div class='ms-settings sub-settings'>
        <h1> Add Project codes of project you are working on</h1>
        <select id="pc-select" class="sub-settings-select" title="Project Codes" size=3>
            <option disabled="disabled" >Holiday</option> 
        </select>
        <div class="clear"></div>
        <input id="pc-input" type="text" class='sub-settings-input' > </input>
        <div id="pc-add" class="button sub-settings-add" action="addpc">Add Project Code</div>
        <div id="pc-del" class="button sub-settings-del" action="delpc">Del Project Code</div>
        <div class="clear"></div>
    </div>

    <div class='ms-settings sub-settings'>
        <h1> Add Email ids of people who you want to send the Weekly to</h1>
        <select id="email-select" class="sub-settings-select" title="Project Codes" size=3></select>
        <div class="clear"></div>
        <input type="text" id='email-input' class="sub-settings-input" > </input>
        <div id="email-add" class="button sub-settings-add" action="addemail">Add Email ids</div>
        <div id="email-del" class="button sub-settings-del" action="delemail">Del Email ids</div>
        <div class="clear"></div>
    </div>
</div>

<div class='tab help'>
</div>

%include footer
