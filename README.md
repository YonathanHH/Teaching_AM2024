# Teaching_AM2024 — Geothermal Reservoir Grid Modelling

> **Teaching support material** developed as part of my role as a **Teaching Assistant** at **Reykjavik University (2024)**, for the Applied Modelling / geothermal reservoir simulation course. These scripts walk students through building and refining a numerical grid for use with the [TOUGH2](https://tough.lbl.gov/) reservoir simulator via the [PyTOUGH](https://github.com/acroucher/PyTOUGH) Python library.

---

## Context

[TOUGH2](https://tough.lbl.gov/) is an industry-standard multiphase flow simulator widely used in geothermal reservoir modelling. [PyTOUGH](https://github.com/acroucher/PyTOUGH) provides a Python interface to build, manipulate, and post-process TOUGH2 models. This repository demonstrates the step-by-step construction of a rectangular 3-D geothermal grid, local refinement, mesh optimisation, and topographic surface fitting — all core skills for geothermal reservoir engineers.

---

## Scripts — Workflow Overview

Run the scripts **in order**. Each script reads the output geometry file from the previous step.

| Step | Script | What it does |
|------|--------|--------------|
| 1 | `01generate_grid.py` | Creates a rectangular 3-D grid (10×10×10 blocks, 2 km × 2 km × 1 km each) using `mulgrid.rectangular()` and writes `Geometry.dat` |
| 2 | `02RefineGrid.py` | Reads `pols.dat` to identify target columns and locally refines the grid inside a polygon, writing `Geometry_02.dat` |
| 3 | `03optimize_by_polygon.py` | Optimises node positions within the refined polygon for better mesh quality (smooth transitions), writing `Geometry_02b.dat` |
| 4 | `04Topo_on_Grid.py` | Fits a topographic surface from `Mountain.dat` (XYZ point cloud) onto the top of the grid using `geo.fit_surface()`, writing `Geometry_03.dat` |

---

## Requirements

```bash
pip install PyTOUGH numpy
```

> PyTOUGH also requires a working TOUGH2 installation for full simulation runs, but the grid-building scripts above run with PyTOUGH alone.

---

## Input Files

| File | Description |
|------|-------------|
| `pols.dat` | Comma-separated XY polygon coordinates that define the refinement/optimisation zone |
| `Mountain.dat` | XYZ topographic point cloud data for surface fitting *(not included — replace with your own DEM export)* |

---

## Output Files (generated)

| File | Description |
|------|-------------|
| `Geometry.dat` | Initial rectangular grid |
| `Geometry_02.dat` | Locally refined grid |
| `Geometry_02b.dat` | Optimised (smoothed) refined grid |
| `Geometry_03.dat` | Final grid with topographic surface fitted |

---

## Skills Demonstrated

- Geothermal reservoir grid construction with PyTOUGH / TOUGH2
- Local mesh refinement and node optimisation for numerical stability
- Topographic surface fitting onto a 3-D numerical model
- Teaching Assistant experience: designing step-by-step modelling workflows for students

---

## About

**Yonathan Hary** — MSc Sustainable Energy Science, Reykjavik University  
Teaching Assistant, Geothermal Conceptual & Numerical Modelling (2024)  
[GitHub](https://github.com/YonathanHH) · [Portfolio](https://yonathanhh.github.io/)
