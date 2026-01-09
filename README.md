
# 🧬 Evolution Simulation — Greedy vs Generous

A small, visual Python sandbox that pits two simple strategies against each other as they compete for limited food in a 2D world. The simulation demonstrates emergent population dynamics between **Greedy (Red)** and **Generous (Blue)** agents.

https://private-user-images.githubusercontent.com/148211492/533932452-b68620f1-7ba5-4943-a5a4-543e0bb690ac.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njc5NjkyNDcsIm5iZiI6MTc2Nzk2ODk0NywicGF0aCI6Ii8xNDgyMTE0OTIvNTMzOTMyNDUyLWI2ODYyMGYxLTdiYTUtNDk0My1hNWE0LTU0M2UwYmI2OTBhYy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMTA5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDEwOVQxNDI5MDdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01ZmRiYTVmYTQ4ZDA0NDY3NjJkNWJjNmMxYTQ4ODZhNzM2MWM3NjY3YzEzYTljNDkwN2M2Njc5MDEzYmJkZjhmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.JeM0BrAr_0oCHWUsdBUHpQMhA4jUbTVjFJCe8L5kp_Q
---

## What it models

- Two populations start with 10 agents each: **Red (Greedy)** and **Blue (Generous)**.
- Each day the world spawns a fixed number of food items (`FOOD_AMOUNT`). Agents move to nearest available food and occupy a left or right seat.
- Interaction rules at a food item:
	- Single occupant: eats the food (food_eaten = 1).
	- Two Blues: split food (each gets 0.5).
	- Two Reds: one randomly gets 0.5, the other gets 0.
	- Red + Blue: Red wins (Red gets 1, Blue gets 0).
- Reproduction rules each night:
	- `food_eaten == 1` → produces 2 offspring.
	- `food_eaten == 0.5` → produces 1 offspring.
	- `food_eaten == 0` → no offspring.

These simple rules produce population shifts visible in the runtime and in the plotted graph at exit.

---

## Files

- `main.py` — Entry point and daily loop (spawning, movement, interactions, reproduction, rendering).
- `blob.py` — `Blob` class: movement, targeting, seating and drawing logic.
- `food.py` — `Food` class: seat management and drawing.
- `settings.py` — Constants: `WIDTH`, `HEIGHT`, colors, `FOOD_AMOUNT`, `BLOB_SIZE`, `BLOB_SPEED`, `FOOD_SIZE`, `FPS`.
- `stats.py` — Plots population over days using `matplotlib`.
- `requirement.txt` — Python packages used for plotting and graphics (pygame, matplotlib, numpy, etc.).

---

## Requirements

- Python 3.8+
- Packages listed in `requirement.txt` (pygame, matplotlib, numpy, ...)

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirement.txt
```

---

## Run

Start the simulation with:

```bash
python main.py
```

- Close the Pygame window to generate and display a population graph (via `matplotlib`).
- The console prints day numbers and population counts during the run.

---

## Quick Configuration

- Edit `settings.py` to tune world size, `FOOD_AMOUNT`, `BLOB_SIZE`, and `BLOB_SPEED`.
- To change starting populations, edit the initialization loops in `main.py` (currently 10 red and 10 blue).

---

## Suggested Experiments

1. Decrease `FOOD_AMOUNT` to create scarcity and observe which strategy dominates.
2. Increase `BLOB_SPEED` for one group to test mobility advantages.
3. Modify interaction rules in `main.py` to explore different social dynamics.

---

## Notes for Developers

- To add sensing, decision-making, or mutation mechanics, extend `blob.py` and pass parameters through `settings.py`.
- `stats.py` currently plots with `matplotlib.show()`; replace or augment it to save CSV/PNG for automated experiments.

---

## License

No license specified. Add a `LICENSE` if you want to set reuse terms.

---

Want a translated README, screenshots, or automated experiment scripts? Tell me which and I’ll add them.
# evolution_simulation
