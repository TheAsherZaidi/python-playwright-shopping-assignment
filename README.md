This project has three browser automation scripts for the Sauce Demo shopping site.

However, for Windows. I am not entirely sure if it works upon testing.

## Scripts

- `01_open_browser.py` opens the login page in a Chromium Window.
- `02_login_one_file.py` checks locked demo account shows the error.
- `03_add_remove_cart.py` adds two products, verifies the cart count is two, removes one product, verifies the count is one, and confirms the remaining product in the cart.

## Requirements

- Python 3
- pip
- Playwright for Python
- Playwright Chromium browser

Install Playwright and its Chromium browser:

Mac: 

```bash
python3 -m pip install playwright
python3 -m playwright install chromium
```

Windows:

```powershell
python -m pip install playwright
python -m playwright install chromium
```

## Run

Mac: 

```bash
python3 01_open_browser.py
python3 02_login_one_file.py
python3 03_add_remove_cart.py
```

Windows: 

```powershell
python 01_open_browser.py
python 02_login_one_file.py
python 03_add_remove_cart.py
```
