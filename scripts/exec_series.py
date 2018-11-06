import os
import time
from multiprocessing import Process
from read_hosts import invokerHosts, invokerMapping, testerHosts, testerMapping


def executeRemote(hostname, functionName, inputNum, processesPerHost):
    os.system("ssh ubuntu@{0} python -u - {1} {2} {3} {0} {4} < ./exec_remote.py > logs/log_{0}_{1}_{2}_{3}.txt"
              .format(hostname, functionName, inputNum, processesPerHost, testerMapping[hostname]))


def launchStatistics():
    print("Launching statistics...")
    for host in invokerHosts:
        os.system("ssh ubuntu@{0} 'bash -s' < statistics.sh & ".format(host))


def retrieveStatistics(functionName, inputNum, numOfProcesses):
    for host in invokerHosts:
        filename = "{0}_{1}_{2}_.txt".format(invokerMapping[host], inputNum, numOfProcesses)
        os.system("ssh ubuntu@{0} 'cat result_statistics' >> results/{1}/{2}"
                  .format(host, functionName, filename))
    print("Retrieved statistics.")


def runSeries(functionName, inputNum, numOfProcesses):
    proc = []
    processesPerHost = numOfProcesses / len(testerHosts)
    launchStatistics()
    print("Starting testing {0} with input={1} and {2} requests...".format(functionName, inputNum, numOfProcesses))
    startTime = time.time()

    for host in testerHosts:
        p = Process(target=executeRemote, args=(
            host, functionName, "{0}".format(inputNum), "{0}".format(processesPerHost),
        ))
        p.start()
        proc.append(p)

    for p in proc:
        p.join()

    timeDif = time.time() - startTime
    print("Completed all requests in {0} seconds".format(time.time() - startTime))
    retrieveStatistics(functionName.replace("-", "_"), inputNum, numOfProcesses)

    return timeDif
