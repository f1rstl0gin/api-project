import heapq
from collections import defaultdict

class Analyzer:

    def correlation(self, data):
        x, y = [], []

        for r in data:
            if r.tuition is not None and r.grad_rate is not None:
                x.append(r.tuition)
                y.append(r.grad_rate)

        n = len(x)
        if n == 0:
            return 0

        mx = sum(x) / n
        my = sum(y) / n

        num = sum((a - mx) * (b - my) for a, b in zip(x, y))
        den = (sum((a - mx) ** 2 for a in x) * sum((b - my) ** 2 for b in y)) ** 0.5

        return num / den if den != 0 else 0

    def group_by_state(self, data):
        groups = defaultdict(list)
        for r in data:
            groups[r.state].append(r)
        return groups

    def top_tuition(self, data):
        return heapq.nlargest(5, data, key=lambda r: r.tuition or 0)