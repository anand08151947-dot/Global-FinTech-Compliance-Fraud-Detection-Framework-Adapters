```mermaid
sequenceDiagram
    participant monitoring
    Note right of monitoring: start - Monitoring agent started
    participant etl
    monitoring->>etl: start - ETL agent started
    Note right of etl: end - ETL agent finished
    participant compliance
    etl->>compliance: start - Compliance agent started
    participant fraud
    compliance->>fraud: start - Fraud agent started
    participant mlops
    fraud->>mlops: start - Mlops agent started
    participant access
    mlops->>access: start - Access agent started
    participant reporting
    access->>reporting: start - Reporting agent started
    reporting->>compliance: end - Compliance agent finished
    compliance->>fraud: end - Fraud agent finished
    fraud->>mlops: end - MLOps agent finished
    mlops->>access: end - Access/Security agent finished
    access->>reporting: end - Reporting/Case agent finished
    reporting->>monitoring: end - Monitoring agent finished
```