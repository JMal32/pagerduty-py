import requests
import json

# Variables for API keys, project keys, and routing keys for PagerDuty, Slack, and Jira.
def main():
    pager_key = "ENTER YOUR PAGERDUTY ROUTING KEY"
    pager_token = "ENTER YOUR PAGERDUTY API KEY"
    jira_token = "ENTER YOUR JIRA API TOKEN"
    jira_key = "ENTER YOUR JIRA API KEY"
    slack_token = "ENTER YOUR SLACK API TOKEN"
    slack_key = "ENTER YOUR SLACK WEBHOOK URL" #I'm still not 100% what slack information is needed here. I will look it up later.


# Function to send alerts to PagerDuty.
def pd_alert(routing_key, summary, source, severity):
    url = "https://events.pagerduty.com/v2/enqueue"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "routing_key": routing_key,
        "event_action": "trigger",
        "payload": {
            "summary": summary,
            "source": source, 
            "severity": severity
        }
    }
    
