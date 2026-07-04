from fastapi import FastAPI

app = FastAPI(title="MelanciaERP")

@app.get("/")
def home():
    return {"status": "MelanciaERP rodando 🚀"}
