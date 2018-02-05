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

## Interessante Links
1. http://jupyter-gmaps.readthedocs.io/en/latest/tutorial.html#basic-concepts
2. https://plot.ly/python/ipython-notebook-tutorial/
3. https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

# SQL Statements

``` sql
select complaint_type, count(complaint_type) from service_request group by complaint_type having count(complaint_type) > 400 and count(complaint_type) < 8000
```
``` sql
select descriptor, count(descriptor) from service_request group by descriptor having count(descriptor) > 8
```
``` sql
SELECT longitude, latitude from service_request where complaint_type = 'Noise - Residential' and latitude is not null and longitude is not null
```
``` sql
SELECT date_trunc('day', created_date) AS dd, count(created_date) as daily_sum FROM service_request where EXTRACT(year from created_date) = '2017' GROUP BY dd ORDER BY date_trunc('day', created_date)
```
noch ein Statement für alle offenen und geschlossenen Request
