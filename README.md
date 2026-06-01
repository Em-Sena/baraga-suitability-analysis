# baraga-suitability-analysis
ArcPy-automated routing model for a Pumped Underground Storage Hydro (PUSH) facility at the Ohio Mine (Baraga, MI). Uses ArcGIS Pro Least-Cost Path (LCP) analysis to balance 300ft watershed buffers, steep slopes, and infrastructure colocation.
# PUSH-Siting-Baraga: Transmission Routing for Pumped Underground Storage Hydro (PUSH)

[![GIS-ArcGIS Pro](https://img.shields.io/badge/GIS-ArcGIS%20Pro-blueviolet?style=flat-squared&logo=arcgis)](https://www.esri.com/)
[![Language-Python](https://img.shields.io/badge/Language-Python%203.x-blue?style=flat-squared&logo=python)](https://www.python.org/)
[![Sponsor-Alfred_P._Sloan_Foundation](https://img.shields.io/badge/Sponsor-Alfred%20P.%20Sloan%20Foundation-lightgrey?style=flat-squared)](https://sloan.org/)

An automated Multi-Criteria Decision Analysis (MCDA) and Least-Cost Path (LCP) workflow built in ArcGIS Pro to optimize transmission line alignment. Developed as part of the Alfred P. Sloan Foundation-funded **Rural Electrification & Climate Resilience Project**, this tool identifies the lowest-impact route to connect a proposed Pumped Underground Storage Hydro (PUSH) facility at the legacy **Ohio Mine (Baraga County, MI)** to the regional grid.

📊 **View the Interactive Project Case Study:** [ArcGIS StoryMap](https://arcg.is/15T1P81)

---

## 📌 Project Overview

Repurposing decommissioned mining assets ("brownfields") for green energy storage is a critical pillar of the clean energy transition. However, connecting these remote sites to the existing electrical grid presents severe environmental, regulatory, and engineering hurdles. 

This project models an optimal 115kV transmission corridor by mathematically weighing environmental constraints against engineering viability, ensuring compliance with strict watershed protections and local land preservation laws.

---

## 🛠️ Technical Workflow & Constraints

The routing model transforms vector constraints into a continuous cost surface, determining the optimal route via ArcPy-automated pathfinding.

| Constraint / Variable | Data Type | Model Weight | Logic / Regulatory Rule |
| :--- | :--- | :--- | :--- |
| **Hydrologic Buffers** | Vector (Polygon) | *Exclusionary* | Strict 300ft setback from water bodies to protect local watersheds. |
| **L'Anse Preservation** | Vector (Polygon) | High Cost (8/10) | Avoids protected ecosystems and conservation parcels. |
| **Terrain Topography (DEM)** | Raster | Moderate Cost | Slopes $>15\%$ dynamically scale up in cost due to erosion and construction limits. |
| **Access Roads** | Vector (Line) | Negative Cost (1/10) | Encourages infrastructure colocation along primary/secondary roads to lower costs. |

### Process Pipeline:
1. **Vector-to-Raster Conversion:** Standardizes multi-source data inputs.
2. **Reclassification:** Normalizes features to a unified scale ($1 = \text{Optimal}$, $10 = \text{Restricted}$).
3. **Distance Accumulation:** Computes a continuous cell-by-cell effort map outward from the Imperial Mine hub.
4. **Optimal Path Allocation:** Traces the mathematically cheapest polyline route to the target grid substation.

---

## 📂 Repository Structure

```text
├── data/
│   └── sample_boundaries/       # Shapefiles/Metadata samples for Baraga County
├── scripts/
│   ├── arcpy_routing_pipeline.py # Main ArcPy script for MCDA & LCP automation
│   └── config.json              # Adjustable layer weights and parameter values
├── layouts/
│   └── map_outputs/             # High-fidelity PDF exports of the final corridor
├── README.md
└── requirements.txt
