import math
import json

def calculate_odds(numbers, picks, extra_numbers, extra_picks, draws_per_year):
    # Calculate the total number of possible combinations for the main numbers
    main_combinations = math.comb(numbers, picks)

    # Calculate the total number of possible combinations for the extra numbers
    extra_combinations = math.comb(extra_numbers, extra_picks)

    # Calculate the total number of possible combinations overall
    total_combinations = main_combinations * extra_combinations

    # Calculate the odds of winning a single draw
    odds_of_winning = 1 / total_combinations

    # Calculate the odds of winning within a year
    odds_per_year = 1 - math.pow((1 - odds_of_winning), draws_per_year)

    # Calculate the odds of winning for a single ticket
    odds_per_ticket = 1 / total_combinations

    return odds_per_year, odds_per_ticket

# Load the lottery data from a JSON file
with open('lotteries.json') as f:
    lottery_data = json.load(f)

# Calculate the odds for each lottery and print the results
for lottery in lottery_data['lotteries']:
    odds_per_year, odds_per_ticket = calculate_odds(lottery['numbers'], lottery['picks'], lottery['extra_numbers'], lottery['extra_picks'], lottery['draws_per_year'])

    # Get the cost per ticket in the default currency for this lottery
    default_currency = lottery['default_currency']
    cost_per_ticket = lottery['cost']

    # Print the results
    print(f"The odds of winning the {lottery['name']} within a year are {odds_per_year:.10f} (or 1 in {1/odds_per_year:.2f}) and it will cost you {cost_per_ticket * lottery['draws_per_year']:.2f} {default_currency} a year per combination if you play every single draw.")
    print(f"The odds of winning the {lottery['name']} for a single combination is {odds_per_ticket:.10f} (or 1 in {1/odds_per_ticket:.2f}) and it will cost you {cost_per_ticket} {default_currency}")
    # print(f"The cost per ticket for the {lottery['name']} is {cost_per_ticket} {default_currency}.")
    print()  # Print an empty line
