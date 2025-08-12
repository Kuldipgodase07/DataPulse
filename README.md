<<<<<<< HEAD
# Model Context Protocol (MCP) Server on GCP

A FastAPI-based MCP server that enables AI agents to perform real-time data analytics on Google Cloud Platform, integrating with Vertex AI and BigQuery.

## Features

- Query cloud-stored datasets in real-time via BigQuery
- Invoke ML models deployed on Vertex AI
- RESTful API endpoints for easy integration with AI agents

## Project Structure

- `main.py` – Main FastAPI server code
- `requirements.txt` – Python dependencies

## Setup

1. **Create and Activate a Virtual Environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure GCP Credentials:**

    - Set your `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to your service account JSON file:

        ```bash
        export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account.json"
        export GCP_PROJECT="your-gcp-project"
        export GCP_LOCATION="us-central1"
        export BQ_DATASET="your_bigquery_dataset"
        ```

4. **Run the Server:**

    ```bash
    uvicorn main:app --reload
    ```

## Usage

### Query BigQuery

**POST** `/query`

**Body:**
```json
{
  "sql": "SELECT * FROM your_dataset.your_table LIMIT 10"
}
=======
# Model-Context-Protocol-MCP-Server-on-GCP
Cloud MCP Server for Real-Time AI Analytics
>>>>>>> 212dba0342d2b8a157370d43484da30645513a56
