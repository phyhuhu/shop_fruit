import time

def order_fruit(fruit, quantity):
    time.sleep(quantity)   # e.g. 2 apples take 2 secs
    return '%s_%s' % (fruit, quantity)
