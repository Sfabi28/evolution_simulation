# 🧬 Evolution Simulation

An interactive, lightweight Python simulation of simple organisms (blobs) that search for food, evolve behaviors, and produce observable statistics over time. Designed for experimentation, teaching, and playful exploration of emergent behavior.

---

## ✨ Highlights

- **Simple & Extensible:** Small codebase so you can quickly understand and modify behaviors.
- **Real-time Simulation:** Run using `main.py` to watch blobs seek food and evolve.
- **Configurable:** Tweak parameters in `settings.py` to change mutation rates, world size, and more.
- **Statistics:** Basic metrics gathered in `stats.py` for observing population trends.

---

## Project Structure

- `main.py` — Simulation entry point and loop.
- `blob.py` — Blob (agent) implementation and behavior logic.
- `food.py` — Food entities and spawning logic.
- `settings.py` — Global simulation parameters to tune.
- `stats.py` — Data collection and basic reporting utilities.
- `requirement.txt` — Dependencies (if any).

---

## Requirements

- Python 3.8+
- (Optional) Create and activate a virtual environment for isolation.

Install dependencies (if using external libs):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirement.txt
```

If `requirement.txt` is empty, the simulation runs with the Python standard library.

---

## Quick Start

Run the simulation with:

```bash
python main.py
```

Controls and runtime information will appear in the console (or in-window prompts if implemented). Tweak parameters in `settings.py` and restart to observe different behaviors.

---

## Configuration Tips

- Open `settings.py` to adjust world size, initial population, food spawn rate, and mutation magnitude.
- Increase mutation rates to explore more diverse evolutionary outcomes.
- Increase initial population for more robust statistics but expect slower performance.

---

## Development Notes

- To add a new sensing or movement behavior, extend `blob.py` and add corresponding parameters to `settings.py`.
- To persist or visualize statistics, update `stats.py` to write CSV or JSON and plot externally.
- Keep simulation steps small when debugging to step through behavior deterministically.

---

## Example Experiments

1. Reduce food spawn rate and increase mutation rate — observe resource-driven adaptation.
2. Increase population and measure average lifespan via `stats.py`.
3. Add new food types (different nutrition values) to `food.py` and watch specialization.

---

## Contributing

Contributions are welcome. Suggested workflow:

1. Fork the repository.
2. Add a feature branch and implement changes.
3. Run the simulation and ensure no regressions.
4. Open a PR with a description of changes and any observable effects.

---

## License

This project is released under an unlisted/unspecified license by default. Add a `LICENSE` file if you want to provide explicit terms.

---

Thanks for exploring this little evolution sandbox! Want me to add screenshots, exportable stats, or a GUI? Open an issue or ask for features.
# evolution_simulation
