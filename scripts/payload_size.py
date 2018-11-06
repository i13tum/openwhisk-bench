import random, string, time, requests

url = "https://172.24.42.82:443/api/v1/web/tester1/default/payload-size.json"

payloadSizeOptions = [10, 1000, 50000, 500000, 750000, 1000000]

result = []

for size in payloadSizeOptions:
    data = {"payload": ''.join(random.choice(string.lowercase) for x in range(size))}
    timeStart = time.time()
    response = requests.post(url, json=data, verify=False)
    print("Completed with code {0}".format(response.status_code))
    result.append(time.time() - timeStart)

print(result)