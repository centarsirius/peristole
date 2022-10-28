# PERISTOLE

[![codeastro](https://img.shields.io/badge/Made%20at-Code/Astro-blueviolet.svg)](https://semaphorep.github.io/codeastro/)
![](https://img.shields.io/github/license/centarsirius/peristole)
[![pypi](https://img.shields.io/pypi/v/peristole)](https://pypi.org/project/peristole/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6744000.svg)](https://doi.org/10.5281/zenodo.6744000)
[![Documentation Status](https://readthedocs.org/projects/peristole/badge/?version=latest)](https://peristole.readthedocs.io/en/latest/?badge=latest)

PackagE that geneRates tIme delay plotS caused by graviTatiOnaL lEnsing

``PERISTOLE`` plots the time delay caused by gravitational lensing and other aspects of a pulsar systems. Current support exists for graphing :

- amplification factor
- latitudinal lensing delay
- rotational lensing delay
- geomterical delay
- gravitational (Shapiro) delay
- combined geometrical and gravitational time delay

The inspiration for this project comes from papers written by Rafikov & Lai, [2005]( https://doi.org/10.1086/429146), [2006](https://doi.org/10.1086/500346) on the double pulsar system J0737-3039. The speciality being that the companion pulsar has an almost edge-on configuration with respect to our line of sight which
> ***presents an unprecedented natural laboratory for testing our understanding of general relativity and pulsar magnetosphere physics***

## Installation

### Using `pip`
The package is installable on Python 3.x. To install the package,

```python
pip install peristole
```
or

```python
pip install git+https://github.com/centarsirius/peristole
```

### Using `GitHub`
Otherwise, clone this repo, and follow the below specified commands

```python
git clone 'https://github.com/centarsirius/peristole'
cd peristole
pip install -e .
```

 ## Demos
 Demos to graph all time delays are inbuilt and will plot a graph for default values given in Rafikov & Lai, [2006](https://doi.org/10.1086/500346). Please take a look at the docs for information on how to access demos.


 ## Future Goals:
 - We currently have a constrained use case but we hope to expand the input pool and also use the query system to fetch pulsar properties to provide a smooth user experience.
