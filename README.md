# Model Context Protocol (MCP) Server on GCP

A FastAPI-based MCP server that enables AI agents to perform real-time data analytics on Google Cloud Platform, integrating with Vertex AI and BigQuery.


## Architecture Diagram
![Project Architecture](https://github.com/Kuldipgodase07/DataPulse/blob/main/GCP%20Diagram)


## Key Features

- **Unified Query & Inference API:** One server, two superpowers — run SQL analytics on BigQuery or get instant predictions from Vertex AI models.
- **Blazing Fast:** Asynchronous FastAPI backend for high-performance, low-latency requests.
- **Cloud-Native Integration:** Native support for Google Cloud authentication and resource management.
- **Developer Friendly:** Clean, well-documented REST endpoints, ready for integration with any modern tech stack.
- **Secure by Design:** Leverages GCP IAM for secure data access and model invocation.

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
```
