from fastapi import FastAPI

app = FastAPI()
import sys

sys.path.append("../")
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from src.simulators import PnCSimulator
from src.simulators import MenuSimulator

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/simulate")
async def root():
    pnc = PnCSimulator()
    lognorm_params, stat, trajs = pnc.simulate(
        n_param=1,
        sim_per_param=1,
    )
    # print("stat", stat)
    # print("traj", trajs)

    df = pd.DataFrame(
        trajs[0], columns=["timeDiff", "pointer_x", "pointer_y", "ball_x", "ball_y"]
    )
    json = df.to_json()
    return {"message": json}
