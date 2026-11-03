# Point-to-Point Connections

All transistor emitters, the sensor GND and the negative lead of C1 go to the common ground rail.

| Component / pin | Connected to | Purpose |
|---|---|---|
| Sensor VCC | +5 V rail | Powers the sensor |
| Sensor GND | Ground rail | Common ground |
| Sensor SIG | One end of R1 | Moisture signal |
| R1 (other end) | Base of Q1 and R2 | Base current limit |
| R2 (other end) | Ground rail | Pull-down for Q1 |
| Q1 emitter / collector | Ground / timer node | Discharge switch for C1 |
| R4 outer terminal / wiper | +5 V / timer node | Charging resistance |
| C1 positive / negative | Timer node / ground | Timing capacitor |
| Q2 base / emitter | Timer node / ground | Inverter input |
| Q2 collector | R3 and the base of Q3 | Inverter output |
| R3 (other end) | +5 V rail | Pull-up |
| Q3 emitter / collector | Ground / pump negative | Pump switch |
| Pump positive | +5 V rail | Pump supply |
| D1 cathode / anode | +5 V / Q3 collector | Flyback protection |

**Timer node** = Q1 collector + R4 wiper + C1 (+) + Q2 base.

## Assembly order

1. Mount the three BC547s with flat faces in the same direction (pin order: collector, base, emitter).
2. Place C1 with its striped (negative) lead towards ground.
3. Place R1, R2, R3 and R4 per the table above.
4. Connect all emitters and C1 negative to ground.
5. Join the timer node; connect R4's outer terminal to +5 V.
6. Connect Q2 collector to Q3 base and R3; R3 other end to +5 V.
7. Connect the pump between +5 V and Q3 collector; D1 across the pump with the banded cathode towards +5 V.
8. Connect the sensor.
9. Before power-on, check for shorts between +5 V and ground with a multimeter.

## Operating states

| Soil | Sensor | Q1 | Q2 | Q3 | Pump |
|---|---|---|---|---|---|
| Dry | HIGH | ON | OFF | ON | ON |
| Wet, C1 charging (< 0.7 V) | LOW | OFF | OFF | ON | ON (delay period) |
| Wet, C1 charged (~0.7 V) | LOW | OFF | ON | OFF | OFF |

![Flowchart](../images/fig4_flowchart.png)
