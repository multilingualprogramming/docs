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

## Exigences système

| Exigence | Minimum | Recommandé |
|-------------|---------|-------------|
| Python | 3.12+ | 3.12.x ou 3.13.x |
| RAM | 256 MB | 512 MB (avec WASM) |
| Disque | 50 MB | 150 MB (avec WASM) |
| OS | Windows, Linux, macOS | Tous |

---

## Options d'installation

### Option 1 - Python seul (minimal)

```bash
pip install multilingualprogramming
```

- Prise en charge complète des 17 langues
- Backend d'exécution Python
- Sans accélération WASM
- Taille d'installation ~50 MB

### Option 2 - Python + WASM (recommandé)

```bash
pip install multilingualprogramming[wasm]
```

- Prise en charge complète des 17 langues
- Accélération de 50 à 100x sur les matrices, la crypto et les calculs scientifiques
- Repli automatique vers Python si WASM est indisponible
- Taille d'installation ~150 MB
- Nécessite `wasmtime` (installé automatiquement)

### Option 3 - Performance maximale

```bash
pip install multilingualprogramming[performance]
```

- Toutes les fonctionnalités WASM
- Replis optimisés avec NumPy
- Exécution hybride WASM + NumPy
- Taille d'installation ~250 MB

---

## Instructions selon la plateforme

### Linux

```bash
# Vérifier Python 3.12+
python3 --version

# Installer
python3 -m pip install multilingualprogramming[wasm]

# Vérifier
python3 -c "from multilingualprogramming.runtime.backend_selector import BackendSelector; print('OK')"
```

### macOS

```bash
# Installer Python 3.12 via Homebrew (optionnel)
brew install python@3.12

# Installer
python3 -m pip install multilingualprogramming[wasm]

# Vérifier
python3 -c "import multilingualprogramming; print('OK')"
```

### Windows

```powershell
# PowerShell (exécution en utilisateur standard)
python -m pip install multilingualprogramming[wasm]

# Vérifier
python -c "import multilingualprogramming; print('OK')"
```

> **Note** : Si `python` est introuvable, essayez `py -3.12` ou vérifiez que Python est dans votre `PATH`.

---

## Environnements virtuels

L'utilisation d'un environnement virtuel est recommandée :

```bash
# Créer un environnement virtuel
python -m venv ml-env

# Activer
source ml-env/bin/activate      # Linux/macOS
ml-env\Scripts\activate         # Windows

# Installer
pip install multilingualprogramming[wasm]

# Désactiver à la fin
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

Pour le développement ou la contribution :

```bash
git clone https://github.com/johnsamuelwrites/multilingual.git
cd multilingual

# Installer en mode développement avec tous les extras
pip install -e ".[dev,wasm]"

# Exécuter les tests
python -m pytest -q

# Exécuter le lint
python -m pylint $(git ls-files '*.py')
```

---

## Vérifier l'installation

### Vérification rapide

```bash
python -c "import multilingualprogramming; print('OK')"
python -m multilingualprogramming --version
```

### Vérification complète

{{snippet:getting_started__installation__py01}}

---

## Dépendances

| Package | Version | Objectif |
|---------|---------|---------|
| roman | >=3.3 | Prise en charge des chiffres romains |
| python-dateutil | >=2.8 | Analyse multilingue date / heure |
| wasmtime | >=1.0.0 | Exécution WASM (optionnel) |
| numpy | any | Replis numériques optimisés (optionnel) |

---

## Désinstallation

```bash
# Supprimer le package
pip uninstall multilingualprogramming

# Supprimer uniquement le support WASM (conserver le package)
pip uninstall wasmtime
```

---

## Dépannage

### `ModuleNotFoundError: No module named 'multilingualprogramming'`

Vérifiez que vous avez installé pour la bonne version de Python :

```bash
which python && python --version
pip install multilingualprogramming
```

### WASM not available on macOS ARM64

WASM fonctionne via émulation sur Apple Silicon. Utilisez le repli Python :

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

Mettez Python à jour vers 3.12+ puis réinstallez.
