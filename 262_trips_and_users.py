import pandas as pd


def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    unbanned = users[users["banned"] == "No"]
    trips_in = trips[trips["request_at"].between("2013-10-01", "2013-10-03")]
    trips_in = trips_in[
        trips_in["client_id"].isin(unbanned["users_id"])
        & trips_in["driver_id"].isin(unbanned["users_id"])
    ]
    trips_in["cancelled"] = trips_in["status"].str.startswith("cancelled")
    trips_summary = (
        trips_in.groupby("request_at")["cancelled"]
        .aggregate(["sum", "size"])
        .reset_index()
    )
    trips_summary["Cancellation Rate"] = (
        trips_summary["sum"] / trips_summary["size"]
    ).round(2)
    trips_summary = trips_summary.rename(columns={"request_at": "Day"})
    return trips_summary[["Day", "Cancellation Rate"]]


data = [
    ["1", "1", "10", "1", "completed", "2013-10-01"],
    ["2", "2", "11", "1", "cancelled_by_driver", "2013-10-01"],
    ["3", "3", "12", "6", "completed", "2013-10-01"],
    ["4", "4", "13", "6", "cancelled_by_client", "2013-10-01"],
    ["5", "1", "10", "1", "completed", "2013-10-02"],
    ["6", "2", "11", "6", "completed", "2013-10-02"],
    ["7", "3", "12", "6", "completed", "2013-10-02"],
    ["8", "2", "12", "12", "completed", "2013-10-03"],
    ["9", "3", "10", "12", "completed", "2013-10-03"],
    ["10", "4", "13", "12", "cancelled_by_driver", "2013-10-03"],
]
trips = pd.DataFrame(
    data,
    columns=[
        "id",
        "client_id",
        "driver_id",
        "city_id",
        "status",
        "request_at",
    ],
).astype(
    {
        "id": "Int64",
        "client_id": "Int64",
        "driver_id": "Int64",
        "city_id": "Int64",
        "status": "object",
        "request_at": "object",
    }
)

data = [
    ["1", "No", "client"],
    ["2", "Yes", "client"],
    ["3", "No", "client"],
    ["4", "No", "client"],
    ["10", "No", "driver"],
    ["11", "No", "driver"],
    ["12", "No", "driver"],
    ["13", "No", "driver"],
]
users = pd.DataFrame(data, columns=["users_id", "banned", "role"]).astype(
    {"users_id": "Int64", "banned": "object", "role": "object"}
)

print(trips_and_users(trips, users))
