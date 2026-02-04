from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return {"msg": "Hello"}


@app.get("/health")
def get_health():
    return {"status": "ok"}
