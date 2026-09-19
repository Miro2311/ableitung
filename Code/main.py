# Code/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from Code.ableitung import ableiten


# Eingabe-Schema: erwartet JSON mit diesen Feldern
class AbleitungRequest(BaseModel):
    funktion: str
    variable: str = "x"
    ordnung: int = 1


# Ausgabe-Schema der API
class AbleitungResponse(BaseModel):
    funktion: str
    variable: str
    ordnung: int
    ableitung: str


app = FastAPI(title="AbleitungsrechnerAPI")


@app.post("/ableitung", response_model=AbleitungResponse)
def ableitung_berechnen(req: AbleitungRequest):
    try:
        ergebnis = ableiten(req.funktion, req.variable, req.ordnung)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return AbleitungResponse(
        funktion=req.funktion,
        variable=req.variable,
        ordnung=req.ordnung,
        ableitung=ergebnis,
    )