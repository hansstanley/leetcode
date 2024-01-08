import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    """
    Returns the second highest salary in the dataframe.
    """
    unique_salaries = employee["salary"].drop_duplicates()
    second_highest = (
        unique_salaries.nlargest(n=2).iloc[-1] if unique_salaries.size > 1 else None
    )
    return pd.DataFrame({"SecondHighestSalary": [second_highest]})
