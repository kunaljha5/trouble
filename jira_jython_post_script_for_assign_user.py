import com.atlassian.jira.component.ComponentAccessor
from com.atlassian.jira.component import ComponentAccessor
import com.atlassian.jira.issue.CustomFieldManager
import com.atlassian.jira.issue.fields.CustomField
from com.atlassian.jira.issue.customfields.manager import OptionsManager




#yagyemang  will be the default assignee
#assignee = ComponentAccessor.getUserManager().getUser("USERNAME1")
optionsManager = ComponentAccessor.getComponent(OptionsManager)
field = ComponentAccessor.getCustomFieldManager().getCustomFieldObjectByName('TEAMNAME')
fieldConfig = field.getRelevantConfig(issue)
options = optionsManager.getOptions(fieldConfig)
issueType = issueType = issue.getIssueTypeObject().getName()




if (issueType == "ISSUE TYPE1"):
    assignee = ComponentAccessor.getUserManager().getUser("SAMPLE_USERID1")
    issue.setAssignee(assignee)
    teamtag= "TEAMNAME1"
    for option in options:
        if option.getValue() == teamtag:
            issue.setCustomFieldValue(field, option)
            break


if (issueType == "ISSUE TYPE2"):
    teamtag= "TEAMNAME2"
    for option in options:
        if option.getValue() == teamtag:
            issue.setCustomFieldValue(field, option)
            break

### Assigne ticket to variable named assignee
#issue.setAssignee(assignee)


