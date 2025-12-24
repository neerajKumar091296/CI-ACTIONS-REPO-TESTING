
import  json
from operator import truediv
import  os
from Client.http_client import *
from validators.response_validator import validate_response
from tests.test_current_user import test_get_current_user


def load_environment_configuration():
    env = os.getenv("ENV","dev")

    with open("configuration/env.json") as file:
        config = json.load(file)

    if env not in config:
        raise ValueError(f"Unknown environment: {env}")

    return config[env]["base_url"]

def load_tests():
    with open("tests/test_case.json") as file:
        return json.load(file)

def run_tests():
    tests = load_tests()
    base_url = load_environment_configuration()
    passed = 0
    failed = 0

    results = []

    for test in tests:
        print(f"\nRunning test: {test['name']}")

        test_result = {
            "name": test["name"],
            "status": "",
            "errors": []
        }
        try:
            response = send_request(
                test["method"],
                test["endpoint"],
                base_url
            )

            errors = validate_response(response,test["expected_status"],
                                   test["expected_fields"])

            if errors:
                test_result["status"] = "Failed"
                test_result["errors"] = errors

                failed += 1
                print("Failed")
                for error in errors:
                    print(f" -{error}")

            else:
                test_result["status"] = "Passed"
                passed += 1
                print("Passed")

        except Exception as exc:
            test_result["status"] = "error"
            test_result["errors"].append(str(exc))
            failed += 1
            print("Error")
            print(f"{exc}")

        results.append(test_result)

    write_report(results,passed,failed)



    print("\n====== Test summary=====")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")



def write_report(result,passed,failed):
    report = {
        "summary": {
            "passed": passed,
            "failed": failed,
            "total": passed + failed
        },
        "results": result
    }

    with open("report/results.json","w") as file:
        json.dump(report,file,indent=2)

    print("\n====== Final Summary ======")
    print(f"Total: {passed + failed}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print("Report written to report/results.json")

def get_current_user(base_url:str,access_token:str):
    url = f"{base_url}/auth/me"

    headers = {
            "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url=url,headers=headers,timeout=10)

    
    if response.status_code != 200:
        raise RuntimeError (
            f"Auth Request failed ({response.status_code}: {response.text})"
        )

    try:
        return response.json()
    except ValueError:
        raise RuntimeError("Respone is not valid json")


if __name__=="__main__":
    test_get_current_user()
    
