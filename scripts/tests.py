from exec_series import runSeries
from util import writeListToFile
import time
import sys
import os

functionNameArg = sys.argv[1:][0]


def runTest(testRequestsRange, testInputRange, resultFolder, functionName):
    os.system("rm -rf logs")
    os.system("mkdir -p logs")

    sleepBetweenTests = 60

    os.system("mkdir -p results/{0}".format(resultFolder))

    for input in testInputRange:
        result = []

        for requests in testRequestsRange:
            timeDiff = runSeries(functionName, input, requests)
            result.append(timeDiff)
            print("Completed testing with {0} requests for input {1}".format(requests, input))
            writeListToFile("results/{2}/time_{0}_{1}.txt".format(input, requests, resultFolder), result)
            time.sleep(sleepBetweenTests)

        print("Result {2}, {0}: {1}".format(result, input, functionName))


def compare_openwhisk_k8s_prime_number():
    testRequestRange100 = [100, 500, 1000, 2000, 3000, 4000]
    testInputRange100 = [100]
    runTest(testRequestRange100, testInputRange100, "prime_number", "prime-number")
    runTest(testRequestRange100, testInputRange100, "prime_number_k8s", "prime-number-k8s")

    testRequestRange2000 = [100, 500, 1000, 2000]
    testInputRange2000 = [2000]
    runTest(testRequestRange2000, testInputRange2000, "prime_number", "prime-number")
    runTest(testRequestRange2000, testInputRange2000, "prime_number_k8s", "prime-number-k8s")


def compare_openwhisk_k8s_weather():
    testRequestRange2000 = [50, 100, 500, 1000, 2000]
    testInputRange2000 = ["Munich"]
    runTest(testRequestRange2000, testInputRange2000, "weather", "weather")
    runTest(testRequestRange2000, testInputRange2000, "weather_k8s", "weather-k8s")


def compare_openwhisk_k8s_matrix():
    testRequestRange = [50, 100, 500, 1000, 2000]
    testInputRange50 = [50]
    testInputRange300 = [300]

    runTest(testRequestRange, testInputRange50, "matrix", "matrix")
    runTest(testRequestRange, testInputRange50, "matrix_k8s", "matrix-k8s")

    runTest(testRequestRange, testInputRange300, "matrix", "matrix")
    runTest(testRequestRange, testInputRange300, "matrix_k8s", "matrix-k8s")


def compare_openwhisk_k8s_matrix_inputs():
    testRequestRange = [1500]
    testInputRange50 = [50, 100, 200, 300, 500]

    runTest(testRequestRange, testInputRange50, "matrix", "matrix")
    runTest(testRequestRange, testInputRange50, "matrix_k8s", "matrix-k8s")


def compare_js_java_prime_number():
    testRequestRange100 = [100, 500, 1000, 2000, 3000, 4000, 10000]
    testInputRange100 = [100]
    runTest(testRequestRange100, testInputRange100, "prime_number", "prime-number")
    runTest(testRequestRange100, testInputRange100, "prime_number_java", "prime-number-java")

    testRequestRange2000 = [100, 500, 1000, 2000, 5000]
    testInputRange2000 = [2000]
    runTest(testRequestRange2000, testInputRange2000, "prime_number", "prime-number")
    runTest(testRequestRange2000, testInputRange2000, "prime_number_java", "prime-number-java")


def compare_js_java_weather():
    testRequestRange = [50, 100, 500, 1000, 2000]
    testInputRange100 = ["Munich"]
    runTest(testRequestRange, testInputRange100, "weather", "weather")
    runTest(testRequestRange, testInputRange100, "weather_java", "weather-java")


def compare_js_java_matrix():
    testRequestRange = [50, 100, 500, 1000, 2000]
    testInputRange50 = [50]
    testInputRange300 = [300]

    runTest(testRequestRange, testInputRange50, "matrix", "matrix")
    runTest(testRequestRange, testInputRange50, "matrix_java", "matrix-java")

    runTest(testRequestRange, testInputRange300, "matrix", "matrix")
    runTest(testRequestRange, testInputRange300, "matrix_java", "matrix-java")


def scaling_prime_number():
    testRequestRange100 = [100, 500, 1000, 2000, 3000, 5000]
    testInputRange100 = [10, 1000, 3000]
    runTest(testRequestRange100, testInputRange100, "prime_number", "prime-number")


def scaling_weather():
    testRequestRange = [50, 100, 500, 1000, 2000]
    testInputRange100 = ["Munich"]
    runTest(testRequestRange, testInputRange100, "weather", "weather")


def scaling_matrix():
    testRequestRange = [1000]
    testInputRange = [300]

    runTest(testRequestRange, testInputRange, "matrix", "matrix")


def scaling_db_get():
    testRequestRange = [2000]
    testInputRange = [1, 2, 3, 4, 5]

    runTest(testRequestRange, testInputRange, "db_get", "db-get")


def extra_load_prime_number():
    testRequestRange = [20000]
    testInputRange = [20000]
    runTest(testRequestRange, testInputRange, "prime_number", "prime-number")


def scaling_intensity_based():
    testRequestRange = [5000]
    testInputRange = [100]
    runTest(testRequestRange, testInputRange, "prime_number", "prime-number")
    testRequestRange = [60]
    testInputRange = [10000]
    runTest(testRequestRange, testInputRange, "prime_number", "prime-number")

    testRequestRange = [2000]
    testInputRange = [100]
    runTest(testRequestRange, testInputRange, "matrix", "matrix")
    testRequestRange = [60]
    testInputRange = [500]
    runTest(testRequestRange, testInputRange, "matrix", "matrix")


def prime_number_appendix():
    testRequestRange100 = [100, 500, 1000, 2000, 3000, 4000]
    testInputRange100 = [10, 500, 3000, 5000]
    runTest(testRequestRange100, testInputRange100, "prime_number", "prime-number")


def matrix_appendix():
    testRequestRange = [50, 100, 500, 1000, 2000, 3000]
    testInputRange50 = [50, 100, 300, 400]

    runTest(testRequestRange, testInputRange50, "matrix", "matrix")


funcOptions = {
    "compare_openwhisk_k8s_prime_number": compare_openwhisk_k8s_prime_number,
    "compare_openwhisk_k8s_weather": compare_openwhisk_k8s_weather,
    "compare_openwhisk_k8s_matrix": compare_openwhisk_k8s_matrix,
    "compare_js_java_prime_number": compare_js_java_prime_number,
    "compare_js_java_weather": compare_js_java_weather,
    "compare_js_java_matrix": compare_js_java_matrix,
    "scaling_prime_number": scaling_prime_number,
    "scaling_weather": scaling_weather,
    "scaling_matrix": scaling_matrix,
    "scaling_db_get": scaling_db_get,
    "extra_load_prime_number": extra_load_prime_number,
    "scaling_intensity_based": scaling_intensity_based,

    "prime_number_appendix": prime_number_appendix,
    "matrix_appendix": matrix_appendix
}

funcOptions[functionNameArg]()