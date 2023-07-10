# sort-names route
Post /sort-names
  names: [string]


Tests:
"""
#Post /sort-names
# Parameters:
#   Names: 'Liam', 'Gary', 'Alan', 'Mary'
#   Expected response (200 OK)

'Alan, Gary, Liam, Mary'
"""
