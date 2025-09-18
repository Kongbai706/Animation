# Animated Rainfall Chart Project

This project visualizes monthly average rainfall as colored dots on a map using matplotlib. The animation scrolls through the last 100 years of data evenly over time.

## Features
- Animated chart with matplotlib
- Monthly average rainfall as colored dots
- Map visualization
- Animation covers last 100 years

## Requirements
- Python 3.8+
- matplotlib
- pandas
- numpy
- (Optional) cartopy or basemap for advanced map plotting

## Setup
1. Create a virtual environment:
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Install dependencies:
   ```powershell
   pip install matplotlib pandas numpy
   # pip install cartopy  # Uncomment if using cartopy
   ```

## Usage
Run the main script:
```powershell
python main.py
```

## Notes
- Replace placeholder data loading code with your actual rainfall dataset.
- For map plotting, install and import cartopy or basemap as needed.
