# Analýza EKG signálu

Krátký přehled projektu pro cvičení 6.

## Co skript dělá

- načte data z `ekg_signal.txt`,
- spočítá min, max a průměr,
- vykreslí signál přes `matplotlib`.

## Spuštění

```powershell
uv run python .\use_signal_plot_ops.py
```

## Malý výpočet

\[
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\]

![Malý náhled grafu](../assets/cviceni_06/maly_nahled.svg)

Více informací je v [přehledu cvičení](./README.md).
