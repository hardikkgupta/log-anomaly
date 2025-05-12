import os
import time
from datetime import datetime
from azure.eventhub import EventHubConsumerClient
from azure.monitor import MonitorClient
from azure.identity import DefaultAzureCredential
from model import detect_anomaly

CONNECTION_STR = os.getenv('EVENT_HUB_CONN_STR', 'YourEventHubConnectionString')
EVENTHUB_NAME = os.getenv('EVENT_HUB_NAME', 'YourEventHubName')
SUBSCRIPTION_ID = os.getenv('AZURE_SUBSCRIPTION_ID')
RESOURCE_GROUP = os.getenv('AZURE_RESOURCE_GROUP')
WORKSPACE_NAME = os.getenv('LOG_ANALYTICS_WORKSPACE_NAME')

# For demonstration, we accumulate numeric log metrics
log_metrics = []

def send_to_azure_monitor(value, is_anomaly, severity="Warning"):
    """Send metrics and alerts to Azure Monitor"""
    try:
        credential = DefaultAzureCredential()
        monitor_client = MonitorClient(credential)
        
        # Send metric
        monitor_client.metrics.create(
            resource_uri=f"/subscriptions/{SUBSCRIPTION_ID}/resourceGroups/{RESOURCE_GROUP}/providers/Microsoft.OperationalInsights/workspaces/{WORKSPACE_NAME}",
            metric_name="LogAnomalyScore",
            timespan=f"{datetime.utcnow().isoformat()}/{datetime.utcnow().isoformat()}",
            interval="PT1M",
            metric_namespace="LogAnomaly",
            value=value
        )
        
        # If anomaly detected, send alert
        if is_anomaly:
            monitor_client.alerts.create_or_update(
                resource_group_name=RESOURCE_GROUP,
                alert_name=f"log-anomaly-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}",
                alert={
                    "location": "global",
                    "properties": {
                        "severity": severity,
                        "description": f"Anomaly detected in log metrics: {value}",
                        "enabled": True,
                        "scopes": [f"/subscriptions/{SUBSCRIPTION_ID}/resourceGroups/{RESOURCE_GROUP}/providers/Microsoft.OperationalInsights/workspaces/{WORKSPACE_NAME}"],
                        "evaluationFrequency": "PT1M",
                        "windowSize": "PT5M",
                        "criteria": {
                            "odata.type": "Microsoft.Azure.Monitor.SingleResourceMultipleMetricCriteria",
                            "allOf": [
                                {
                                    "name": "Metric1",
                                    "metricName": "LogAnomalyScore",
                                    "operator": "GreaterThan",
                                    "threshold": value,
                                    "timeAggregation": "Average"
                                }
                            ]
                        }
                    }
                }
            )
    except Exception as e:
        print(f"Error sending to Azure Monitor: {e}")

def on_event(partition_context, event):
    global log_metrics
    # Assume event body is a numeric metric for simplicity
    try:
        value = float(event.body_as_str())
        log_metrics.append(value)
        if len(log_metrics) > 100:
            log_metrics.pop(0)
        anomalies = detect_anomaly(log_metrics)
        is_anomaly = len(log_metrics) - 1 in anomalies
        
        # Send to Azure Monitor
        send_to_azure_monitor(value, is_anomaly)
        
        if is_anomaly:
            print(f"Anomaly detected: {value} at index {len(log_metrics)-1}")
    except Exception as e:
        print(f"Error processing event: {e}")
    partition_context.update_checkpoint(event)


def main():
    client = EventHubConsumerClient.from_connection_string(
        CONNECTION_STR,
        consumer_group="$Default",
        eventhub_name=EVENTHUB_NAME
    )
    try:
        with client:
            client.receive(
                on_event=on_event,
                starting_position="-1",  # from beginning
            )
    except KeyboardInterrupt:
        print("Stopped by user.")

if __name__ == "__main__":
    main() 