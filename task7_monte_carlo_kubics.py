import random
from collections import Counter
import matplotlib.pyplot as plt


ANALYTIC_COUNTS = {s: c for s, c in zip(range(2, 13), [1,2,3,4,5,6,5,4,3,2,1])}
ANALYTIC_PROB = {s: c / 36 for s, c in ANALYTIC_COUNTS.items()}


def monte_carlo_dice(trials: int = 200_000) -> dict[int, float]:
    cnt = Counter()
    for _ in range(trials):
        s = random.randint(1, 6) + random.randint(1, 6)
        cnt[s] += 1
    return {s: cnt[s] / trials for s in range(2, 13)}


def plot_probs(mc: dict[int, float]):
    sums = list(range(2, 13))
    mc_vals = [mc[s] for s in sums]
    an_vals = [ANALYTIC_PROB[s] for s in sums]

    plt.figure(figsize=(9, 4))
    plt.plot(sums, mc_vals, marker="o", label="Monte-Carlo")
    plt.plot(sums, an_vals, marker="x", label="Analytic")
    plt.xticks(sums)
    plt.xlabel("Sum")
    plt.ylabel("Probability")
    plt.title("Two dice: Monte-Carlo vs Analytic")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    trials = 200_000
    mc = monte_carlo_dice(trials=trials)

    print(f"Trials: {trials}")
    print("sum | Monte-Carlo | Analytic | abs diff")
    for s in range(2, 13):
        diff = abs(mc[s] - ANALYTIC_PROB[s])
        print(f"{s:>3} | {mc[s]:>10.6f} | {ANALYTIC_PROB[s]:>7.6f} | {diff:.6f}")

    plot_probs(mc)