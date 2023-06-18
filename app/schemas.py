from pydantic import BaseModel


class ActivitySchema(BaseModel):
    id: str
    athlete_id: str
    athlete_name: str
    athlete_url: str
    type: str
    url: str
    title: str
    timestamp: str


class LeaderboardSchema(BaseModel):
    id: str
    timestamp: str
    activity_ids: list
    activity_type: str
    athlete_id: str
    athlete_name: str
    distance: str
    distance_gain: str
