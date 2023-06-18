from pynamodb.attributes import UnicodeAttribute, ListAttribute
from pynamodb.models import Model
from settings import config


class BaseTable(Model):
    class Meta:
        region = config.AWS_REGION


class Activities(BaseTable):
    class Meta(BaseTable.Meta):
        table_name = "leaderboard_activities"

    id = UnicodeAttribute(hash_key=True)
    athlete_id = UnicodeAttribute(null=False)
    athlete_name = UnicodeAttribute(null=False)
    athlete_url = UnicodeAttribute(null=False)
    type = UnicodeAttribute(null=False)
    url = UnicodeAttribute(null=False)
    title = UnicodeAttribute(null=False)
    timestamp = UnicodeAttribute(null=False)


class Leaderboard(BaseTable):
    class Meta(BaseTable.Meta):
        table_name = "leaderboard_summary"

    id = UnicodeAttribute(hash_key=True)
    timestamp = UnicodeAttribute(range_key=True)
    activity_ids = ListAttribute()
    activity_type = UnicodeAttribute()
    athlete_id = UnicodeAttribute()
    athlete_name = UnicodeAttribute()
    distance = UnicodeAttribute()
    distance_gain = UnicodeAttribute()
