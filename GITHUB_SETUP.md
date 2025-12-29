# GitHub Repository Setup Guide

Complete guide for setting up your GitHub repository for django-context-memory.

---

## 1. Create GitHub Repository

### Option A: Via GitHub Website

1. Go to https://github.com/new
2. Repository name: `django-context-memory`
3. Description: "Deep code intelligence for AI assistants working with Django projects"
4. Make it **Public** (required for PyPI)
5. **DO NOT** initialize with README (we already have one)
6. Click "Create repository"

### Option B: Via GitHub CLI

```bash
gh repo create GavinHolder/django-context-memory --public --description "Deep code intelligence for AI assistants working with Django projects"
```

---

## 2. Push Your Code to GitHub

From the `django_context_memory` directory:

```bash
# Navigate to library directory
cd django_context_memory

# Initialize git (if not already)
git init

# Add remote
git remote add origin https://github.com/GavinHolder/django-context-memory.git

# Add all files
git add .

# Create .gitignore if needed
cat > .gitignore << EOF
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/
.venv/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Testing
.tox/
.coverage
.pytest_cache/
htmlcov/

# OS
.DS_Store
Thumbs.db
EOF

# Commit
git add .
git commit -m "Initial commit: Django Context Memory v1.0.0"

# Push to GitHub
git push -u origin main

# If using 'master' branch:
# git push -u origin master
```

---

## 3. Set Up PyPI API Token in GitHub Secrets

### Step 1: Get Your PyPI API Token

1. Go to https://pypi.org/manage/account/
2. Scroll to "API tokens"
3. Click "Add API token"
4. Token name: `django-context-memory-github-actions`
5. Scope: "Entire account" (you can change to project-specific after first upload)
6. Click "Add token"
7. **COPY THE TOKEN** (starts with `pypi-`) - you won't see it again!

### Step 2: Add Token to GitHub Secrets

1. Go to your repo: https://github.com/GavinHolder/django-context-memory
2. Click **Settings** (top menu)
3. In left sidebar, click **Secrets and variables** → **Actions**
4. Click **New repository secret**
5. Name: `PYPI_API_TOKEN`
6. Value: Paste your PyPI token (the full `pypi-...` string)
7. Click **Add secret**

---

## 4. Verify GitHub Actions Workflow

The workflow file is already created at:
```
.github/workflows/publish.yml
```

### What It Does

The workflow automatically publishes to PyPI when you:
1. Create a GitHub Release (recommended)
2. Manually trigger it (via GitHub Actions tab)

### Test the Workflow (Manual Trigger)

1. Go to your repo on GitHub
2. Click **Actions** tab
3. Click **Publish to PyPI** workflow
4. Click **Run workflow** button
5. Select branch (main/master)
6. Click **Run workflow**

**Note:** This will attempt to publish, so make sure your version is ready!

---

## 5. Create Your First Release

### Update Version

Before creating a release, ensure version is correct:

```bash
# Edit django_context_memory/__init__.py
__version__ = "1.0.0"

# Edit setup.py
version="1.0.0",

# Commit version
git add django_context_memory/__init__.py setup.py
git commit -m "Bump version to 1.0.0"
git push
```

### Create Release via GitHub

1. Go to https://github.com/GavinHolder/django-context-memory
2. Click **Releases** (right sidebar)
3. Click **Create a new release**
4. Click **Choose a tag**
5. Type: `v1.0.0` and click **Create new tag: v1.0.0 on publish**
6. Release title: `v1.0.0 - Initial Release`
7. Description: Copy from CHANGELOG.md or write:
   ```markdown
   ## Django Context Memory v1.0.0

   Initial production release of Django Context Memory!

   ### Features
   - Deep code analysis using Python AST
   - Django-aware extraction (models, views, forms, admin, etc.)
   - CLI tools with `django-context` command
   - Aggregated context generation
   - Auto-generated documentation
   - Comprehensive error handling and logging

   ### Installation
   ```bash
   pip install django-context-memory
   ```

   ### Quick Start
   ```bash
   cd /path/to/your/django/project
   django-context init
   django-context build-all
   ```

   See full documentation at [README.md](https://github.com/GavinHolder/django-context-memory#readme)
   ```
8. Click **Publish release**

### What Happens Next

1. GitHub creates the tag `v1.0.0`
2. GitHub Actions workflow triggers automatically
3. Package is built and uploaded to PyPI
4. Your package is live at https://pypi.org/project/django-context-memory/

