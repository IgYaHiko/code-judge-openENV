from fastapi import FastAPI
from models import Action
from server.environment import CodingEnvironment

app = FastAPI()
env = CodingEnvironment()

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: Action):
    return env.step(action)

@app.get("/state")
def state():
    return env.state