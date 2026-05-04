import urllib.request
import json

class ApiClient:
    BASE_URL = "https://api.data.gov/ed/collegescorecard/v1/schools.json"

    def fetch_page(self, api_key, page):
        url = (
            self.BASE_URL +
            "?api_key=" + api_key +
            "&page=" + str(page) +
            "&per_page=100" +
            "&fields=school.name,school.state,latest.cost.tuition.in_state,latest.completion.rate"
        )

        req = urllib.request.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0")

        response = urllib.request.urlopen(req)
        return json.loads(response.read().decode())