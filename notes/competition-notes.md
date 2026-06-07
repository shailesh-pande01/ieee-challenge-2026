# IEEE Global Student Challenge 2025 - Learning Notes

## Purpose

This document tracks my understanding, learning progress, questions, and research notes for the IEEE Global Student Challenge.

---

# Challenge 1: Backdoor Attacks in Distributed Machine Learning and their Remediation

## What is this challenge about?

This challenge focuses on securing distributed machine learning systems where multiple participants collaboratively train a model. Attackers may intentionally inject malicious updates to create hidden behaviors (backdoors) inside the model.

---

## My Understanding (In My Own Words)

Normally, machine learning models learn from data and improve over time. In distributed or federated learning, many devices train a model together without sharing raw data.

A malicious participant can send poisoned updates during training. The model may appear normal but secretly behave incorrectly when a specific trigger is present.

The goal is to detect and prevent such attacks.

---

## Key Concepts

* Machine Learning
* Neural Networks
* Distributed Learning
* Federated Learning
* Model Poisoning
* Data Poisoning
* Backdoor Attacks
* Adversarial Machine Learning
* Robust Aggregation

---

## Questions and Short Answers

### How does federated learning work?

Devices train locally and send model updates to a central server, which combines them into a global model.

### Why is distributed ML vulnerable?

The server often trusts updates from participants, making it possible for attackers to submit malicious updates.

### How are backdoors inserted?

Attackers poison training data or modify model updates before sending them.

### How are malicious updates detected?

Using anomaly detection, statistical analysis, and secure aggregation techniques.

### What defenses exist?

* Krum
* Trimmed Mean
* Median Aggregation
* Secure Aggregation
* Byzantine-Robust Learning

### What are current limitations?

Sophisticated attacks can still bypass many defenses while remaining difficult to detect.

---

## What I Already Know

* Programming fundamentals
* Git and GitHub
* Basic software development

## Completely New Topics

* Federated Learning
* Adversarial Machine Learning
* Model Poisoning
* Backdoor Detection

---

# Challenge 2: Automatic Discovery of Vulnerabilities in GitHub CI/CD Workflows and their Patches

## What is this challenge about?

This challenge focuses on finding security issues in GitHub Actions workflows and automatically suggesting secure fixes.

---

## My Understanding (In My Own Words)

Modern projects use CI/CD pipelines to automatically test, build, and deploy applications.

Workflow files can contain security mistakes that expose secrets, allow unauthorized access, or create supply-chain risks.

The goal is to automatically detect these issues and recommend patches.

---

## Key Concepts

* GitHub Actions
* CI/CD
* DevSecOps
* Workflow Security
* Supply Chain Security
* Static Analysis
* Secrets Management
* Least Privilege

---

## Questions and Short Answers

### What security mistakes are common?

* Hardcoded secrets
* Excessive permissions
* Using untrusted actions
* Unsafe shell commands

### How can YAML be analyzed?

By parsing workflow files and checking them against security rules.

### How are workflow permissions checked?

By examining the permissions block and comparing it with required permissions.

### Can AI suggest patches?

Yes. AI can identify patterns and generate safer workflow configurations.

### How do scanners work?

They analyze workflow files and flag known risky configurations without executing them.

---

## What I Already Know

* Git
* GitHub
* Basic GitHub Actions usage
* Frontend development

## Completely New Topics

* CI/CD Security
* DevSecOps
* Static Analysis
* Supply Chain Attacks

---

# Challenge 3: Analyzing Resource Usage in Data Center Computers and Predicting Events

## What is this challenge about?

This challenge focuses on analyzing server resource usage and predicting failures or performance slowdowns before they happen.

---

## My Understanding (In My Own Words)

Data centers contain thousands of servers generating metrics such as CPU, memory, disk, and network usage.

By analyzing these metrics over time, it may be possible to predict failures or performance degradation before users are affected.

---

## Key Concepts

* Data Centers
* Monitoring
* Observability
* Time-Series Data
* Anomaly Detection
* Predictive Maintenance
* Machine Learning
* Resource Utilization

---

## Questions and Short Answers

### What metrics predict failures?

* CPU Usage
* Memory Usage
* Disk Utilization
* Temperature
* Network Activity
* Error Logs

### How are logs analyzed?

Patterns, anomalies, and historical events are examined to identify warning signs.

### Which ML models work best?

Common approaches include:

* Random Forest
* XGBoost
* LSTM
* Anomaly Detection Models

### How much historical data is needed?

Generally weeks or months of data improve prediction accuracy.

### How are false alarms reduced?

By combining multiple signals and improving model quality using historical validation.

---

## What I Already Know

* Basic computer systems
* Programming
* Web technologies

## Completely New Topics

* Data Center Operations
* Observability
* Time-Series Analysis
* Failure Prediction Models

---

# Current Ranking (Based on My Background)

### 1. GitHub CI/CD Security

Most aligned with my current knowledge and experience.

### 2. Data Center Resource Analysis

Moderate learning curve with some machine learning requirements.

### 3. Backdoor Attacks in Distributed ML

Most research-intensive and requires significant ML knowledge.

---
