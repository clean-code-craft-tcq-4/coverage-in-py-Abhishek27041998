from BreachInfer.Temperature.infer_breach import classify_temperature_breach
from Sender.send_to_controller import send_to_controller
from Sender.send_to_email import send_to_email


def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType = classify_temperature_breach(batteryChar['coolingType'], temperatureInC)

  if alertTarget == 'TO_CONTROLLER':
    send_to_controller(breachType)
  elif alertTarget == 'TO_EMAIL':
    send_to_email(breachType)
