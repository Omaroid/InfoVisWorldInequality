# 2019-wid

Extracts of the [World Inequality Database](https://wid.world/).

## Content

* **data/** the data in [tsv](https://bl.ocks.org/mbostock/3305937).
	* **countries.tsv** country codes
	* **income/** income share per country
* **viz/** sample visualisations
* **vendor/** vendorized d3 library

## Data structure

Income data table are given per country.
The attributes present in the tables are:

* **year** the year for the data
* **low** the lower bound of the population quantile (from 0. to 1.)
* **high** the upper bound of the population quantile (from 0. to 1.)
* **width** the width of the quntile (high-low)
* **share** the share of the total income captured by this [low, high] quantile
* **cumul** the cumulative share of the quantiles, i.e. the share of [0., high]

## Sample visualizations

* **histogram.html** a basic histogram showing how to select a specific year, and how to use **low**, **high**, **width** and **share**
* **cdf.html** a cumulative distribution function plot showing a use for **cumul**
* **time.html** a time series visualization
