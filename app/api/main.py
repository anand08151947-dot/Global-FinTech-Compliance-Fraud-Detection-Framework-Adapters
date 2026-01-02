from fastapi import FastAPI
from app.adapters.postgres_adapter import PostgresAdapter
from app.adapters.dynamodb_adapter import DynamoDBAdapter
from app.adapters.snowflake_adapter import SnowflakeAdapter

from app.validators.unified_schema_validator import UnifiedSchemaValidator
from app.adapters.orchestrator_adapter import OrchestratorAdapter

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/run-validation")
def run_validation():
    # Example: fetch data from adapters and validate
    pg = PostgresAdapter()
    dy = DynamoDBAdapter()
    validator = UnifiedSchemaValidator()
    pg_data = pg.fetch()
    dy_data = dy.fetch()
    result = validator.validate(pg_data, dy_data)
    return {"validation_result": result}


# New endpoint to run the orchestrator pipeline
@app.post("/run-orchestrator-pipeline")
def run_orchestrator_pipeline():
    orchestrator = OrchestratorAdapter()
    results = orchestrator.run_pipeline()
    return {"pipeline_results": results}


# Example usage for local testing (not an endpoint)
if __name__ == "__main__":
    orchestrator = OrchestratorAdapter()
    results = orchestrator.run_pipeline()
    print("Orchestrator Pipeline Results:")
    print(results)
