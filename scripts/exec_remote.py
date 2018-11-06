import concurrent.futures
import sys
import time

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

functionNameArg = sys.argv[1:][0]
inputArg = sys.argv[1:][1]
numOfProcessesArg = int(sys.argv[1:][2])
testerHostArg = sys.argv[1:][3]
testerKeyArg = sys.argv[1:][4]

mysqlHost = "172.24.63.183"
apiHost = "172.24.42.82"
namespace = "tester{0}".format(testerKeyArg)
k8sHost = "172.24.42.47:30899"

ramLoader = 69999


def runPrimeNumber(inputNum):
    return "https://{0}:443/api/v1/web/{1}/default/prime-number.json?num={2}".format(apiHost, namespace, inputNum)


def runMatrix(inputNum):
    return "https://{0}:443/api/v1/web/{1}/default/matrix.json?size={2}&ramLoader={3}".format(apiHost, namespace, inputNum, ramLoader)


def runWeather(inputStr):
    return "https://{0}:443/api/v1/web/{1}/default/weather.json?location={2}".format(apiHost, namespace, inputStr)


def runDb(inputNum):
    return "https://{0}:443/api/v1/web/{1}/default/db-get.json?MYSQL_HOSTNAME={2}&MYSQL_USERNAME={3}&" \
           "MYSQL_PASSWORD={4}&MYSQL_DATABASE={5}&delay={6}"\
        .format(apiHost, namespace, mysqlHost, "root", "aa", "test", inputNum)


def runPayloadSize(stringSize):
    return "https://{0}:443/api/v1/web/{1}/default/payload-size.json?".format(apiHost, namespace)


def runPrimeNumberJava(inputNum):
    return "https://{0}:443/api/v1/web/{1}/default/prime-number-java.json?num={2}".format(apiHost, namespace, inputNum)


def runMatrixJava(inputNum):
    return "https://{0}:443/api/v1/web/{1}/default/matrix-java.json?size={2}&ramLoader={3}".format(apiHost, namespace, inputNum, ramLoader)


def runWeatherJava(inputStr):
    return "https://{0}:443/api/v1/web/{1}/default/weather.json?location={2}".format(apiHost, namespace, inputStr)


def runPrimeNumberK8s(inputNum):
    return "http://{0}/prime-number?num={1}".format(k8sHost, inputNum)


def runMatrixK8s(inputNum):
    return "http://{0}/matrix?size={1}&ramLoader={2}".format(k8sHost, inputNum, ramLoader)


def runWeatherK8s(inputStr):
    return "http://{0}/weather?location={1}".format(k8sHost, inputStr)


funcOptions = {
    "prime-number": runPrimeNumber,
    "matrix": runMatrix,
    "weather": runWeather,
    "db-get": runDb,
    "prime-number-java": runPrimeNumberJava,
    "matrix-java": runMatrixJava,
    "weather-java": runWeatherJava,
    "prime-number-k8s": runPrimeNumberK8s,
    "matrix-k8s": runMatrixK8s,
    "weather-k8s": runWeatherK8s,
}


def get(url):
    try:
        time.sleep(0.001)
        return requests.get(url, verify=False)
    except:
        print("Delay due to a request error")
        time.sleep(0.01)
        return get(url)


def runInParallel(functionName, input, numOfProcesses):
    print("Starting testing on host {0} with namespace {1}...".format(testerHostArg, namespace))

    with concurrent.futures.ThreadPoolExecutor(max_workers=numOfProcesses) as executor:
        futures = executor.map(
            get, [
                funcOptions[functionName](input)
                for _ in range(numOfProcesses)
            ])
        for response in futures:
            if response is None:
                print('No response was received')
            else:
                print('{0} {1}: {2}'.format(time.time(), response.status_code, response.content))


    print("Completed processing requests on host {0}".format(testerHostArg))


runInParallel(functionNameArg, inputArg, numOfProcessesArg)
