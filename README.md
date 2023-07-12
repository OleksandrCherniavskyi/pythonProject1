# pythonProject1
This project is a Django-based web application that analyzes and presents information about the IT sector in the Polish region using a database. The data is obtained from the [JustJoin.It API](https://justjoin.it/) and is updated daily through continuous integration and deployment (CI/CD) using GitHub Actions.

## Features
The start page allows users to select a specific time period for viewing analytics.
Main charts provide insights such as:
- Top positions in the IT sector.
- Top specializations in the field.
- Number of positions available on a daily and weekly basis.
- Skill ratings for each position and specialization.


## Getting Started
To run the project using the Docker file, follow these steps:

Clone the repository:

Copy code
```bash
git clone https://github.com/OleksandrCherniavskyi/pythonProject1.git
```
Build the Docker image:

Copy code
```docker
docker build -t image_name .
```

Run the Docker container:

Copy code
```docker
docker run -p 8080:8080 image_name
```
The application will be accessible at http://localhost:8080.



