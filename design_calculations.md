# Design Calculations

## 1. Transistor as a switch

`IB(min) = IC / hFE`, and for guaranteed saturation `IB(design) ≈ IC / 10`.

## 2. Base drive of Q1 (R1, R2)

- Current through R1: (5 − 0.7) / 500 Ω = 8.6 mA
- Current through R2: 0.7 V / 10 kΩ = 0.07 mA
- `IB(Q1) ≈ 8.6 − 0.07 ≈ 8.5 mA`
- Q1's collector current is at most (5 − 0.2) V / 100 kΩ ≈ 48 µA, so only about 5 µA of base current is needed for hard saturation. Q1 is heavily over-driven.

## 3. Minimum resistance of R4

At 1 kΩ the current into Q1's collector is about 4.8 mA (safe). At 0 Ω nothing limits it, so never set R4 to zero, or put about 1 kΩ in series with it.

## 4. RC timer delay

Capacitor charging: `Vc(t) = VCC (1 − e^(−t/RC))`

Q2 turns ON at VBE ≈ 0.7 V with VCC = 5 V:

`t = −RC · ln(1 − 0.7/5) ≈ 0.151 × R × C`

| R4 | C1 = 470 µF | C1 = 680 µF | C1 = 1000 µF |
|---|---|---|---|
| 100 kΩ | 7.1 s | 10.3 s | 15.1 s |
| 75 kΩ | 5.3 s | 7.7 s | 11.3 s |
| 50 kΩ | 3.5 s | 5.1 s | 7.5 s |
| 25 kΩ | 1.8 s | 2.6 s | 3.8 s |
| 10 kΩ | 0.7 s | 1.0 s | 1.5 s |

These are theoretical. Real delay is longer: electrolytics have about ±20 % tolerance, the transistor does not switch sharply at 0.7 V, and Q3 turns OFF only once Q2 is well into conduction. Measure on the real circuit.

![Charging curves](../images/fig6_c1_charging_curves.png)
![Delay vs R4](../images/fig9_delay_vs_r4.png)

## 5. Q2 and Q3

- Q2 ON: current through R3 ≈ (5 − 0.2) / 1 kΩ = 4.8 mA, so base current ≥ 4.8 mA / 110 ≈ 44 µA.
- Available from the timer at R4 = 100 kΩ: (5 − 0.7) / 100 kΩ = 43 µA. This is marginal for low-gain parts and fine for BC547B/C. Avoid the extreme maximum of R4 with low-gain transistors.
- Q2 OFF: R3 feeds Q3's base with (5 − 0.7) / 1 kΩ = 4.3 mA.

| Pump current | Forced gain needed (IC/IB) | Remark |
|---|---|---|
| 50 mA | 12 | Suitable |
| 100 mA | 23 | Suitable, at the BC547 limit |
| 200 mA | 47 | Exceeds 100 mA rating, use stronger transistor |
| 400 mA | 93 | Exceeds rating, use stronger transistor |

For pumps above 100 mA use a BC337 or 2N2222 (about 800 mA) and reduce R3 to about 470 Ω.

Dissipation in Q3 at 100 mA and VCE(sat) = 0.25 V: 25 mW, far below 500 mW.

## 6. Flyback diode

When Q3 interrupts the motor current, `v = L di/dt` produces a spike. D1 clamps the collector to about VCC + 0.7 V ≈ 5.7 V, well under the 45 V rating of the BC547.

## 7. Power

- Pump voltage ≈ 5 − 0.2 = 4.8 V; at 100 mA the pump takes about 0.5 W while running.
- Standby current about 10–25 mA (sensor module plus R3 path). At 20 mA average, a 10,000 mAh power bank runs the electronics for roughly 500 hours (about 20 days). These are estimates to confirm with a multimeter.

## 8. Expected node voltages

| Node | Soil dry (pump ON) | Wet, delay running (pump ON) | Wet, delay over (pump OFF) |
|---|---|---|---|
| Sensor SIG | ~5 V | ~0 V | ~0 V |
| Base of Q1 | ~0.7 V | ~0 V | ~0 V |
| Timer node (C1) | 0.1–0.2 V | rising 0.2 → 0.7 V | ~0.7 V |
| Collector Q2 / base Q3 | ~0.7 V | ~0.7 V | 0.1–0.2 V |
| Collector of Q3 | 0.1–0.25 V | 0.1–0.25 V | ~5 V |
| Across the pump | ~4.8 V | ~4.8 V | 0 V |

## Design considerations

- Add a 100 nF ceramic capacitor across the supply and use short, thick supply wires to reduce pump start-up noise.
- There is no built-in hysteresis; the dryness threshold is set by the sensor trimmer and the RC delay prevents rapid switching.
- The delay is a fixed time, so the water delivered also depends on the pump flow rate.
- All emitters, the sensor and the supply must share one ground.
