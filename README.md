

# Flask Task

A Flask blueprint developed to the Test Task

## Summary

- [Installation](#installation)
- [Running Tests](#running-tests)
- [Docker](#docker)
- [DOcumentation](#documentation)
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

## Documentation

To calculate the distance between the Moscow Ring Road and an adress I used the Haversine Formula. So to check the distance the application just need a coordinate or a name of a place/adress.

### The Blueprint

The blueprint calculate by checking the GET Request.
- If the request is a coordinate, then the blueprint will check if the adress is inside the Moscow Ring Road, if not the blueprint will calculate the distance and after add the result to the `distance.log` file
- If is an adress. The blueprint will get the coordinate through a Geocoder API and then will do the same steps, check if it is inside the Moscow Ring Road, if not will calculate and add the result to the `distance.log` file

### HTTP Request

```http
  GET /${adress}
```

| Parameter | Type     | Description                       | Response                       |
| :-------- | :------- | :-------------------------------- | :-------------------------------- 
| `adress`      | `string` | **Required**. The adress to calculate the distance | If not inside the MKAD, save the response on the `distance.log` file |

### Examples

In the exemples I will use the coordinates of 2 places, 1 is the coordinate of Maryina Roshcha  that is inside the MKAD and the another is the London coordinate

```http
  GET /55.79691668126746, 37.599703014240795 //Maryina Roshcha coordinate
```
For being inside the MKAD, the blueprint will not calculate and add to `distance.log` file

```http
  GET /51.50173484532344, -0.1254902875175711 //London coordinate
```

For being outside the MKAD, the blueprint will calculate and add to `distance.log` file. The .log file will seem like this:

```bash
  2021-08-25 17:49:58,199:INFO:blueprint_view.py:The distance from Moscow Ring Road to 51.50173484532344, -0.1254902875175711 is 2515 km
```

## Author

- [@fabiobarkoski](https://www.github.com/fabiobarkoski)

