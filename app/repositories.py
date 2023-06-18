from uuid import UUID
from typing import List, Union
from datetime import datetime, date

from tables import Activities, Leaderboard
from schemas import ActivitySchema, LeaderboardSchema


class ActivityRepository:
    table: Activities = Activities
    schema_out: ActivitySchema = ActivitySchema

    @classmethod
    def get(cls, entry_id: Union[str, UUID]) -> ActivitySchema:
        model = cls.table.get(str(entry_id))
        return cls.schema_out(**model.attribute_values)

    @classmethod
    def list(cls) -> List[ActivitySchema]:
        return [cls.schema_out(**model.attribute_values) for model in cls.table.scan()]


class LeaderboardsRepository:
    table: Leaderboard = Leaderboard
    schema_out: LeaderboardSchema = LeaderboardSchema

    @classmethod
    def list(cls) -> List[LeaderboardSchema]:
        return [cls.schema_out(**model.attribute_values) for model in cls.table.scan()]


class LeaderboardRepository:
    table: Leaderboard = Leaderboard
    schema_out: LeaderboardSchema = LeaderboardSchema

    @classmethod
    def list(cls, period) -> List[LeaderboardSchema]:
        epoch = str(
            int(
                datetime.strptime(period if period else str(date.today()), "%Y-%m-%d")
                .replace(hour=23, minute=59, second=59)
                .timestamp()
            )
        )

        return [
            cls.schema_out(**model.attribute_values)
            for model in cls.table.scan(filter_condition=Leaderboard.timestamp == epoch)
        ]
