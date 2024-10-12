from typing import List
from collections import Counter


def calculate_favourite_food(data: List):
    data = data.copy()

    for i in range(len(data)):
        all_types = data[i][4].split(",")
        count = Counter(all_types)
        data[i] = data[i][:4] + count.most_common(1)[0][:1] + data[i][5:]

    return data
