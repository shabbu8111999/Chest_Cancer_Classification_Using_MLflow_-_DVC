# Chest_Cancer_Classification_Using_MLflow_-_DVC


## Workflows 

1. Update config.yaml
2. Update secrets.yaml [optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml


# DAGSHUB WEBSITE

[dagshub](https://dagshub.com/)


## Dagshub Setup

ML_FLOW_TRACKING_URI= https://dagshub.com/shabbu8111999/Chest_Cancer_Classification_Using_MLflow_-_DVC.mlflow

ML FLOW_TRACKING_USERNAME = shabbu8111999

ML FLOW_TRACKING_TOKENS = 929d2e7e19d6a84f2682135c783b813c29e24089

#            OR
### Use This Code

import dagshub
dagshub.init(repo_owner='shabbu8111999', repo_name='Chest_Cancer_Classification_Using_MLflow_-_DVC', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)


## NOTE:
1. In Command Prompt Terminal(cmd) use : set 
2. In Linux/Mac Command use : export
3. In Powershell Terminal use : $env:


```bash

set MLFLOW_TRACKING_URI=https://dagshub.com/shabbu8111999/Chest_Cancer_Classification_Using_MLflow_-_DVC.mlflow

set MLFLOW_TRACKING_USERNAME=shabbu8111999

set MLFLOW_TRACKING_PASSWORD=89fd3ee38ac225a7a6c8489337e31ea344128042

```