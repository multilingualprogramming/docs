---
page_id: getting_started__installation
locale: fr
title: Installation
path_segments:
- demarrage
- installation
source_hash: 7febf671956e
status: translated
permalink: /fr/docs/demarrage/installation/
---

## Exigences systeme

| Exigence | Minimum | Recommande |
|-------------|---------|-------------|
| Python | 3.12+ | 3.12.x or 3.13.x |
| RAM | 256 MB | 512 MB (with WASM) |
| Disk | 50 MB | 150 MB (with WASM) |
| OS | Windows, Linux, macOS | Any |

---

## Options d'installation

### Option 1 — Python Only (Minimal)

```bash
pip install multilingualprogramming
```

- Prise en charge complete des 17 langues
- Backend d'execution Python
- Sans acceleration WASM
- Taille d'installation ~50 MB

### Option 2 - Python + WASM (recommande)

```bash
pip install multilingualprogramming[wasm]
```

- Prise en charge complete des 17 langues
- 50–100x speedup on matrix, crypto, scientific operations
- Repli automatique vers Python si WASM indisponible
- Taille d'installation ~150 MB
- Necessite : `wasmtime` (installe automatiquement)

### Option 3 — Maximum Performance

```bash
pip install multilingualprogramming[performance]
```

- Toutes les fonctionnalites WASM
- Replis optimises avec NumPy
- Execution hybride WASM + NumPy
- Taille d'installation ~250 MB

---

## Instructions selon la plateforme

### Linux

```bash
# Verifier Python 3.12+
python3 --version

# Installer
python3 -m pip install multilingualprogramming[wasm]

# Verifier
python3 -c "from multilingualprogramming.runtime.backend_selector import BackendSelector; print('OK')"
```

### macOS

```bash
# Installer Python 3.12 via Homebrew (optional)
brew install python@3.12

# Installer
python3 -m pip install multilingualprogramming[wasm]

# Verifier
python3 -c "import multilingualprogramming; print('OK')"
```

### Windows

```powershell
# PowerShell (execution en utilisateur standard)
python -m pip install multilingualprogramming[wasm]

# Verifier
python -c "import multilingualprogramming; print('OK')"
```

> **Note** : Si `python` est introuvable, essayez `py -3.12` ou verifiez que Python est dans votre PATH.

---

## Environnements virtuels

L'utilisation d'un environnement virtuel est recommandee :

```bash
# Creer un environnement virtuel
python -m venv ml-env

# Activer
source ml-env/bin/activate      # Linux/macOS
ml-env\Scripts\activate         # Windows

# Installer
pip install multilingualprogramming[wasm]

# Desactiver a la fin
deactivate
```

Avec conda :

```bash
conda create -n ml-env python=3.12
conda activate ml-env
pip install multilingualprogramming[wasm]
```

---

## Docker

```dockerfile
FROM python:3.12-slim

WORKDIR /app
RUN pip install multilingualprogramming[wasm]

COPY . .
CMD ["python", "-m", "multilingualprogramming", "repl"]
```

```bash
docker build -t multilingual-app .
docker run -it multilingual-app
```

---

## Compilation depuis la source

Pour le developpement ou la contribution :

```bash
git clone https://github.com/johnsamuelwrites/multilingual.git
cd multilingual

# Installer in development mode with all extras
pip install -e ".[dev,wasm]"

# Executer les tests
python -m pytest -q

# Executer le lint
python -m pylint $(git ls-files '*.py')
```

---

## Verifier l'installation

### Verification rapide

```bash
python -c "import multilingualprogramming; print('OK')"
python -m multilingualprogramming --version
```

### Verification complete

{{snippet:getting_started__installation__py01}}

---

## Dependances

| Package | Version | Objectif |
|---------|---------|---------|
| roman | >=3.3 | Prise en charge des chiffres romains |
| python-dateutil | >=2.8 | Analyse multilingue date/heure |
| wasmtime | >=1.0.0 | Execution WASM (optionnel) |
| numpy | any | Replis numeriques optimises (optionnel) |

---

## Desinstallation

```bash
# Supprimer le package
pip uninstall multilingualprogramming

# Supprimer uniquement le support WASM (conserver le package)
pip uninstall wasmtime
```

---

## Depannage

### `ModuleNotFoundError: No module named 'multilingualprogramming'`

Verifiez que vous avez installe pour la bonne version de Python :

```bash
which python && python --version
pip install multilingualprogramming
```

### WASM not available on macOS ARM64

WASM fonctionne via emulation sur Apple Silicon. Utilisez le repli Python :

{{snippet:getting_started__installation__py02}}

### Windows `ImportError`

Installez les redistribuables Visual C++ de Microsoft, ou :

```bash
pip install --upgrade wasmtime
```

### Python version too old

```
ERROR: Requires Python >= 3.12
```

Mettez Python a jour vers 3.12+ puis reinstallez.
