import os
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from google.cloud import bigquery, aiplatform
from typing import List

app = FastAPI(title="Model Context Protocol (MCP) Server")

# Set your GCP project and location
GCP_PROJECT = os.environ.get("GCP_PROJECT", "your-gcp-project")
GCP_LOCATION = os.environ.get("GCP_LOCATION", "us-central1")
BQ_DATASET = os.environ.get("BQ_DATASET", "your_bigquery_dataset")

# Initialize the BigQuery client
bq_client = bigquery.Client(project=GCP_PROJECT)

# Initialize Vertex AI
aiplatform.init(project=GCP_PROJECT, location=GCP_LOCATION)

class QueryRequest(BaseModel):
    sql: str

class PredictRequest(BaseModel):
    endpoint_id: str
    instances: List[dict]

@app.post("/query")
def query_bigquery(req: QueryRequest):
    try:
        query_job = bq_client.query(req.sql)
        results = [dict(row) for row in query_job.result()]
        return {"result": results}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/predict")
def predict_vertex(req: PredictRequest):
    try:
        endpoint = aiplatform.Endpoint(req.endpoint_id)
        prediction = endpoint.predict(instances=req.instances)
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/")
def read_root():
    return {"message": "Welcome to the Model Context Protocol (MCP) Server!"}