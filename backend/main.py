from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Hello World"
        "version": "0.0.1"
        "docs": "/docs"}


@app.get("/health")
def health():
    return {"status": "ok"}
@app.head("/health")
def head_health():
    return Response(status_code=200)