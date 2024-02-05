# Kubernetes
Kubernetes is an open-source platform designed to automate deploying, scaling, and operating application containers. It groups containers that make up an application into logical units for easy management and discovery. Kubernetes is highly flexible and supports a wide range of container tools, including Docker.

## Key Concepts of Kubernetes
- Pods: The smallest deployable units created and managed by Kubernetes. A Pod represents a single instance of a running process in your cluster and can contain one or more containers.
- Services: An abstract way to expose an application running on a set of Pods as a network service. It provides a consistent endpoint for accessing the pods.
- Deployments: Manages the creation and updating of Pods. Using Deployments, you can declare the desired state of your application, and Kubernetes will manage the deployment to that state.
- Nodes: The physical or virtual machines that make up the cluster. Each node is managed by the master and contains the services necessary to run Pods.
- Namespaces: Allows you to partition resources into logically named groups, which can help you manage different environments within the same cluster (e.g., development, test, and production).

## Kubernetes CLI (kubectl)
The Kubernetes command-line tool, kubectl, allows you to run commands against Kubernetes clusters. You can use kubectl to deploy applications, inspect and manage cluster resources, and view logs.

- Get Information About Cluster Resources

    - List all pods in all namespaces:
```sh
kubectl get pods --all-namespaces
```
    - List all services in the default namespace:
```sh
kubectl get services
```

- Create and Manage Kubernetes Resources

    - Create resources using a file:
```sh
kubectl apply -f deployment.yaml
```
    - Delete a deployment:
```sh
kubectl delete deployment my-deployment
```

- Interacting with Pods and Containers

    - Execute a command in a container:
```sh
kubectl exec -it <pod-name> -- bash
```
    - Get logs for a pod:
```sh
kubectl logs <pod-name>
```

- Managing Deployments
    - Create a deployment:
```sh
kubectl create deployment my-deployment --image=myimage
```
    - Update a deployment:
```sh
kubectl set image deployment/my-deployment my-container=myimage:version
```

- Working with ConfigMaps and Secrets
    - Create a ConfigMap:
```sh
kubectl create configmap my-config --from-literal=key1=value1 --from-literal=key2=value2
```
    - Create a secret:
```sh
kubectl create secret generic my-secret --from-literal=password=mypassword
```
kubectl Configuration and Contexts

    - Kubeconfig Files: kubectl uses a configuration file (usually ~/.kube/config) to store cluster credentials and settings. You can specify a different configuration file by setting the KUBECONFIG environment variable or by using the --kubeconfig flag.
    - Kubeconfig File Structure
A kubeconfig file typically contains the following main sections:

        - clusters: Lists the Kubernetes clusters you have access to, including the cluster name and connection details.
        - users: Defines user credentials for accessing the clusters.
        - contexts: Combines a cluster, a user, and a namespace to use as a current working environment.
        - current-context: Specifies the default context to use for commands.

    - Contexts: A context in kubectl is a combination of a cluster, namespace, and user. You can switch between contexts using:
```sh
kubectl config use-context my-context
```

- Example: Deploying an NGINX Deployment
  
1. Create a Deployment YAML File (nginx-deployment.yaml):
```yaml
Copy code
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```
1. Deploy the NGINX Deployment:
```sh
kubectl apply -f nginx-deployment.yaml
```

1. Verify the Deployment:
```sh
kubectl get deployments
```

1. Access the NGINX Application (assuming you have a Service exposing NGINX):
    - Get the Service endpoint:
```sh
kubectl get service nginx-service
```