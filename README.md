Overview

This lab simulates a real Security Operations Center (SOC) workflow by collecting, ingesting, and analyzing Windows Security Event Logs using Splunk Enterprise.

The objective was to detect and investigate authentication activity — specifically failed login attempts (Event ID 4625) — and create automated alerts similar to what a SOC Analyst would monitor in a production environment.




Lab Objectives

Configure centralized log collection from Windows Event Viewer

Forward security logs into a SIEM (Splunk)

Identify suspicious authentication activity

Detect brute-force login behavior

Create automated security alerts

Practice analyst investigation workflows




Lab Architecture

Environment Components:

Host Machine: Windows 10/11

SIEM Platform: Splunk Enterprise

Log Source: Windows Security Event Logs

Log Forwarder: Splunk Universal Forwarder

Data Flow:

Windows Event Viewer
        ↓
Splunk Universal Forwarder
        ↓
Splunk Indexer (Port 9997)
        ↓
Splunk Search & Alerting Dashboard



Configuration Steps
Install Splunk Enterprise

Installed Splunk Enterprise on host system

Accessed web interface via:

http://localhost:8000



Install Splunk Universal Forwarder

Configured forwarder to send logs to the indexer:

Receiver IP: <Host IP>
Port: 9997

Verified forwarding status:

active forwards: <IP>:9997



Enable Windows Security Log Collection

Configured inputs to monitor:

Windows Security Event Logs

Key monitored events:

4625 — Failed Logon

4624 — Successful Logon

4720 — User Account Created

4726 — User Account Deleted




Create Splunk Index

Created dedicated index:

wineventlog_lab

Purpose:

Separate lab telemetry from default logs

Simulate enterprise log organization




Detection & Analysis
Failed Login Search
index=wineventlog_lab EventCode=4625
| table _time Account_Name Logon_Type Workstation_Name
| sort - _time

This query identifies failed authentication attempts and displays:

Timestamp

Username

Logon type

Source workstation

Brute Force Detection Logic

Indicators analyzed:

Multiple failed logins within short time window

Repeated attempts against same account

Interactive logon attempts (Logon Type 7)




Alert Creation

Created scheduled alert in Splunk:

Trigger Conditions

EventCode = 4625 detected

Runs on cron schedule (every 5 minutes)

Alert Actions

Generate triggered alert

SOC analyst review required

This simulates real SOC monitoring workflows.




Skills Demonstrated

SIEM deployment and configuration

Log ingestion & normalization

Windows Event Log analysis

Security monitoring concepts

Threat detection fundamentals

Alert engineering

SOC investigation workflow




SOC Analyst Relevance

This lab mirrors real Tier-1 SOC responsibilities:

Monitoring authentication alerts

Investigating suspicious login activity

Validating security events

Escalating potential incidents




Future Improvements

Add Linux log ingestion

Implement correlation rules

Integrate MITRE ATT&CK mapping

Forward logs from multiple endpoints

Build dashboard visualizations




Author

Dozie Enwerem
Aspiring SOC Analyst | CompTIA Security+ Certified
Hands-on labs focused on SIEM, log analysis, and threat detection.
