# https://github.com/rglsk/dynamodb-fastapi
# https://rogulski.it/dynamodb-with-fastapi/


import uvicorn

from fastapi import FastAPI
from typing import Union

# from starlette import status
from repositories import (
    ActivityRepository,
    ActivitySchema,
    LeaderboardsRepository,
    LeaderboardSchema,
    LeaderboardRepository,
)

from typing import List

app = FastAPI()


@app.get("/")
def test_endpoint():
    return "Hello form FastAPI"


@app.get("/activity/{activity_id}", response_model=ActivitySchema)
def get_activity(activity_id: str):
    activity = ActivityRepository.get(activity_id)
    return activity


@app.get("/activities/", response_model=List[ActivitySchema])
def get_activities():
    activities = ActivityRepository.list()
    return activities


@app.get("/leaderboard/", response_model=List[LeaderboardSchema])
def get_leaderboard(date: Union[str, None] = None):
    leaderboard = LeaderboardRepository.list(date)
    return leaderboard


@app.get("/leaderboards/", response_model=List[LeaderboardSchema])
def get_leaderboard():
    leaderboard = LeaderboardsRepository.list()
    return leaderboard


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
