from typing import Dict, List, Tuple


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items: Dict[str, Dict[str, int]], budget: int) -> Tuple[List[str], int, int]:
    ranked = sorted(
        items.items(),
        key=lambda kv: kv[1]["calories"] / kv[1]["cost"],
        reverse=True,
    )

    chosen = []
    total_cost = 0
    total_cal = 0

    for name, meta in ranked:
        if total_cost + meta["cost"] <= budget:
            chosen.append(name)
            total_cost += meta["cost"]
            total_cal += meta["calories"]

    return chosen, total_cost, total_cal


def dynamic_programming(items: Dict[str, Dict[str, int]], budget: int) -> Tuple[List[str], int, int]:
    names = list(items.keys())
    n = len(names)

    # dp[i][b] = max calories using first i items with budget b
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    take = [[False] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = names[i - 1]
        cost = items[name]["cost"]
        cal = items[name]["calories"]
        for b in range(budget + 1):
            dp[i][b] = dp[i - 1][b]
            if cost <= b:
                cand = dp[i - 1][b - cost] + cal
                if cand > dp[i][b]:
                    dp[i][b] = cand
                    take[i][b] = True

    # restore chosen set
    chosen = []
    b = budget
    for i in range(n, 0, -1):
        if take[i][b]:
            name = names[i - 1]
            chosen.append(name)
            b -= items[name]["cost"]

    chosen.reverse()
    total_cost = sum(items[name]["cost"] for name in chosen)
    total_cal = sum(items[name]["calories"] for name in chosen)
    return chosen, total_cost, total_cal


if __name__ == "__main__":
    budget = 100

    g = greedy_algorithm(items, budget)
    print("Greedy:", g)

    d = dynamic_programming(items, budget)
    print("DP:", d)