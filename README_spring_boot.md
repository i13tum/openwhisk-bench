The spring boot project is located in **/spring-boot-functions**.

To have it deployed on a Kubernetes cluster do the following:
1) Build an image from the Dockerfile,
2) Push the image to a remote Docker repository (e.g. I used my personal account on Docker Hub),
3) Create a deployment and a service  from the docker image. It is a standard process described in tutorials. I followed https://medium.com/platformer-blog/getting-started-with-kubernetes-deploy-a-docker-container-with-kubernetes-in-5-minutes-eb4be0e96370, with the only difference that I used `NodePort` type of the deployment instead of `LoadBalancer`.
