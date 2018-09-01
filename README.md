## Get Started with the code

* Suppose you already have **docker** installed.
```bash
# in the same directory where this README.md resides.
scripts/run_docker.sh
```
in the jupyter ipython notebook page (e.g. ```http://<>:8888```) create a new **Python 3** notebook with ...

- Cell 1 - install dependencies.

```
%%bash
conda install pandas_datareader pytables
```

- Cell 2 - configure matplotlib

```python
%matplotlib inline

import matplotlib
matplotlib.rcParams['figure.figsize'] = (19, 8)
```

- Cell 3 - run it...

```python
from lmk.ticker import Ticker

ticker = Ticker("TSLA")
ticker.retrieve_history("2015-06-01", "2016-04-30")
ticker.visualize("V,C,CL,LMK,WM,PV")
```

and github renders ```ipynb``` files, so here is what the above looks like.
<https://github.com/dyno/LMK/blob/master/lmk.ipynb>

## File Layout

```
.
├── README.md
├── book
│   ├── 1938_1940.py
│   └── 1938_1940.txt
├── lmk
│   ├── __init__.py
│   ├── cache.py
│   ├── calculator
│   │   ├── ATRCalculator.py
│   │   ├── EntryPointCalculator.py
│   │   ├── LMKBandCalculator.py
│   │   ├── ODRCalculator.py
│   │   └── PivotCalculator.py
│   ├── datasource
│   │   ├── DataSource.py
│   │   ├── Google.py
│   │   ├── NetEase.py
│   │   └── Yahoo.py
│   ├── market
│   │   ├── China.py
│   │   ├── Market.py
│   │   └── US.py
│   ├── test
│   │   ├── __init__.py
│   │   ├── test_calculator.py
│   │   ├── test_datasource.py
│   │   ├── test_market.py
│   │   └── test_utils.py
│   ├── ticker.py
│   └── utils.py
├── run.md
├── run_test.sh
└── scripts
    ├── launchd_wrapper.sh
    ├── org.jupyter.server.plist
    └── run_docker.sh
```


### Code Highlight ###

* ```NetEase.py``` - Get China market data with better quality than Yahoo/Google.
* ```PivotCalculator.py``` - An algorithm to calculate local crest/trough.


## TODO List

* multi-tickers in one graph (unlikely...)

* zipline ...

* ~~the cache layer~~ see Market.py/cache.py

* ~~Chinese font (on Mac)~~

```python
# remove font cache
# rm -rf $(python -c "import matplotlib; print(matplotlib.get_cachedir())")

# list all available fonts.
from matplotlib.font_manager import FontManager
m = FontManager()
{f.name:f.fname for f in m.ttflist}

# pick a font.
matplotlib.rcParams['font.family'] = ['sans-serif']
matplotlib.rcParams['font.sans-serif'] = ['STHeiti']
```
