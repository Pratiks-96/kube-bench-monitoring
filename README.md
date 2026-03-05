# kube-bench-monitoring
kube-bench CronJob
        │
        ▼
Kubernetes Job
        │
        ▼
Scan Output
        │
        ▼
Exporter Metrics
        │
        ▼
Prometheus Scrapes Metrics
        │
        ▼
Alert Rule Triggered
        │
        ▼
Alertmanager Sends Alert


using this we can get if cronjob of the kube-bench fail then this will get refect and show any misconfiguration about this 
<img width="817" height="289" alt="image" src="https://github.com/user-attachments/assets/2d12dbea-5252-4219-a7a4-5aaab898073f" />

<img width="1357" height="681" alt="image" src="https://github.com/user-attachments/assets/583e9ae9-4767-48ee-8943-65c6bac379d7" />
