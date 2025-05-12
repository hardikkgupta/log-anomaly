# 🚨 Log-Anomaly Detection Agent on Azure

[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat&logo=microsoft-azure&logoColor=white)](https://azure.microsoft.com)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

<div align="center">
  <img src="https://raw.githubusercontent.com/yourusername/log-anomaly-agent/main/docs/architecture.png" alt="Architecture Diagram" width="600"/>
</div>

## 📋 Overview

A production-grade, real-time log anomaly detection system that leverages Azure's powerful cloud services to provide scalable, reliable, and automated monitoring of application logs. The system detects anomalies using machine learning, triggers alerts, and automates incident response.

### ✨ Key Features

- 🔄 Real-time log streaming with Azure Event Hubs
- 🤖 ML-powered anomaly detection
- 🚀 Scalable containerized deployment
- 🔔 Automated alerting and notifications
- 📊 Comprehensive monitoring and metrics
- 🔄 Zero-downtime updates with AKS

## 🏗️ Architecture

The system is built on a modern, cloud-native architecture:

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Log Ingestion** | Azure Event Hubs | Real-time log streaming |
| **Anomaly Detection** | Python ML Model | Pattern recognition and anomaly detection |
| **Container Runtime** | Azure Container Instances / AKS | Scalable deployment |
| **Monitoring** | Azure Monitor | Metrics and alerting |
| **Automation** | Logic Apps | Incident response and notifications |

## 🚀 Getting Started

### Prerequisites

- Azure subscription
- Python 3.11+
- Docker
- Azure CLI
- kubectl (for AKS deployment)

### 1️⃣ Local Development

```bash
# Clone the repository
git clone https://github.com/yourusername/log-anomaly-agent.git
cd log-anomaly-agent

# Set up Python environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt

# Configure environment variables
export EVENT_HUB_CONN_STR="your-connection-string"
export EVENT_HUB_NAME="your-event-hub"
export AZURE_SUBSCRIPTION_ID="your-subscription-id"
export AZURE_RESOURCE_GROUP="your-resource-group"
export LOG_ANALYTICS_WORKSPACE_NAME="your-workspace"

# Run the agent
cd anomaly_detector
python consumer.py
```

### 2️⃣ Container Deployment

```bash
# Build the container
docker build -t log-anomaly-agent .

# Run locally
docker run -e EVENT_HUB_CONN_STR=... \
           -e EVENT_HUB_NAME=... \
           -e AZURE_SUBSCRIPTION_ID=... \
           -e AZURE_RESOURCE_GROUP=... \
           -e LOG_ANALYTICS_WORKSPACE_NAME=... \
           log-anomaly-agent
```

### 3️⃣ Azure Deployment

#### Azure Container Instances (ACI)
```bash
# Deploy to ACI
./deploy/aci_deploy.sh
```

#### Azure Kubernetes Service (AKS)
```bash
# Deploy to AKS
kubectl apply -f deploy/aks/
```

## 🔔 Alerting & Automation

The system provides comprehensive alerting and automation through Azure Monitor and Logic Apps:

### Azure Monitor Integration
- Real-time metrics collection
- Custom alert rules
- Log Analytics integration
- Performance monitoring

### Logic Apps Workflow
1. **Alert Trigger**: Azure Monitor alerts trigger the workflow
2. **Notification Channels**:
   - Microsoft Teams channel
   - Email notifications
   - Custom escalation paths
3. **Alert Content**:
   - Severity level
   - Detailed description
   - Timestamp
   - Metric values

### Setup Instructions
1. Deploy the Logic App:
   ```bash
   az deployment group create \
     --resource-group your-resource-group \
     --template-file deploy/logic_app.json
   ```

2. Configure connections:
   - Teams connection
   - Outlook connection
   - Azure Monitor connection

3. Set parameters:
   ```json
   {
     "teamId": "your-team-id",
     "channelId": "your-channel-id",
     "emailRecipients": "team@example.com,oncall@example.com"
   }
   ```

## 📊 Monitoring & Metrics

The system collects and analyzes various metrics:

| Metric | Description | Alert Threshold |
|--------|-------------|-----------------|
| LogAnomalyScore | Anomaly detection score | > 3.0 |
| ProcessingLatency | Event processing time | > 1000ms |
| ErrorRate | Error percentage | > 1% |

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

- 📧 Email: support@example.com
- 💬 Teams Channel: #log-anomaly-support
- 📚 [Documentation](https://docs.example.com/log-anomaly)

---

<div align="center">
  Made with ❤️ by Your Team
</div>