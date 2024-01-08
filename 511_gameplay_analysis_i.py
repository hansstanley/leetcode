import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    logins = (
        activity.groupby("player_id")["event_date"]
        .aggregate(["min"])
        .reset_index()
        .rename(columns={"min": "first_login"})
    )
    return logins


data = [
    [1, 2, "2016-03-01", 5],
    [1, 2, "2016-05-02", 6],
    [2, 3, "2017-06-25", 1],
    [3, 1, "2016-03-02", 0],
    [3, 4, "2018-07-03", 5],
]
activity = pd.DataFrame(
    data, columns=["player_id", "device_id", "event_date", "games_played"]
).astype(
    {
        "player_id": "Int64",
        "device_id": "Int64",
        "event_date": "datetime64[ns]",
        "games_played": "Int64",
    }
)

print(game_analysis(activity))
