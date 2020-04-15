'''
- find min and max to calculate the transaction that yields the biggest profit
- transaction can only be made with price that is before
- start at index 1?
- compare against all indexes before and if profit is higher, swap
'''

list = [1050, 270, 1540, 3800, 2]

def find_max_profit(prices):
  buy = 0
  sell = 0
  profit = 0

  for i in range(len(prices)):
    for j in range(i):
      if prices[i] - prices[j] > profit:
        buy = prices[i]
        sell = prices[j]
        profit = prices[i] - prices[j]

  return(f'Buy at ${buy} and sell at ${sell} for a profit of ${profit}.')

print(find_max_profit(list))

'''
#!/user/bin/python
import argparse

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print('A profit of ${profit} can be made from the stock prices {prices}.'.format(profit=find_max_profit(args.integers), prices=args.integers))
'''