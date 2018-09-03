# London Cyclehire Data

## A brief look at London cyclehire data.

The dataset used is available from [Data.world](https://data.world/makeovermonday/london-cycle-hire-usage), otherwise the raw data is freely available from [data.london.gov.uk](data.london.gov.uk) through TFL's website.

`Overview.ipynb` looks at where there is the greatest disparity between bikes being added or removed and the capacity of a bike-point over the course of a single day as a way of looking for where and how much TFL is load-balancing the system. Spoiler, its mostly train stations.

`Waterloo.ipynb` looks at Waterloo Station specifically, treating the 3 bike-points there as one and building a model to predict the number bikes removed on a given day.


