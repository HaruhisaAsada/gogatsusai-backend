# gogatsusai backend

## Run local

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

- API docs: `http://127.0.0.1:8000/docs`
- Health: `GET /health`
