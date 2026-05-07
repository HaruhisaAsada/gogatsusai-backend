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

## Docker run

```bash
docker build -t gogatsusai-backend .
docker run --rm -p 8000:8000 -e DATABASE_URL=sqlite:///./gogatsusai.db gogatsusai-backend
```
