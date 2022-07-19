"""
Utility function to send to Alert to Controller
"""


def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')
