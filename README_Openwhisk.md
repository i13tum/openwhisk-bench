# Setting up Openwhisk

https://github.com/apache/incubator-openwhisk/blob/master/ansible/README_DISTRIBUTED.md is used as a base for this guide.

1. Clone the https://github.com/apache/incubator-openwhisk project.

2. On each of the host machines enable ssh access with the root user.

```
sudo passwd root
su root
cp /home/ubuntu/.ssh/authorized_keys /root/.ssh/
```

3. Define `remote_user = root` in the `ansible/ansible.cfg`.

4. List the host machine IPs in the `ansible/environments/distributed/hosts`.

5. Install a few utilities on the host machines:

```
apt-get update -y
apt-get install -y python2.7 python-pip unzip
echo "deb http://cz.archive.ubuntu.com/ubuntu trusty main" >> /etc/apt/sources.list
```
6. Prepare machines with ansible notebooks:

Ensure that the Ansible VM can authenticate to the OpenWhisk VMs via SSH using the following command.

`ansible all -i environments/distributed -m ping`

Generate config files

`ansible-playbook -i environments/distributed setup.yml`

Install prerequisites on OpenWhisk nodes.

`ansible-playbook -i environments/distributed prereq_build.yml`

Deploy registry.

`ansible-playbook -i environments/distributed registry.yml`

7. On each of the host machines:

Add the ip of the machine which hosts the docker registry (check the `ansible/environments/distributed/hosts`) into the list of insecure registries:
```
echo '{ "insecure-registries":["<registry_ip>:5000"]}' >> /etc/docker/daemon.json
```
Reboot the machine

Stop the docker service

`service docker stop`

Start docker

`nohup docker daemon -H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock &`

``

8. Build images and distribute them:

```
cd ..
./gradlew distDocker -PdockerHost=<registry_ip> -PdockerRegistry=<registry_ip>:5000
```

9. Setup Openwhisk with ansible playbook

```
cd ansible
ansible-playbook -i environments/distributed couchdb.yml
ansible-playbook -i environments/distributed initdb.yml
ansible-playbook -i environments/distributed wipe.yml
ansible-playbook -i environments/distributed openwhisk.yml

# installs a catalog of public packages and actions
ansible-playbook -i environments/distributed postdeploy.yml

# to use the API gateway
ansible-playbook -i environments/distributed apigateway.yml
ansible-playbook -i environments/distributed routemgmt.yml
```

10. Verify that everything is working

```
../bin/wsk property set --auth $(cat files/auth.whisk.system) --apihost <edge_url>
../bin/wsk -i -v action invoke /whisk.system/samples/helloWorld --blocking --result
```



