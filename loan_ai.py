import json

def load_rules():
    with open("rules.json", "r") as file:
        return json.load(file)

def check_eligibility(applicant, rules):
    if not (rules["age_min"] <= applicant["age"] <= rules["age_max"]):
        return "Not Eligible (Age Criteria Failed)"

    if applicant["income"] < rules["min_income"]:
        return "Not Eligible (Income Criteria Failed)"

    if applicant["credit_score"] < rules["min_credit_score"]:
        return "Not Eligible (Credit Score Criteria Failed)"

    if rules["employment_required"] and applicant["employment_status"] != "employed":
        return "Not Eligible (Employment Status Failed)"

    return "Eligible for Loan"

if __name__ == "__main__":
    rules = load_rules()

    applicant = {
        "age": 28,
        "income": 50000,
        "credit_score": 720,
        "employment_status": "employed"
    }

    result = check_eligibility(applicant, rules)
    print("Loan Decision:", result)
