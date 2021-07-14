from fastapi import FastAPI

app = FastAPI()


tickers = {
    "NSE": ["Bajaj Finance", "HDFC Bank", "Reliance"],
    "NASDAQ": ["Google", "Tesla"],
}


@app.get("/tickers/{index}")
def get_tickers(index: str):
    if index in tickers.keys():
        return {"tickers": tickers[index]}

    else:
        return {"detail": "Index not found."}
