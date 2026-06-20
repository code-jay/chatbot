import numpy as np


def cosine_similarity(
    a: list[float],
    b: list[float]
) -> float:
    a = np.array(a)
    b = np.array(b)

    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)

    if a_norm == 0 or b_norm == 0:
        return 0.0

    return float(np.dot(a, b) / (a_norm * b_norm))