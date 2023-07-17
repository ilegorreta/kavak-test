# Kavak-test - Exercise 1

This repository contains the first exercise for the Data Engineering Test.

Here are the exercise instructions:

### Ejercicio 1 (Desarrollar en Pandas) [tiempo estimado: 1 hr]
Descarga la Base de datos histórica de [Quién es Quién en los Precios de Profeco](https://datos.gob.mx/busca/dataset/quien-es-quien-en-los-precios) y resuelve los
siguientes incisos. Para el procesamiento de los datos y el análisis exploratorio debes usar Python
Pandas sin ocupar funciones puras de python.
1. ¿Cuántos registros hay?
2. ¿Cuántas categorías?
3. ¿Cuántas cadenas comerciales están siendo monitoreadas (y, por lo tanto, reportadas
en esa base de datos)?
4. ¿Cuáles son los productos más monitoreados en cada estado de la república?
5. ¿Cuál es la cadena comercial con mayor variedad de productos monitoreados?
6. Encuentra algún dato curioso en los datos y comunícalo en un slide de powerpoint.

## Initial Considerations

It is noteworthy to mention that the API endpoint for this resource is broken:
https://api.datos.gob.mx/v1/profeco.precios
So it was not possible to make an API call to retrieve the information. As a workaround I needed to download a CSV file containing information from February 2022 and get the insights from that dataset.

This project uses [Visual Studio Code](https://code.visualstudio.com/) and the [devcontainer feature](https://code.visualstudio.com/docs/devcontainers/containers) to run the code with all the required dependencies.

It is also posible to manually create a Docker image based on this Dockerfile and to enter a container using that image (that's basically what VSCode DevContainer is doing under the hood).

## Requirements

- Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)

- Install [Visual Studio Code](https://code.visualstudio.com/download)

- Install the [VS Code Remote Development pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

## Setup

1. Install required tools 

2. Git clone this repo to your laptop

3. Open the local repo folder in VS Code

4. Open the [VS Code command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) and select/type 'Reopen in Container'

5. Wait while the devcontainer is built and initialized, this may take several minutes

6. Run ```python /app/src/main.py``` within the DevContainer in VS Code

## Directory Tree Structure
It is noteworthy pointing out the directory structure of the repository:
```
├── .devcontainer
│   └── devcontainer.json
├── Dockerfile
├── README.md
├── data
│   └── precios_profeco_2022.csv
├── requirements.txt
└── src
    ├── constants.py
    ├── ejercicio_1_utils.py
    └── main.py
```
## Future Considerations
Some worthy future considerations to improve this project could be to add GitHub Actions to create CI/CD jobs everytime a commit is pushed to this repository, so we can automate the execution of unit testing. Additionally, it would be great to continue troubleshooting the API endpoint so we can download data directly from the API, instead of downloading a CSV file. 

## Developed by: Ivan Legorreta
**Phone number**: +52 (55)1320-7574

**Email**: ilegorreta@outlook.com
