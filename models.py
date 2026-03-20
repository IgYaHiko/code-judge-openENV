from pydantic import BaseModel
from typing import List

class Action(BaseModel):
    code: str

class Observation(BaseModel):
    problem: str
    feedback: str

class StepResult(BaseModel):
    observation: Observation
    reward: float
    done: bool

class State(BaseModel):
    step_count: int
    episode_id: str