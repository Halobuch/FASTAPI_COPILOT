# FASTAPI_COPILOT

A minimal FastAPI app with a prompt form at `/`. Submitting the form sends a
JSON request to `POST /generate` and displays the response. The app also
provides `POST /payload` to return an arbitrary JSON object in a `received`
field.

Install dependencies and start the development server:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Send a request:

```bash
curl -X POST http://127.0.0.1:8000/generate \
	-H 'Content-Type: application/json' \
	-d '{"prompt":"Write a greeting"}'
```

Or open `http://127.0.0.1:8000` and submit the form.

The generate route currently acknowledges the prompt; connect a generation
service in `main.py` to return generated content.

Calculate a SHA-256 checksum for text:

```bash
curl -X POST http://127.0.0.1:8000/checksum \
	-H 'Content-Type: application/json' \
	-d '{"text":"hello"}'
```

```bash
curl -X POST http://127.0.0.1:8000/payload \
	-H 'Content-Type: application/json' \
	-d '{"name":"example","active":true}'
```
