# Infer breach for temperature
from ConfigReader.read_config import parse_config


def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'


def classify_temperature_breach(coolingType, temperatureInC):
  config = parse_config('BreachInfer/breach_values.yml')

  temperature_breaches = config['Temperature']

  lowerLimit = 0
  upperLimit = 0

  for ct in temperature_breaches.keys():
      if coolingType == ct:
          lowerLimit = temperature_breaches[ct]['lower_limit']
          upperLimit = temperature_breaches[ct]['upper_limit']
          break

  return infer_breach(temperatureInC, lowerLimit, upperLimit)
