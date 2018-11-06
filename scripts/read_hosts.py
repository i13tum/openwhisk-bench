from util import readFileToArray

invokerHostsFile = "config/invoker_hosts"
testerHostsFile = "config/tester_hosts"


def createMapping(arr):
    result = {}
    inc = 0
    for el in arr:
        result[el] = inc
        inc = inc + 1
    return result


invokerHosts = readFileToArray(invokerHostsFile)
invokerMapping = createMapping(invokerHosts)

testerHosts = readFileToArray(testerHostsFile)
testerMapping = createMapping(testerHosts)