---

## 6. Verify Publication

### Check PyPI

1. Go to https://pypi.org/project/django-context-memory/
2. Verify version shows as 1.0.0
3. Check that README displays correctly

### Test Installation

```bash
# Create test environment
python -m venv test_install
source test_install/bin/activate  # Windows: test_install\Scripts\activate

# Install from PyPI
pip install django-context-memory

# Verify
django-context --version
python -c "from django_context_memory import Config; print('SUCCESS')"

# Clean up
deactivate
rm -rf test_install
```

---

## 7. Add Badges to README

After publishing, you can add status badges. Create/edit `README.md`:

```markdown
# Django Context Memory

[![PyPI version](https://badge.fury.io/py/django-context-memory.svg)](https://badge.fury.io/py/django-context-memory)
[![Python Versions](https://img.shields.io/pypi/pyversions/django-context-memory.svg)](https://pypi.org/project/django-context-memory/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Actions](https://github.com/GavinHolder/django-context-memory/workflows/Publish%20to%20PyPI/badge.svg)](https://github.com/GavinHolder/django-context-memory/actions)
```

---

## 8. Repository Settings (Recommended)

### Protect Main Branch

1. Go to **Settings** → **Branches**
2. Click **Add rule**
3. Branch name pattern: `main` (or `master`)
4. Check:
   - ✅ Require a pull request before merging
   - ✅ Require status checks to pass before merging
5. Save changes

### Add Topics

1. Go to your repo homepage
2. Click **⚙️** next to "About"
3. Add topics:
   - `django`
   - `python`
   - `ai`
   - `claude`
   - `code-intelligence`
   - `ast`
   - `code-analysis`
4. Save changes

### Set Up GitHub Pages (Optional)

For documentation hosting:

1. Go to **Settings** → **Pages**
2. Source: Deploy from a branch
3. Branch: `main` / `docs` (create docs folder if needed)
4. Save

---

## 9. Ongoing Workflow

### For Each New Release

1. **Update code** and commit changes
2. **Update version** in `__init__.py` and `setup.py`
3. **Update CHANGELOG.md** with changes
4. **Commit and push**:
   ```bash
   git add .
   git commit -m "Bump version to x.y.z"
   git push
   ```
5. **Create GitHub Release** with new tag (e.g., `v1.0.1`)
6. **GitHub Actions automatically publishes to PyPI**
7. **Verify** on PyPI and test installation

### Semantic Versioning

- **Patch** (1.0.0 → 1.0.1): Bug fixes
- **Minor** (1.0.1 → 1.1.0): New features (backward compatible)
- **Major** (1.1.0 → 2.0.0): Breaking changes

---

## 10. Troubleshooting

### "Package already exists" on PyPI

- You can't overwrite a published version
- Increment version number and republish

### Workflow fails with "Invalid credentials"

- Check that `PYPI_API_TOKEN` secret is set correctly
- Regenerate PyPI token if needed

### "Tag already exists"

- Delete the tag locally and remotely:
  ```bash
  git tag -d v1.0.0
  git push origin :refs/tags/v1.0.0
  ```
- Create release again with correct tag

### Workflow doesn't trigger

- Check that workflow file is in `.github/workflows/`
- Verify file is named `publish.yml`
- Check that you created a **Release**, not just a tag

---

## Quick Reference

### Initial Setup Checklist

- [ ] Create GitHub repo: `GavinHolder/django-context-memory`
- [ ] Push code to GitHub
- [ ] Get PyPI API token
- [ ] Add `PYPI_API_TOKEN` to GitHub Secrets
- [ ] Verify workflow file exists: `.github/workflows/publish.yml`
- [ ] Create first release (v1.0.0)
- [ ] Verify package on PyPI
- [ ] Test installation

### For Each Release

- [ ] Update version numbers
- [ ] Update CHANGELOG.md
- [ ] Commit and push
- [ ] Create GitHub Release
- [ ] Verify on PyPI
- [ ] Test installation

---

## Resources

- **Your Repo**: https://github.com/GavinHolder/django-context-memory
- **PyPI Project**: https://pypi.org/project/django-context-memory/
- **GitHub Actions Docs**: https://docs.github.com/en/actions
- **PyPI Publishing Guide**: https://packaging.python.org/tutorials/packaging-projects/

---

**You're all set!** 🚀

Follow the steps above to get your package on GitHub and PyPI.
