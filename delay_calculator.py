#!/usr/bin/env python3
"""Pump-ON delay calculator for the microcontroller-free plant watering system.

Q2 turns ON when the voltage across C1 reaches about 0.7 V, so

    t = -R * C * ln(1 - Vbe / Vcc)  ~=  0.151 * R * C   (Vbe = 0.7 V, Vcc = 5 V)

R is the resistance of R4 in the circuit, C is C1. This is the theoretical
value; the real delay is longer (capacitor tolerance, transistor turn-on).

Usage:
    python delay_calculator.py --r 100 --c 680     # R in kohm, C in uF
    python delay_calculator.py --table             # reproduce Table 6 of the report
"""
import argparse
import math


def delay_seconds(r_kohm: float, c_uf: float, vcc: float = 5.0, vbe: float = 0.7) -> float:
    """Return the pump-ON delay in seconds."""
    if r_kohm <= 0 or c_uf <= 0:
        raise ValueError("R and C must be positive")
    if not 0 < vbe < vcc:
        raise ValueError("Need 0 < Vbe < Vcc")
    r_ohm = r_kohm * 1e3
    c_f = c_uf * 1e-6
    return -r_ohm * c_f * math.log(1 - vbe / vcc)


def print_table() -> None:
    caps = (470, 680, 1000)
    rs = (100, 75, 50, 25, 10)
    print("R4 (kohm) | " + " | ".join(f"C1={c} uF" for c in caps))
    for r in rs:
        print(f"{r:>9} | " + " | ".join(f"{delay_seconds(r, c):>9.1f} s" for c in caps))


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--r", type=float, help="R4 in the circuit, in kohm")
    p.add_argument("--c", type=float, help="C1, in uF")
    p.add_argument("--vcc", type=float, default=5.0, help="supply voltage (default 5)")
    p.add_argument("--table", action="store_true", help="print the delay table")
    args = p.parse_args()

    if args.table:
        print_table()
    elif args.r is not None and args.c is not None:
        t = delay_seconds(args.r, args.c, vcc=args.vcc)
        print(f"R4 = {args.r} kohm, C1 = {args.c} uF -> theoretical delay = {t:.1f} s")
        print(f"Time constant RC = {args.r * args.c / 1000:.1f} s")
    else:
        p.error("give --r and --c, or use --table")


if __name__ == "__main__":
    main()
