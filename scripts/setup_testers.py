import subprocess
from read_hosts import testerHosts, testerMapping

for key in testerMapping.values():
    p = subprocess.Popen("../../incubator-openwhisk/bin/wskadmin user delete tester{0}".format(key),
                         stdout=subprocess.PIPE, shell=True)
    (output, _) = p.communicate()
    p.wait()
    print("tester{0}: {1}".format(key, output))

    p = subprocess.Popen("../../incubator-openwhisk/bin/wskadmin user create tester{0}".format(key),
                         stdout=subprocess.PIPE, shell=True)
    (auth, _) = p.communicate()
    p.wait()
    print("tester{0}: {1}".format(key, auth))

    subprocess.call(["./create_functions.sh", "tester{0}".format(key), auth])

    print("Finished for tester{0}".format(key))
