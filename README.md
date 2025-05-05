# FFXIV Gil Flip Finder 🪙

A CLI tool that helps identify the most profitable items to flip in Final Fantasy XIV using market data from [Saddlebag Exchange](https://saddlebagexchange.com).

## Features

- 🔎 Scans the market for profitable item flips
- 📈 Sorts and scores items based on ROI, profit margin, and sale rate
- 🛠️ Configurable filters and thresholds via command-line arguments or `config.json`
- 🕒 Can be scheduled to run automatically (via Task Scheduler or cron)
- 🐧 Works in WSL/Linux environments

## Requirements

- Python 3.8+
- `requests`, `tabulate` libraries (install via `pip install -r requirements.txt`)
- WSL (if running on Windows)

## Usage

### Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ff14-gil-finder.git
cd ff14-gil-finder
```

2. Install dependencies:

```python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Configure default values in src/gilflip/config.json. (Optional)

4. Run below command to run script with default values

```
python3 src/gilflip/main.py
```

### Example Output

```
Name                                          ROI%    Profit    Profit%    Home Server Price    Buy Price    Sale rate    Item Score  Selling Server
------------------------------------------  ------  --------  ---------  -------------------  -----------  -----------  ------------  -------------------
Modern Aesthetics - Ambitious Ends              80    727525        415               950000       174975       0.0493      104.752   Chaos - Cerberus
```

### CLI Options

```
Flag    Description
--roi	        Minimum preferred ROI %
--mprof	        Minimum profit amount in gil
--mappu	        Minimum average price per unit
-s	            Minimum item stack size
-t	            Sales time period in hours
--min-sales	    Minimum sales in that period
--hq	        Filter HQ items only
--home	        Set your home server
-d	            Include region-wide listings
-v	            Include vendor-sold items
--out-of-stock	Include items currently out of stock
```

### Automation


You can automate this script using:

Windows Task Scheduler (using a .bat file that invokes WSL and activates the virtual environment)

cron if running directly in Ubuntu/WSL

### Acknowledgments

Saddlebag Exchange API for market data

Universalis for historical insights