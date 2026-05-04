from api.client import ApiClient
from data.repository import Repository
from services.analyzer import Analyzer
from services.normalizer import Normalizer

def main():

    API_KEY = "qyHOVo0aXypSm9tOoeMunO4bGgjs1NRzN2M1CEj6"

    client = ApiClient()
    repo = Repository()
    analyzer = Analyzer()
    normalizer = Normalizer()

    print("Fetching data...")

 #loads data
    for page in range(2):
        raw = client.fetch_page(API_KEY, page)
        results = raw.get("results", [])

        print(f"Page {page} records:", len(results))

        for item in results:
            clean = normalizer.clean(item)
            repo.add(clean)

    data = repo.data
    print("\nTotal usable records:", len(data))


#analyzes data
    corr = analyzer.correlation(data)
    groups = analyzer.group_by_state(data)
    top = analyzer.top_tuition(data)

    # state averages (small aggregation table)
    state_avg = {}
    for state, schools in groups.items():
        valid = [s.tuition for s in schools if s.tuition is not None]
        if len(valid) > 0:
            state_avg[state] = sum(valid) / len(valid)


# outputs
    print("Research Report")


    print("\nThesis")
    print("Higher tuition is associated with higher graduation rates across U.S. colleges, varying by state.")

    print("\nDataset Used")
    print("U.S. Department of Education College Scorecard API")
    print("Endpoint: https://api.data.gov/ed/collegescorecard/v1/schools")

    print("\nMethods")
    print("- Pearson correlation (tuition vs graduation rate)")
    print("- Grouping by state (dictionary / HashMap)")
    print("- Top-K ranking using heap (top 5 tuition schools)")
    print("- Filtering missing values (data cleaning)")

    print("\nResults")

    print("\nCorrelation (tuition vs graduation):", round(corr, 4))

    print("\nTop 5 highest tuition schools:")
    for r in top:
        print(f"- {r.name}: {r.tuition}")

    print("\nState averages (sample):")
    for i, (state, avg) in enumerate(state_avg.items()):
        if i == 8:
            break
        print(f"- {state}: {round(avg, 2)}")

    print("\nConclusion")

    if corr > 0.2:
        print("Supported: moderate positive relationship found.")
    elif corr < -0.2:
        print("Supported: negative relationship found.")
    else:
        print("Inconclusive: weak or no clear linear relationship.")


if __name__ == "__main__":
    main()