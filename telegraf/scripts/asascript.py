from genie.testbed import load
import json
from jsonmerge import merge

tb = load('/opt/telegraf/ASA-Telemetry-Guide/telegraf/scripts/testbed-asa.yaml')
switch_list = tb.devices.keys()
switch_stats = []
for switch in switch_list:
  dev = tb.devices[switch]
  dev.connect(log_stdout=False)
  dev.connect()
  
  
  p1 = dev.parse('show vpn-sessiondb')
  p2 = dev.parse('show resource usage')
  p3 = {'switch_name': switch}
  
  p4 = merge(p1,p2)
  p5 = merge(p3,p4)
  
  switch_stats.append(p5)

print(json.dumps(switch_stats))
