# PERISTOLE

[![codeastro](https://img.shields.io/badge/Made%20at-Code/Astro-blueviolet.svg)](https://semaphorep.github.io/codeastro/)
![](https://img.shields.io/github/license/centarsirius/peristole)
[![pypi](https://img.shields.io/pypi/v/maglimit)](https://pypi.org/project/peristole/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6744001.svg)](https://doi.org/10.5281/zenodo.6744001)
[![Documentation Status](https://readthedocs.org/projects/maglimit/badge/?version=latest)](https://maglimit.readthedocs.io/en/latest/?badge=latest)

## PERISTOLE : PackagE that geneRates tIme delay plotS due To gravitatiOnaL lEnsing

PERISTOLE plots the time delay caused due to gravitational lensing and other aspects of a pulsar. Current support exists for graphing :
- latitudinal time delay
- rotational time delay
- geomterical time delay
- gravitational time delay

The inspiration for this project came from papers written by Rafikov & Lai, [2005]( https://doi.org/10.1086/429146), [2006](https://doi.org/10.1086/500346) on the double pulsar system J0737-3039. The speciality of this double pulsar system being that the companion pulsar has an almost edge-on configuration with respect to our line of sight which
> ***presents an unprecedented natural laboratory for testing our understanding of general relativity and pulsar magnetosphere physics***

## Installation

### Using `pip`
The package is installable on Python 3.x. To install the package,

```python
pip install peristole
```

### Using `GitHub`
Otherwise, clone this repo, and follow the below specified commands

```python
git clone 'https://github.com/centarsirius/peristole'
cd peristole
pip install -e .
```

 ## Demos
 Demos to graph all time delays are inbuilt. Calling the function name without any inputs will plot a graph for default values given in Rafikov & Lai, [2006](https://doi.org/10.1086/500346).


 ## Future Goals:
 - We currently have a constrained use case but we hope to expand the input pool and also use the query system to fetch pulsar properties to provide a smooth user experience. 