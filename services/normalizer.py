from domain.school_record import SchoolRecord

class Normalizer:

    def clean(self, item):

        def safe_float(x):
            try:
                return float(x) if x is not None else None
            except:
                return None

        tuition = item.get("latest.cost.tuition.in_state")
        grad = item.get("latest.completion.rate")

        if tuition is None and grad is None:
            return None

        return SchoolRecord(
            name=item.get("school.name", "Unknown"),
            state=item.get("school.state", "Unknown"),
            tuition=safe_float(tuition),
            grad_rate=safe_float(grad)
        )