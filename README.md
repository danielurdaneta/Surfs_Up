# Surfs_Up

## Overview of the project

The purpose of this project was to determine if the weather conditions on the island of Oahu are suitable for a surf shop, using a SQLite database, Jupyter Notebook, SQLAlchemy, Pandas, we made inquiries and obtained useful information on whether this investment is worth it.

## Results

From the summary statistics of the month of june and december, we can determine the following:

* The average temperature of the two months is slightly different, with an average of 74.94 in June and 71.04 in December
* The standard deviation is higher for the month of December (3.74) than in June (3.25), which indicates that there is a more variable climate in December.
* The minium temperature in December is significantly lower (56) than in June (64).

![summary statistics](https://user-images.githubusercontent.com/81272629/123519365-6c80e580-d670-11eb-827d-ce8ba87063ce.png)

## Summary

As we can see in the previous analysis, there are very similar temperature conditions for the months of June and December, with December having a slightly lower average temperature and a somewhat higher standard deviation, which may suggest that both months are suitable for surf shop

Another queries we could make to get further insights are the following:

```
rain_june = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date)==6).all()
rain_dec = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date)==12).all()

```

Since there is a positive correlation between precipitation and sales, with these queries we can determine which month can be the most successful in sales based on the amount of precipitation that each usually receives.
