import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    """
    Returns the Nth highest salary in the dataframe.
    """
    unique_salaries = employee["salary"].drop_duplicates()
    sorted_salaries = unique_salaries.sort_values(ascending=False)
    nth_highest = sorted_salaries.iloc[N - 1] if 0 < N <= sorted_salaries.size else None
    return pd.DataFrame({f"getNthHighestSalary({N})": [nth_highest]})


employees = pd.DataFrame(
    {
        "id": [1, 2, 3],
        "salary": [1000, 2000, 3000],
    }
)

print(nth_highest_salary(employees, -1))
