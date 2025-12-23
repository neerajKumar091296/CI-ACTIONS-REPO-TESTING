import  json


def validate_response(response,expected_status,expected_fields):
    errors = []

    if response.status_code != expected_status:
        errors.append(f"Expected status {expected_status} got {response.status_code}")


    try:
        body = response.json()
    except ValueError:
        errors.append("Response is not valid JSON")
        return errors

    for field in expected_fields:
        if field not in body:
            errors.append(f"Missing expected filed: {field}")

    return errors
