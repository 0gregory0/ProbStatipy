# ProbStatipy
---

## Intro
[ProbStatipy](https://pypi.org/project/ProbStatipy/) is a package of Python modules equipped with functions that are used in Statistics.

While the functions are extensively documented, you can check out my Jupyter Notebooks in the [Numerical Summary repo](https://github.com/0gregory0/Numerical-Summary) to fully understand my thought process while coming up with these functions.

---

## Modules
As of now, this package contains three modules in the `src` folder (`src > ProbStatipy`):
1. [central.py](https://github.com/0gregory0/ProbStatipy/blob/main/src/ProbStatipy/central.py): Contains functions to measure central tendency such as Mean, Median and Mode.
2. [spread.py](https://github.com/0gregory0/ProbStatipy/blob/main/src/ProbStatipy/spread.py): Contains functions to measure dispersion/spread such as Variance (Mean Squared Deviation), Standard Deviation and Mean Absolute Deviation (MAD).
3. [probability.py](https://github.com/0gregory0/ProbStatipy/blob/main/src/ProbStatipy/probability.py): Contains a function to compute probability and classes outlining the properties and methods of Sample Spaces and Events.

---

## How to install and use this package
To install the package, run:

```bash
pip install ProbStatipy
```

To upgrade it, run:

```bash
pip install --upgrade ProbStatipy
```

To use the modules in your Python Code, ensure to include the following import statements:

```python
from ProbStatipy import central
from ProbStatipy import spread
from ProbStatipy import probability
```

Now you can access the functions to conduct your statistical analysis:

```python
print(central.mean([3,4,5]))
print(spread.variance([3,4,5]))
print(probability.probability(3, 10))
```
```powershell
>>> 4.0
>>> 0.6666666666666
>>> 0.3
```

You can also import the modules using an alias as observed below:
```python
from ProbStatipy import central as ctr
from ProbStatipy import spread as spr
from ProbStatipy import probability as prb

print(ctr.mean([3,4,5]))
print(spr.variance([3,4,5]))
print(prb.probability(3, 10))
```

```powershell
>>> 4.0
>>> 0.6666666666666
>>> 0.3
```

---

## Functions
Below is a catalogue of functions available in each module
> **`central.py`**
>  > `mean()`
>  > Calculates the population arithmetic mean
>
>  > `median()`
>  > Calculates the median value of the population
>
>  > `mode()`
>  > Calculates the mode


> **`spread.py`**
>  > `variance()`
>  > calculates the population variance
>
>  > `stdeviation()`
>  > computes the population standard deviation
> 
>  > `mad()`
>  > Computes the population mean absolute deviation
> 
>  > `get_range`
>  > gets the range of the dataset
> 
>  > `iqr()`
>  > gets the interquartile range of the dataset

> **`probability.py`**
> >`probability()`
> >Derives the probability of a successful occurrence given the number of occurrences and successful observations.

---

## Classes
> **`probability.py`**
> >`SampleSpace`
> >SampleSpace is a class that represents the sample space of a random experiment.
> >
> >`Event`
> >Event is a Class designed to mimick a subset of a sample space.

---

## Dependencies

| Module | Statistics Topic | Dependencies |
| --- | --- | --- | 
| pystats_central | Central Tendancy | - |     
| pystats_spread | Spread / Dispersion | [math](https://docs.python.org/3/library/math.html) |     

