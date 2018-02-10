![Title Picture](http://fouryears.eu/wp-content/uploads/2015/09/kdnuggets-jobs-2014-titles-300x177.jpg)

## Prerequisites

1. Install Kafka:
    - https://dzone.com/articles/running-apache-kafka-on-windows-os (install with binary file)

2. Install PostgreSQL
    - https://www.postgresql.org/download/

2. Install Python and pip
    - https://matthewhorne.me/how-to-install-python-and-pip-on-windows-10/

3. Install required Libraries

        $ pip install sodapy
        $ pip install kafka-python
        $ pip install psycopg2
        $ pip install sqlalchemy
        $ pip install bokeh
        $ pip install ipython-sql
        $ pip install gmaps

4. Activate gmaps Widget in Jupyter

        $ jupyter nbextension enable --py --sys-prefix widgetsnbextension
        $ jupyter nbextension enable --py --sys-prefix gmaps

5. Retrive Google Maps API Key for using Google Maps for visualization
  - http://jupyter-gmaps.readthedocs.io/en/latest/authentication.html

## Kafka Start Command

.\bin\windows\kafka-server-start.bat .\config\server.properties

## Helpful Links
1. https://medium.com/@shaaslam/installing-apache-kafka-on-windows-495f6f2fd3c8
2. https://github.com/xmunoz/sodapy
3. https://dev.socrata.com/docs/queries/
4. https://github.com/dpkp/kafka-python
5. https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9
6. https://kafka-python.readthedocs.io/en/master/apidoc/modules.html
7. https://www.cloudkarafka.com/blog/2016-12-13-part2-3-apache-kafka-for-beginners_example-and-sample-code-python.html
8. https://dev.socrata.com/foundry/data.cityofnewyork.us/fhrw-4uyv
9. https://suhas.org/sqlalchemy-tutorial/
10. https://dzone.com/articles/running-apache-kafka-on-windows-os
11. https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook
12. https://www.heise.de/developer/artikel/Effiziente-Datenverarbeitung-mit-Kafka-3877195.html?seite=all
13. https://github.com/catherinedevlin/ipython-sql
14. https://bokeh.pydata.org/en/latest/docs/user_guide/categorical.html#userguide-categorical
15. https://www.confluent.io/blog/simplest-useful-kafka-connect-data-pipeline-world-thereabouts-part-1/
16. https://docs.confluent.io/current/installation/installing_cp.html

## Further Links
1. http://jupyter-gmaps.readthedocs.io/en/latest/tutorial.html#basic-concepts
2. https://plot.ly/python/ipython-notebook-tutorial/
3. https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

# SQL Statements

``` sql
SELECT complaint_type, COUNT(complaint_type)
FROM service_request
GROUP BY complaint_type
HAVING COUNT(complaint_type) > 400 AND COUNT(complaint_type) < 8000
```
``` sql
SELECT descriptor, COUNT(descriptor)
FROM service_request
GROUP BY descriptor
HAVING COUNT(descriptor) > 8
```
``` sql
SELECT longitude, latitude
FROM service_request
WHERE complaint_type = 'Noise - Residential' AND latitude IS NOT NULL AND longitude IS NOT NULL
```
``` sql
SELECT DATE_TRUNC('day', created_date) AS dd, COUNT(created_date) AS daily_sum
FROM service_request WHERE EXTRACT(year from created_date) = '2017'
GROUP BY dd ORDER BY DATE_TRUNC('day', created_date)
```
``` sql
SELECT AVG(closed_date - created_date) AS avg_duration, MIN(closed_date - created_date) AS min_duration, MAX(closed_date - created_date) AS max_duration, complaint_type
FROM service_request
WHERE created_date IS NOT NULL AND closed_date IS NOT NULL
GROUP BY complaint_type
HAVING MAX(closed_date - created_date) < INTERVAL '365 days' AND MIN(closed_date - created_date) > '00:00:00'
ORDER BY avg_duration ASC
```
