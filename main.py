from fastapi import FastAPI
from vietfin import vf

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Vietfin API đang hoạt động"}

@app.get("/stocks")
def get_stocks():
    return {"data": vf.equity.search()}

@app.get("/stock/{symbol}")
def get_stock_profile(symbol: str):
    return {"data": vf.equity.profile(symbol=symbol)}

@app.get("/stock/{symbol}/price")
def get_stock_price(symbol: str):
    return {"data": vf.equity.historical(symbol=symbol)}

@app.get("/stock/{symbol}/dividends")
def get_dividends(symbol: str):
    return {"data": vf.equity.fundamental.dividends(symbol=symbol)}

@app.get("/stock/{symbol}/management")
def get_management(symbol: str):
    return {"data": vf.equity.fundamental.management(symbol=symbol)}

@app.get("/stock/{symbol}/ratios")
def get_ratios(symbol: str):
    return {"data": vf.equity.fundamental.ratios(symbol=symbol)}

@app.get("/stock/{symbol}/income")
def get_income(symbol: str):
    return {"data": vf.equity.fundamental.income(symbol=symbol)}

@app.get("/stock/{symbol}/events")
def get_events(symbol: str):
    return {"data": vf.equity.calendar.events(symbol=symbol)}

@app.get("/funds")
def get_funds():
    return {"data": vf.funds.search()}

@app.get("/etfs")
def get_etfs():
    return {"data": vf.etf.search()}

@app.get("/index/{symbol}")
def get_index_constituents(symbol: str):
    return {"data": vf.index.constituents(symbol=symbol)}

@app.get("/derivatives/futures")
def get_futures():
    return {"data": vf.derivatives.futures.search()}