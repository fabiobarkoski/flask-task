
# Flask Task

A Flask blueprint developed to the Test Task

## Summary

- [Installation](#installation)
- [Running Tests](#running-tests)
- [Docker](#docker)
- [Blueprint Reference](#blueprint-reference)
- [Author](#author)

## Installation

Clone the project

```bash
  git clone https://github.com/fabiobarkoski/flask-task.git
```

Go to the project directory

```bash
  cd flask-task
```

Current to install the dependencies you need the package manager [Poetry](https://python-poetry.org/docs/). After installed type.

```bash
  poetry install
```

To start the App

```bash
  gunicorn --chdir ./src/ app:app
```

## Running Tests

To run tests, run the following command

```bash
  pytest
```

## Docker

To build a image, run the following command inside the project folder

```bash
  docker build -t flask-task .
```

And after run

```bash
  docker run -p 8000:8000 flask-task
```

## Blueprint Reference

#### Calculate the distance

```http
  GET /${adress}
```

| Parameter | Type     | Description                       | Response                       |
| :-------- | :------- | :-------------------------------- | :-------------------------------- 
| `adress`      | `string` | **Required**. The adress to calculate the distance | If not in MKAD, save the response on the `distance.log` file |

  
## Author

- [@fabiobarkoski](https://www.github.com/fabiobarkoski)

  