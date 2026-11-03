# Automatic Plant Watering System Without Microcontroller

An automatic plant watering system built only from basic analog components: a soil moisture sensor, three BC547 NPN transistors, an RC timer and a small 5 V DC pump. **No Arduino, no microcontroller, no code.**

Project report for **U25EC304 & Analog Electronics Laboratory**, Department of Electronics and Communication Engineering, KPR Institute of Engineering and Technology (Autonomous), Coimbatore. Academic year 2026–2027 (Odd Semester), II Year.

## Team

| Name | Register No. |
|---|---|
| LOKITH G | 25EC115 |
| MADHAN RAJA| 25EC116 |
| Malini K | 25EC121 |
| Haresh S | 25EC066 |

## How it works

![Block diagram](images/fig1_block_diagram.png)

1. **Soil dry** → sensor output HIGH → Q1 ON and discharges C1 → Q2 OFF → Q3 ON → **pump runs**.
2. **Soil wet** → sensor output LOW → Q1 OFF → C1 charges through R4 (pump keeps running during this delay).
3. When C1 reaches about 0.7 V → Q2 ON → Q3 OFF → **pump stops**.
4. D1 (1N4007) across the pump absorbs the motor's inductive spike.

Delay: `t ≈ 0.151 × R4 × C1` (about 10 s for 100 kΩ and 680 µF, in theory; longer in practice).

![Circuit diagram](images/fig3_circuit_diagram.png)

## Components

| Ref | Part | Value |
|---|---|---|
| P1 | Resistive soil moisture sensor module | 3-pin (VCC, GND, SIG) |
| Q1, Q2, Q3 | NPN transistor | BC547 |
| R1 | Resistor | 500 Ω (470 Ω / 510 Ω also fine) |
| R2 | Resistor | 10 kΩ |
| R3 | Resistor | 1 kΩ |
| R4 | Potentiometer | 100 kΩ linear |
| C1 | Electrolytic capacitor | 680 µF, ≥ 10 V |
| D1 | Diode | 1N4007 |
| M1 | Mini submersible pump | DC 3–6 V |
| — | Supply | 5 V DC, at least 500 mA |

Full list: [`docs/bill_of_materials.csv`](docs/bill_of_materials.csv). Approximate cost: ₹270 – ₹450.

## Repository layout

```
.
├── README.md
├── LICENSE
├── .gitignore
├── report/Project_Report.pdf        Full project report
├── images/                          Figures from the report
├── docs/
│   ├── connections.md               Point-to-point wiring table
│   ├── design_calculations.md       Design maths and voltage table
│   ├── testing_and_troubleshooting.md
│   └── bill_of_materials.csv
└── tools/delay_calculator.py        Pump-ON delay calculator
```

## Quick start

1. Assemble the circuit on a breadboard using [`docs/connections.md`](docs/connections.md).
2. Check there is no short between +5 V and ground before powering on.
3. Set the sensor's trimmer so the output is LOW in just-watered soil and HIGH when the soil needs water.
4. Start with R4 at its middle position, then adjust (see [`docs/testing_and_troubleshooting.md`](docs/testing_and_troubleshooting.md)).

Estimate the delay for your own R4 and C1:

```bash
python tools/delay_calculator.py --r 100 --c 680
python tools/delay_calculator.py --table
```

## Precautions

- Never run the pump dry; keep the pump fully under water and seal its wire joints.
- Check polarity of C1 and D1 before power-on.
- Do not turn R4 to 0 Ω (add about 1 kΩ in series for protection).
- Use 5 V only.
- Resistive probes corrode over time; clean them or use a capacitive sensor.
- BC547 is rated 100 mA. For pumps drawing more, replace Q3 with a BC337 or 2N2222 and reduce R3 to about 470 Ω.
- Not suitable for cacti or other plants that must stay dry.

## Limitations and future scope

No empty-tank detection, no display or alerts, and the delay depends on component tolerance. Possible upgrades: capacitive sensor, water-level sensor with LED/buzzer, Schmitt-trigger comparator, relay or MOSFET for larger pumps, solar power, soldered PCB, optional microcontroller/IoT add-on.

## Reference

R. Krisna, "A Simple Automatic Plant Watering System without Microcontroller," CircuitDigest, May 2024. https://circuitdigest.com/electronic-circuits/automatic-plant-watering-system-without-arduino

## License

Released under the MIT License (see [`LICENSE`](LICENSE)).
