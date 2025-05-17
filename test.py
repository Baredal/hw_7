import requests
import time

URL = "http://localhost:8000/process"

test_cases = [
    "HeLlO WORld",
    "this is a fraud case",
    "my password is 1234",
    ""
]

def run_test():
    for idx, data in enumerate(test_cases, 1):
        print(f"\n▶ Testing case #{idx}: {data!r}")
        start = time.time()
        response = requests.post(URL, data=data.encode('utf-8'), headers={"Content-Type": "text/plain"})
        duration = time.time() - start

        try:
            result = response.json()
        except Exception:
            result = f"Non-JSON response: {response.text}"

        print(f"Status Code: {response.status_code}")
        print(f"Response: {result}")
        print(f"Request Duration: {duration:.2f}s")

if __name__ == "__main__":
    run_test()
