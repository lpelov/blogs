# Running Dolly 2.0

EXPERIMENT to run Dolly in a VSCode DevContainer!!!

You can build and use your own container for local use and when ready take it to the Cloud for example by using Oracle Cloud Data Science Jobs Service. To run the job, you have to make your own Dockerfile, and build an image. In this example the `Dockerfile` is designed so that you can make builds for local and remote cloud runs.

You use the local build when you test locally against your code. During the local development, you don't need to build a new image for every code change. Use the remote cloud option to run the Dockerfile when you think your code is complete, and you want to run it in the cloud with the code inside.

## Prerequisite

- Install [Docker](<https://docs.docker.com/get-docker>) **or** [Rancher Desktop](<https://rancherdesktop.io/>) as a free alternative to docker

## Build and Run

### Build to test run locally

Builds the docker image but does not include the code for quick run, debug etc.

```bash
docker build --build-arg type=local -t dolly2 .
```

:exclamation:On Apple Silicon

```bash
docker buildx build --platform linux/amd64 --build-arg type=local -t dolly2 .
```

### Run local run and test

```bash
docker run --platform linux/amd64 --rm -v $PWD:/app dolly2 sleep infinity
```

### Add devcontainer.json

For local use I would recommend you using the VSCode Dev Container feature.

```json
// For format details, see https://aka.ms/devcontainer.json. For config options, see the
// README at: https://github.com/devcontainers/templates/tree/main/src/docker-existing-dockerfile
{
 "name": "Dolly 2.0",
 "image": "dolly2",
 // Features to add to the dev container. More info: https://containers.dev/features.
 // "features": {},

 // Use 'forwardPorts' to make a list of ports inside the container available locally.
 // "forwardPorts": [],

 // Uncomment the next line to run commands after the container is created.
 // "postCreateCommand": "cat /etc/os-release",

 // Configure tool-specific properties.
 "customizations": {
  "vscode": {
   "extensions": ["ms-python.python", "ms-toolsai.jupyter", "ms-azuretools.vscode-docker", "ms-python.isort", "eamodio.gitlens"]
  }
 },

 "mounts": [
  "source=/Users/LYPELOV/development/GitHub/blogs/dolly-2.0,target=/app,type=bind"
 ]

 // Uncomment to connect as an existing user other than the container default. More info: https://aka.ms/dev-containers-non-root.
 // "remoteUser": "devcontainer"
}
```
