import unittest
import alerts as alerts

# Checkpoint 1
class SystemAlertTests(unittest.TestCase):
    
  # Checkpoint 2
  def test_power_outage_alert(self):
    self.assertRaises(alerts.PowerError, alerts.power_outage_detected, True)
    
  # Checkpoint 3
  def test_water_levels_warning(self):
    self.assertWarns(alerts.WaterLevelWarning, alerts.water_levels_check, 150)

unittest.main()