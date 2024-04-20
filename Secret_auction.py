from art import logo
# from clear_function import clear

# used call clear() to clear the output in the console.
print(logo)

def clear_terminal():
    print("\033[H\033[J")

# Call this function whenever you want to clear the terminal
# clear_terminal()


details_list = [] # created a list to store all dictionaries containing bidder details

def auction_details(name, bid):
  details = {}
  details["name"] = name
  details["bid"] = bid #created a dictionary
  details_list.append(details)
  return details_list

def auction_bidder(details_list):
  highest_bid = 0
  winning_bidder = ""
  for item in details_list:
    if item["bid"] > highest_bid:
      highest_bid = item["bid"]
      winning_bidder = item["name"]
  print(f'The winner is {winning_bidder} with a bid of ${highest_bid}')

bidding_finished = False

while( not bidding_finished):
  name = input("What is your name? ")
  bid_amount = int(input("What is your bid? $"))
  should_continue = input("Are there any bidders? ")
  
  list_for_finalising = auction_details(name,bid_amount)
  if should_continue == "yes":
   clear_terminal()
  elif should_continue == "no":
    bidding_finished = True
    auction_bidder(list_for_finalising)


 

  
