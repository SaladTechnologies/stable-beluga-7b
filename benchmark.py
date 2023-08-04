import requests
import time
import os
import json

def fetch_data(domain_name, api_key, data):
    start_time = time.time()
    response = requests.post(domain_name, headers={
        "Content-Type": "application/json",
        "Salad-Api-Key": api_key
    }, data=data)
    end_time = time.time()
    return response, end_time - start_time

def main():
    domain_name = "https://domain-name.com"
    api_key = "your-api-key"
    data = {
        "data": "your-data"
    }

    total_ms = 0
    min_ms = float("inf")
    max_ms = 0
    iteration = 100

    # Create a folder to store the responses
    folder_name = "benchmark_results"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    for _ in range(iteration):
        response, time_taken = fetch_data(domain_name, api_key, data)
        total_ms += time_taken
        min_ms = min(min_ms, time_taken)
        max_ms = max(max_ms, time_taken)

        file_name = "response_{}.json".format(_)
        with open(os.path.join(folder_name, file_name), "w") as f:
            json.dump(response.json(), f)

    print("Total time:", total_ms / 1000, "s")
    print("Min time:", min_ms, "ms")
    print("Max time:", max_ms, "ms")
    print("Avg. time:", total_ms / iteration, "ms")

if __name__ == "__main__":
    main()