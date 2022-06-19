from enum import Enum


class Monotonicity(Enum):
    INCREASING = 1
    DECREASING = 2
    NONE = 3


def increasing_or_decreasing(ns):
    if all(ns[i] < ns[i + 1] for i in range(len(ns) - 1)) and len(ns) > 1:
        return Monotonicity.INCREASING
    elif all(ns[i] > ns[i + 1] for i in range(len(ns) - 1)) and len(ns) > 1:
        return Monotonicity.DECREASING
    else:
        return Monotonicity.NONE


increasing_or_decreasing([[1, 2, 3, 4, 5]])
