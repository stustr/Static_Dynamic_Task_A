### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    # the code below only has one =, which does not check for equivalency
    if card.value = 1:
      return True
    # following line is missing a colon at the end
    else
      return False
   
  # dif shoulf be def and the arguments given in the function are not all separated by commas
  dif highest_card(self, card1 card2):
  # indentation of the reaminder of the codeblock should be one tab to the right
  if card1.value > card2.value:
    # card is not a known variable in this function (should be card1)
    return card
  else:
    return card2
  


def cards_total(self, cards):
  # total is not assigned a value, and therefore cannot be used further in the function
  total
  for card in cards:
    total += card.value
    # before assignment total would have to be changed to a string in order to work and the indentation would nedd to be in line with the for loop, in order for the for loop to iterate through all instances in cards.
    return "You have a total of" + total
  
```
