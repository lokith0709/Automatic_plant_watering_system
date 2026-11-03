# Calibration, Testing and Troubleshooting

## Calibration

**Dryness threshold:** with the probes in the soil of a just-watered plant, turn the trimmer on the sensor module until the output is LOW (wet). Let the soil dry and confirm the output turns HIGH when the plant needs water.

**Pump time:**

1. Set R4 to its middle position.
2. Let the soil dry until the pump starts, then observe how long it runs after the soil becomes wet.
3. After 2–4 hours check the soil. Too wet → lower R4. Still dry deep in the pot → raise R4.
4. If R4's range is not enough, change C1 (smaller = shorter, larger = longer).

| Plant type | Water need | Suggested setting |
|---|---|---|
| Succulents, low-water plants | Low | Low R4, or smaller C1 |
| Pothos, spider plant | Moderate | Middle of R4 |
| Ferns, peace lily | High | High R4, or larger C1 |
| Cactus, desert plants | Must stay dry | Not suitable |

## Stage-wise test procedure

| Step | Test | Expected result |
|---|---|---|
| 1 | Continuity check, look for +5 V to ground shorts before power-on | No short |
| 2 | Apply 5 V, measure at sensor, potentiometer and pump | 5 V at all points |
| 3 | Probes in dry air | Output HIGH, Q1 ON, pump runs |
| 4 | Dip probes in water | Output LOW; pump continues for the delay, then stops |
| 5 | Remove and dry probes | Output HIGH; pump starts immediately |
| 6 | Vary R4 and repeat step 4 | Delay changes with R4 |
| 7 | Probes in plant soil, full system | Pump starts when dry, stops after delay when wet |

## Troubleshooting

| Problem | Possible cause | Solution |
|---|---|---|
| Pump runs continuously | Sensor output inverted, Q2 faulty, or no common ground | Check sensor polarity, test Q2, check grounds |
| Pump never starts | No supply, wrong transistor orientation, faulty Q3 | Check 5 V at all points, transistor pins and diode direction |
| Watering time too short | C1 too small or R4 low | Increase C1 or raise R4 |
| Watering time too long | C1 too large or R4 at maximum | Reduce C1 or lower R4 |
| Sensor not detecting moisture | Corroded probes or poor soil contact | Clean probes and insert properly |
| Weak water flow | Low pump voltage or kinked tube | Check 5 V at pump, straighten tube |
| Sensor or pump restarts when pump starts | Supply voltage dips | Stronger supply, 100 nF across the supply |

## Setup photos

![TinkerCAD breadboard layout](../images/fig7_tinkercad_breadboard.png)
*TinkerCAD note: the simulator's sensor model gives the inverse output of the real module, so pump behaviour appears reversed in simulation.*

![Final setup](../images/fig8_final_setup.png)
