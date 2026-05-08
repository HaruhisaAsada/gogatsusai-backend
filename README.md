# gogatsusai-backend

FastAPI backend for Gogatsusai booth manager.

## Local run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

- API docs: `http://127.0.0.1:8000/docs`
- Health: `GET /health`

## Environment variables

Copy and edit:

```bash
cp .env.example .env
```

- `DATABASE_URL` default: `sqlite:///./gogatsusai.db`
- `GOOGLE_SHEETS_ID`: target spreadsheet ID
- `GOOGLE_SHEET_NAME`: target sheet name (default: `sales_1`)

## Docker run

```bash
docker build -t gogatsusai-backend .
docker run --rm -p 8080:8080 -e PORT=8080 -e DATABASE_URL=sqlite:///./gogatsusai.db gogatsusai-backend
```

For local Sheets append, set `GOOGLE_APPLICATION_CREDENTIALS` to the service account JSON path.
