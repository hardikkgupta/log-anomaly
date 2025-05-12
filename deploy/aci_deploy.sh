#!/bin/bash
# Deploys the log-anomaly-agent container to Azure Container Instances

RESOURCE_GROUP="your-resource-group"
ACI_NAME="log-anomaly-agent"
IMAGE="yourdockerhubusername/log-anomaly-agent:latest"
EVENT_HUB_CONN_STR="<your-event-hub-connection-string>"
EVENT_HUB_NAME="<your-event-hub-name>"

az container create \
  --resource-group $RESOURCE_GROUP \
  --name $ACI_NAME \
  --image $IMAGE \
  --cpu 1 --memory 1.5 \
  --restart-policy OnFailure \
  --environment-variables EVENT_HUB_CONN_STR="$EVENT_HUB_CONN_STR" EVENT_HUB_NAME="$EVENT_HUB_NAME" 