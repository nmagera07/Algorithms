#!/usr/bin/python

import argparse

def find_max_profit(prices):
  profits = []

  for i in prices:
      price_index = prices.index(i)
        
      for j in range(price_index + 1, len(prices)):
        
          price_difference = prices[j] - prices[price_index]

          profits.append(price_difference)
  return max(profits)


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))