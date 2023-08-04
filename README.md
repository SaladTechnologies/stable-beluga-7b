## Benchmarking script for Salad Cloud API
This script is to benchmark the performance of the stable-beluga-7b on Salad Portal. It makes a request to the API along with certain parameters, such as the API key, access domain name, and data. The results of the request are then saved to a file.

## How to run the script
To run the script, you will need to have Python installed. You can then save the script as a .py file and run it from the command line. For example, if you have saved the script as benchmark.py, you can run it by typing the following command into the command line:

```
python benchmark.py
```

This will run the script and save the results to a file.

## Parameters
The script requires the following parameters:

- domain_name: The domain name of the Salad Cloud API.
- api_key: The API key for the Salad Cloud API.
- data: The data to be sent to the Salad Cloud API.

## Building the Docker Image

First, [download the model](https://huggingface.co/stabilityai/StableBeluga-7B/tree/main) from Huggingface to a directory called `./stable-beluga-7b-gpu-docker/model`.

From project root:
```shell
docker build -t saladtechnologies/stable-beluga-7b:latest -f ./stable-beluga-7b-gpu-docker/Dockerfile ./stable-beluga-7b-gpu-docker
```

## Running the Docker Container

```shell
docker run --gpus all -p 8888:8888 saladtechnologies/stable-beluga-7b:latest
```