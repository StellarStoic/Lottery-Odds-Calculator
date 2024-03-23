Lottery Odds Calculator
========================

This script calculates the odds of winning various lotteries around the world based on their rules and draws per year. It also provides the cost per ticket and the total cost per year for playing every single draw.

Requirements
------------

* Python 3.x
* math module (included with Python)
* json module (included with Python)

Usage
-----

1. Create a JSON file named `lotteries.json` with the following format:
```json
{
    "lotteries": [
        {
            "name": "Powerball",
            "numbers": 69,
            "picks": 5,
            "extra_numbers": 26,
            "extra_picks": 1,
            "draws_per_year": 156,
            "default_currency": "USD",
            "cost": 2.00
        },
        {
            "name": "Lotto America",
            "numbers": 52,
            "picks": 5,
            "extra_numbers": 10,
            "extra_picks": 1,
            "draws_per_year": 156,
            "default_currency": "USD",
            "cost": 1.00
        },
        {
            "name": "Mega Millions",
            "numbers": 70,
            "picks": 5,
            "extra_numbers": 25,
            "extra_picks": 1,
            "draws_per_year": 104,
            "default_currency": "USD",
            "cost": 2.00
        },
        {
            "name": "EuroMillions",
            "numbers": 50,
            "picks": 5,
            "extra_numbers": 12,
            "extra_picks": 2,
            "draws_per_year": 104,
            "default_currency": "EUR",
            "cost": 2.50
        }
    ]
}
```
The JSON file should contain an array of lottery objects, each with the following properties:

* `name`: The name of the lottery.
* `numbers`: The total number of main numbers to choose from.
* `picks`: The number of main numbers to pick per combination.
* `extra_numbers`: The total number of extra numbers to choose from.
* `extra_picks`: The number of extra numbers to pick per combination.
* `draws_per_year`: The number of draws per year.
* `default_currency`: The default currency for the lottery.
* `cost`: The cost per ticket in the default currency.
1. Run the script using Python 3.x.

Example Output
--------------
```vbnet
The odds of winning the Powerball within a year are 0.0000005339 (or 1 in 1873086.02) and it will cost you 312.00 USD a year per combination if you play every single draw.
The odds of winning the Powerball for a single combination is 0.0000000034 (or 1 in 292201338.00) and it will cost you 2.0 USD

The odds of winning the Lotto America within a year are 0.0000060024 (or 1 in 166600.50) and it will cost you 156.00 USD a year per combination if you play every single draw.
The odds of winning the Lotto America for a single combination is 0.0000000385 (or 1 in 25989600.00) and it will cost you 1.0 USD

The odds of winning the Mega Millions within a year are 0.0000003437 (or 1 in 2909378.89) and it will cost you 208.00 USD a year per combination if you play every single draw.
The odds of winning the Mega Millions for a single combination is 0.0000000033 (or 1 in 302575350.00) and it will cost you 2.0 USD

The odds of winning the EuroMillions within a year are 0.0000007437 (or 1 in 1344598.19) and it will cost you 260.00 EUR a year per combination if you play every single draw.
The odds of winning the EuroMillions for a single combination is 0.0000000072 (or 1 in 139838160.00) and it will cost you 2.5 EUR
```
License
-------

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) file for details.