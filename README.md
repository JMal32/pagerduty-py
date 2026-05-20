# pagerduty-py

A learning project exploring how PagerDuty, Jira, and Slack APIs interact —
prototyping a tiny pipeline that turns PagerDuty incidents into Jira tickets
and Slack messages.

> **Status: work-in-progress / learning project.** This is the kind of
> automation I'd want to write on the job. Today it sketches the PagerDuty
> event-trigger payload and the surrounding orchestration shape; the
> Jira/Slack legs are partially stubbed. The goal is the *integration
> pattern*, not a production tool.

## What's here

- `alerts.py` — `pd_alert(routing_key, summary, source, severity)` builds and
  (will) POST a PagerDuty Events API v2 trigger payload, plus a `main()`
  scaffold that loads API keys/tokens for PagerDuty, Jira, and Slack.

## What I learned working on this

- PagerDuty Events API v2 payload shape (`routing_key`, `event_action`,
  severity tiers)
- Jira REST API authentication and ticket-creation flow
- Slack incoming webhooks vs. Slack Web API tokens (and which one you
  actually want for a given use case)
- Keeping secrets out of source — even a placeholder-only repo should
  obviously never hard-code real keys

## Configuration

`alerts.py` reads credentials from variables at the top of `main()`. For a
real deployment these should come from environment variables or a secrets
manager, not source. Required values:

| Variable | Source |
|---|---|
| `pager_key` | PagerDuty integration routing key |
| `pager_token` | PagerDuty REST API token |
| `jira_token`, `jira_key` | Jira API token and project key |
| `slack_token`, `slack_key` | Slack bot token and webhook URL |

## Run

```sh
python3 alerts.py
```

## Author

Justin Malone — [@JMal32](https://github.com/JMal32)
