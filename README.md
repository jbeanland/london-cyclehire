# London and Oslo Cyclehire Data

## A brief look at cyclehire data from two cities.

The dataset used for London is available from [Data.world](https://data.world/makeovermonday/london-cycle-hire-usage), otherwise the raw data is freely available from [data.london.gov.uk](data.london.gov.uk) through TFL's website.

`Overview.ipynb` looks at where there is the greatest disparity between bikes being added or removed and the capacity of a bike-point over the course of a single day as a way of looking for where and how much TFL is load-balancing the system. Spoiler, its mostly train stations.

`Waterloo.ipynb` looks at Waterloo Station specifically, treating the 3 bike-points there as one and building a model to predict the number bikes removed on a given day.


For `Oslo.ipynb`, data was collected from [the public api](https://developer.oslobysykkel.no/api) for the cycle scheme by running `collect_data.py` at 10 minute intervals for 1 day. The notebook then looks for load balancing performed on the system through the differences in bike numbers from one record to the next.
