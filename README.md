# unlimited-fil-a

This python script reads the cookies from Chrome (or from local variables) and then brute-force the "missed transaction" API to get unclaimed points.

# Usage

- Login to https://www.chick-fil-a.com/ with Chrome or set the variables `asp_net_cookie` and `crn_token`
- Edit `main.py` and update `DATE`, `ORDER_NUMBER` and `RESTAURANT_NUMBER` with the correct values
- Run `python main.py`
- The script will stop after the quota of API calls is reached (usually 5 matches)
- The quota is lifted after 1 month
- Your transaction history should look like that after running the script:

![transactions](https://raw.githubusercontent.com/Falydoor/unlimited-fil-a/main/transactions.png)

# Help

- The `RESTAURANT_NUMBER` can be found on https://www.chick-fil-a.com/locations after inspecting the link of the restaurant (ex: https://www.chick-fil-a.com/LocationRedirect/XXXXX).
- `ORDER_NUMBER` can be found on an email receipt.
