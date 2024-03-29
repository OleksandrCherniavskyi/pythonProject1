# [pythonProject1](https://t7q6wq-8080.csb.app/)
This project is a Django-based web application that analyzes and presents information about the IT sector in the Polish region using a database. The data is obtained from the [JustJoin.It API](https://justjoin.it/) and is updated daily through continuous integration and deployment (CI/CD) using GitHub Actions.

## Unfortunately, starting from September 25, 2023, Justjoin has been updated, and access to the API has been closed. 
- This project does not have a positive value for me, and I will not be finding a new solution
- I have backed up the old SQLite database and closed the PostgreSQL database.


## Features
The start page allows users to select a specific time period for viewing analytics.
Main charts provide insights such as:
- Top positions in the IT sector.
- Top specializations in the field.
- Number of positions available on a daily and weekly basis.
- Skill ratings for each position and specialization.

Link to page https://t7q6wq-8080.csb.app/

## Getting Started
To run the project using the Docker file, follow these steps:

Clone the repository:


```bash
git clone https://github.com/OleksandrCherniavskyi/pythonProject1.git
```
Build the Docker image:


```docker
docker build -t image_name .
```

Run the Docker container:


```docker
docker run -p 8080:8080 image_name
```
The application will be accessible at http://localhost:8080.


### Update branch in [codesandbox.io](https://codesandbox.io/p/github/OleksandrCherniavskyi/pythonProject1/draft/recursing-cerf?layout=%257B%2522sidebarPanel%2522%253A%2522EXPLORER%2522%252C%2522rootPanelGroup%2522%253A%257B%2522direction%2522%253A%2522horizontal%2522%252C%2522contentType%2522%253A%2522UNKNOWN%2522%252C%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522id%2522%253A%2522ROOT_LAYOUT%2522%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522contentType%2522%253A%2522UNKNOWN%2522%252C%2522direction%2522%253A%2522vertical%2522%252C%2522id%2522%253A%2522cljx7c3c5000g356mmd82hphu%2522%252C%2522sizes%2522%253A%255B69.50900164000001%252C30.490998359999992%255D%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522contentType%2522%253A%2522EDITOR%2522%252C%2522direction%2522%253A%2522horizontal%2522%252C%2522id%2522%253A%2522EDITOR%2522%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL%2522%252C%2522contentType%2522%253A%2522EDITOR%2522%252C%2522id%2522%253A%2522cljx7c3c5000b356mt9fi4bi3%2522%257D%255D%252C%2522sizes%2522%253A%255B100%255D%257D%252C%257B%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522contentType%2522%253A%2522SHELLS%2522%252C%2522direction%2522%253A%2522horizontal%2522%252C%2522id%2522%253A%2522SHELLS%2522%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL%2522%252C%2522contentType%2522%253A%2522SHELLS%2522%252C%2522id%2522%253A%2522cljx7c3c5000f356m5lkt4ynz%2522%257D%255D%252C%2522sizes%2522%253A%255B100%255D%257D%255D%257D%252C%257B%2522type%2522%253A%2522PANEL_GROUP%2522%252C%2522contentType%2522%253A%2522DEVTOOLS%2522%252C%2522direction%2522%253A%2522vertical%2522%252C%2522id%2522%253A%2522DEVTOOLS%2522%252C%2522panels%2522%253A%255B%257B%2522type%2522%253A%2522PANEL%2522%252C%2522contentType%2522%253A%2522DEVTOOLS%2522%252C%2522id%2522%253A%2522cljx7c3c5000d356mwceb135q%2522%257D%255D%252C%2522sizes%2522%253A%255B100%255D%257D%255D%252C%2522sizes%2522%253A%255B50%252C50%255D%257D%252C%2522tabbedPanels%2522%253A%257B%2522cljx7c3c5000b356mt9fi4bi3%2522%253A%257B%2522id%2522%253A%2522cljx7c3c5000b356mt9fi4bi3%2522%252C%2522activeTabId%2522%253A%2522cll1aw31t02rk356mh7rrlsvg%2522%252C%2522tabs%2522%253A%255B%257B%2522id%2522%253A%2522cljx7c3c5000a356myn8txfxy%2522%252C%2522mode%2522%253A%2522permanent%2522%252C%2522type%2522%253A%2522FILE%2522%252C%2522filepath%2522%253A%2522%252FREADME.md%2522%252C%2522state%2522%253A%2522IDLE%2522%257D%252C%257B%2522type%2522%253A%2522FILE%2522%252C%2522filepath%2522%253A%2522%252Fmy_page%252Fchart%252Fviews.py%2522%252C%2522id%2522%253A%2522cll1aw31t02rk356mh7rrlsvg%2522%252C%2522mode%2522%253A%2522permanent%2522%252C%2522state%2522%253A%2522IDLE%2522%257D%255D%257D%252C%2522cljx7c3c5000d356mwceb135q%2522%253A%257B%2522id%2522%253A%2522cljx7c3c5000d356mwceb135q%2522%252C%2522activeTabId%2522%253A%2522cll1aerlk027m356m7yyot2ko%2522%252C%2522tabs%2522%253A%255B%257B%2522type%2522%253A%2522UNASSIGNED_PORT%2522%252C%2522port%2522%253A8080%252C%2522id%2522%253A%2522cll1aerlk027m356m7yyot2ko%2522%252C%2522mode%2522%253A%2522permanent%2522%252C%2522path%2522%253A%2522%2522%257D%255D%257D%252C%2522cljx7c3c5000f356m5lkt4ynz%2522%253A%257B%2522id%2522%253A%2522cljx7c3c5000f356m5lkt4ynz%2522%252C%2522activeTabId%2522%253A%2522cll1aeped01sp356m842gdlhv%2522%252C%2522tabs%2522%253A%255B%257B%2522id%2522%253A%2522cljx7c3c5000e356mbdrj498s%2522%252C%2522mode%2522%253A%2522permanent%2522%252C%2522type%2522%253A%2522TERMINAL%2522%252C%2522shellId%2522%253A%2522cll3fcwuc003ad7gn0nwufa5c%2522%257D%252C%257B%2522type%2522%253A%2522TASK_LOG%2522%252C%2522taskId%2522%253A%2522docker%2520build%2520-t%2520image_name%2520.%2522%252C%2522id%2522%253A%2522cll1ad2jr010m356mm4af3xhu%2522%252C%2522mode%2522%253A%2522permanent%2522%257D%252C%257B%2522type%2522%253A%2522TASK_LOG%2522%252C%2522taskId%2522%253A%2522docker%2520run%2520-p%25208080%253A8080%2520image_name%2522%252C%2522id%2522%253A%2522cll1aeped01sp356m842gdlhv%2522%252C%2522mode%2522%253A%2522permanent%2522%257D%255D%257D%257D%252C%2522showDevtools%2522%253Atrue%252C%2522showShells%2522%253Atrue%252C%2522showSidebar%2522%253Atrue%252C%2522sidebarPanelSize%2522%253A15%257D)
- git fetch
- git merge origin/master


### Migrate from SQLite to PostgreSQL
- I migrate used django manage.py
- in terminal used command ```.\manage.py dumpdata``` to export data from SQLite in JSON
- i've some error, i fixed use ```set PYTHONIOENCODING=utf-8```
  - ```.\manage.py dumpdata chart.Offers  > dboffers.json```
  - ```.\manage.py dumpdata chart.Brands  > dbbrands.json```
  - ```.\manage.py dumpdata chart.Skills  > dbskills.json```
  - ```.\manage.py dumpdata chart.EmploymentTypes  > dbet.json```
  - ```.\manage.py dumpdata chart.BrandsOffice  > dbbo.json```
- create PostgreSQL database (i chose RDS from AWS)
- create table in PostgreSQL
- change connectin in setting.py to new DB 
- import data in database use ```.\manage.py loaddata```
  - ```.\manage.py loaddata dbbrands.json```
  - ```.\manage.py loaddata dboffers.json```
  - ```.\manage.py loaddata dbskills.json```
  - ```.\manage.py loaddata dbet.json```
  - ```.\manage.py loaddata dbbo.json```
