# OpenWhisk Benchmarking Framework 

A Distributed Analysis and Benchmarking Framework for Apache OpenWhisk Serverless Platform – Demo Paper: https://dl.acm.org/citation.cfm?id=3284016


# Update config files

The **scripts/config/invoker_hosts** and **scripts/config/tester_hosts** files have to be updated with the actual IPs of Openwhisk invoker machines and tester machines correspondingly. The count of machines in each case can be absolutely arbitrary, and the framework will take it into account automatically.

Also update relevant URLs in the upper part of the **exec_remote.py** script, i.e. the host of the Openwhisk API, Kubernetes API and the MySQL instance.

# Prepare tester machines

To make the scripts work correctly, make sure that the following software is installed on all tester machines: Python, Python packages **futures** and **requests**.

```
sudo apt-get update -y
sudo apt-get install -y python2.7 python-pip

export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo dpkg-reconfigure locales

pip install futures
pip install requests
```

Also make sure that the host which is used as the starting point for the framework, has an SSH access to all the tester machines with login **ubuntu**.

# Prepare namespaces and actions

Next, create jar files for functions implemented in Java by executing the **functions/java/create_jars.sh** script. Further, namespaces and actions have to be created for further test case executions. It can be done manually via WSK CLI, however, with a larger number of tester machines this would be a long tedious task. A simple execution of the script **setup_testers.py** without any arguments creates a number of namespaces equal to the number of tester machines and creates sample functions for each of the namespaces. In case something in the action configurations has to be changed, such as the RAM quota or timeout values, it can be done in the script **create_functions.sh**.

# Execute a test case

The script **tests.py** is supposed to be used to execute a test case. There is a number of test cases which are already defined in the script. The general syntax is the following:

`python tests.py test_case_name`

Each test case is internally executing the script **exec_series.py**, which is responsible for a single test execution and accepts the name of the function, the function input and the number of concurrent requests as an input.

Sometimes right after Openwhisk was setup, an attempt to run a test against it fails, with Openwhisk returning 502 for every request. I have no found the reason why this happens, and only a full redeploy of Openwhisk helps to fix it.

# Statistics

After the test case execution was finished, the results are available in the **results** folder in the root of the project. The results within the folder are distributed into directories named as the executed sample functions. Within each of the folders:

* Files pulled from invokers, containing two columns: CPU and RAM usage on the specific Openwhisk invoker. The file naming follows the following pattern: *invokerId_functionInput_numberOfConcurrentRequests_.txt*.
  
* Files containing the execution duration. The file naming pattern is the following: *time_functionInput_numberOfConcurrentRequests_.txt*.

Statistics can be evaluated and visualized with Jupyter notebooks. Examples can be seen in the **results_final** directory.
