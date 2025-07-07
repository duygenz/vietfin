from fastapi import FastAPI
from vietfin import vf

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Vietfin API đang hoạt động"}

@app.get("/stocks")
def get_stocks():
    try:
        data = vf.equity.search()
        return {"data": data}
    except Exception as e:
        return {"error": str(e)}