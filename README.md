# Prettify JSON

The code used for interpret json formated text into readable form. In this project uses two modules:
1. json (allows to encode and decode data in a convenient format)
2. sys  (provides access to some variables and functions that interact with the python interpreter)

# Quickstart

The programm takes a path to file with json formated text as an argument and  displays in comsole into readble form.

## Input

```python
{'4': 5, '6': 7}
```

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>

```
## Output

```python
{
    "4": 5,
    "6": 7
}
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
