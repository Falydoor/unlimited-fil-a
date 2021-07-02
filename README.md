# unlimited-fil-a

This python script reads the cookies from Chrome and then brute-force the "missed transaction" API to get unclaimed points.

# Usage

- Login to https://www.chick-fil-a.com/ with Chrome
- Edit `main.py` and update `DATE`, `ORDER_NUMBER` and `RESTAURANT_NUMBER` with the correct values
- Run `python main.py`
- The script will stop after the quota of API calls is reached (the quota is lifted after 1 month usually)

# Help

- The `RESTAURANT_NUMBER` can be found on https://www.chick-fil-a.com/locations after inspecting the link of the restaurant (ex: https://www.chick-fil-a.com/LocationRedirect/XXXXX).
- `ORDER_NUMBER` can be found on an email receipt.
