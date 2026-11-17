# Solar Wind Interaction & Space Exploration Simulation Suite

Lately, I have become deeply enthusiastic about solar wind physics and space weather. Alongside a few fellow undergraduate students, I am currently developing two coursework projects centered around this field of study. While the initial phases of our work were not primarily focused on heavy computational fluid or plasma simulation, our long-term goal has always been to expand these projects and progressively refine the physical and numerical models we use.

Because all three projects revolve around interactions with the Solar Wind, this repository brings them together under a unified framework. In the `Equations/` section, I outline the general governing equations, the specific analytical/numerical models currently implemented, and the advanced formulations planned for future iterations. Additionally, the repository is organized into three dedicated project folders, each containing a more detailed technical breakdown, implementation notes, and current simulation progress.

---

## 📂 Repository Structure

```text 
SW-test-case/
├── .gitignore              # Git exclusion rules
├── .python-version         # Python version specification
├── pyproject.toml  uv.lock # Python environment (managed via uv)
├── README.md               # General overview and repository summary
├── Equations/              # Theoretical framework and mathematical models
│   ├── main.tex              # LaTeX source file
│   └── main.pdf              # Compiled PDF
├── EM_Shield/              # Active Electromagnetic Shielding System study
│   ├── Main.ipynb            # Main Jupyter notebook for shield analysis
│   ├── data_YBCO.xlsx        # Experimental dataset for YBCO HTS
│   └── about_data.txt        # Metadata of the YBCO dataset
└── Comet_Tail/             # Comet tail study
    ├── Main.ipynb            # Main notebook for comet analysis
    ├── Cases/                # Test cases and results
    └── PLUTO-comet/        # Numerical MHD integrations for comet
``` 

---

## 🛰️ Project Summaries

### 1. Active Electromagnetic Shielding System (`EM_Shield/`)

* **Focus:** Designing a magnetic coil architecture capable of deflecting charged solar wind particles to protect spacecraft or habitats.

* **Methodology & Current Progress:** We selected a "pumpkin-like" coil geometry tailored to our mission sizing constraints. Driven by system requirements—maximum allowable array dimensions, ambient solar wind magnetic field strength, and the maximum permissible magnetic field inside the protected zone—we applied the Biot–Savart Law to size the coils and estimate the required current density assuming YBCO HTS (High-Temperature Superconductor) tapes. We also evaluated the induced electric field characteristics.

* **Validation:** To validate particle deflection efficiently, we exploited the quadrupole symmetry of the pumpkin configuration, simulating only one-quarter of the cross-section. Using the Lorentz force equations, we propagated test particles initialized with free-stream parallel velocities derived from solar wind conditions and verified that their trajectories do not penetrate the protected inner volume.

### 2. Comet Detection via Coronagraphs & Space Weather (`Comet_Tail/`)

* **Focus:** Multi-spacecraft detection, 3D localization of sungrazing comets, and their future use as natural space weather probes.

* **Methodology & Current Progress:** This is the project to which I have dedicated the most effort, and it forms the core proposal for my upcoming undergraduate thesis. The primary pipeline ingests solar coronagraph imagery from multiple vantage points (different space probes) and applies image processing and object detection algorithms to identify comets—predominantly sungrazers. By correlating detections across multiple viewpoints, we aim to perform 3D triangulation to reconstruct their trajectories in the inner heliosphere.

* **Future Vision & Simulation Demo:** While detection and 3D localization are the immediate milestones, comets act as natural probes for studying space weather and solar wind structure (e.g., observing ion tail disconnection events and magnetic reconnection driven by solar wind transients). Because we are currently focused on the computer vision and detection phase, I do not yet have full-scale research simulations of my own for this module; however, I have included a simple, AI-assisted test case implemented in PLUTO to illustrate a basic MHD cometary tail interaction, which is explored in greater detail inside the project folder.

---

## 🚀 Getting Started

Each project folder contains its own standalone `test_case.py` (or simulation setup) with specific instructions, input parameters, and expected verification outputs.

```bash
# Clone the repository
git clone https://github.com/S4GC/SW-test-case.git
cd SW-test-case

# Sync Python dependencies using uv
uv sync
```