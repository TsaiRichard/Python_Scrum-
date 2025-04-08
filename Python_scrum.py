# to install Jira lib
# pip install jira >> to be inputted in the CMD
# import the installed Jira library 
from jira import JIRA 
# Specify a server key. It should be your 
# domain name link. yourdomainname.atlassian.net 
jiraOptions = {'server': "https://pelotoncycle.atlassian.net"} 

# Get a JIRA client instance, pass, 
# Authentication parameters 
# and the Server name. 
# emailID = your emailID 
# token = token you receive after registration 
jira = JIRA(options=jiraOptions, basic_auth=( 
    "richard.tsai@onepeloton.com", "ATATT3xFfGF0b2nE6a8hUyNh6XG3PIh-d9mgEhC9XyHAa7HP05NUF-mKD-XwFj7M_Dq9n7Rpgvp5LFTBLOsA-wNSqeLmReS5PIr330fbnWgH3jIS0uuzFKTBVrHHdIK8zgBbkCS9V0wVtgZjLbQQib_l8RLW2j8q50Lpx05_N8AWsXPpEg2rMWg=29CC3AD2"))

    # Search all issues mentioned against a project name. 
for singleIssue in jira.search_issues(jql_str='project = HWQAT',startAt = 0, maxResults = 100): 
    print('{}: {}:{}'.format(singleIssue.key, singleIssue.fields.summary, 
                             singleIssue.fields.reporter.displayName))  