from typing import Tuple, Union
from entities import Request


def check_is_binary(value: int, name: str):
    if value not in [0, 1]:
        raise ValueError(f"Parameter '{name}' is not binary.")


def check_within_range(
    value: Union[int, float],
    lower_bound: Union[int, float],
    upper_bound: Union[int, float],
    name: str,
):
    if not (lower_bound <= value <= upper_bound):
        raise ValueError(f"Parameter '{name}' is out of [{lower_bound}, {upper_bound}] range.")


def check_data_validity(data: Request) -> Tuple[bool, str]:
    try:
        check_within_range(data.age, 0, 120, "age")
        check_is_binary(data.sex, "sex")
        check_within_range(data.cp, 0, 3, "cp")
        check_within_range(data.trestbps, 50, 300, "trestbps")
        check_within_range(data.chol, 50, 500, "chol")
        check_is_binary(data.fbs, "fbs")
        check_within_range(data.restecg, 0, 2, "restecg")
        check_within_range(data.thalach, 0, 200, "thalach")
        check_is_binary(data.exang, "exang")
        check_within_range(data.oldpeak, 0, 10, "oldpeak")
        check_within_range(data.slope, 0, 2, "slope")
        check_within_range(data.ca, 0, 4, "ca")
        check_within_range(data.thal, 0, 3, "thal")
        return True, "OK"
    except ValueError as error:
        return False, str(error)
