# Publishing Django Context Memory to PyPI

Complete step-by-step guide to publish this library to the Python Package Index (PyPI).

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Pre-Publishing Checklist](#pre-publishing-checklist)
- [Step-by-Step Publishing Process](#step-by-step-publishing-process)
- [Testing the Published Package](#testing-the-published-package)
- [Updating After Publication](#updating-after-publication)
- [Troubleshooting](#troubleshooting)

---

## Prerequisites

### 1. PyPI Account

Create accounts on both Test PyPI and Production PyPI:

1. **Test PyPI** (for testing): https://test.pypi.org/account/register/
2. **Production PyPI** (for real release): https://pypi.org/account/register/

### 2. API Tokens

Generate API tokens for secure uploads:

**Test PyPI:**
1. Go to https://test.pypi.org/manage/account/
2. Scroll to "API tokens"
3. Click "Add API token"
4. Name it (e.g., "django-context-memory-test")
5. Scope: "Entire account" (or specific project after first upload)
6. Copy the token (starts with `pypi-`)

**Production PyPI:**
1. Go to https://pypi.org/manage/account/
2. Follow same steps as Test PyPI
3. Save the token securely

### 3. Install Build Tools

```bash
pip install --upgrade pip
pip install build twine
```

---

## Pre-Publishing Checklist

Before publishing, verify everything is ready:

### ✅ 1. Package Structure

Verify your structure looks like this:

```
django_context_memory/
├── django_context_memory/        # Python package
│   ├── __init__.py               # Version, exports
│   ├── analyzer.py
│   ├── builder.py
│   ├── scanner.py
│   ├── config.py
│   ├── cli.py
│   ├── doc_generator.py
│   └── utils.py
├── setup.py                      # Package configuration
├── pyproject.toml               # Build system config
├── README.md                    # Package description
├── LICENSE                      # License file
├── CHANGELOG.md                 # Version history
├── INSTALLATION.md              # Installation guide
├── CLI_GUIDE.md                 # CLI documentation
└── MANIFEST.in                  # Include non-Python files
```

### ✅ 2. Version Number

Check version in `django_context_memory/__init__.py`:

```python
__version__ = "1.0.0"  # Update this before each release
```

### ✅ 3. README.md

Ensure README.md has:
- Clear description
- Installation instructions
- Quick start example
- Features list
- License

### ✅ 4. LICENSE

Ensure you have a LICENSE file (currently MIT).

### ✅ 5. setup.py

Verify all metadata is correct:

```python
setup(
    name="django-context-memory",
    version="1.0.0",  # Match __init__.py version
    author="Gavin Holder",
    author_email="mangleholder@gmail.com",  # ✓ Already updated
    description="Deep code intelligence for Django projects",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/GavinHolder/django-context-memory",  # ✓ Updated
    # ... rest of setup
)
```

### ✅ 6. CHANGELOG.md

Document the version you're releasing:

```markdown
## [1.0.0] - 2025-12-29

### Added
- Initial production release
- Deep code analysis using Python AST
- CLI tools (django-context command)
- ... etc
```

### ✅ 7. Create MANIFEST.in

Create this file to include documentation:

```bash
cd django_context_memory
```

Create `MANIFEST.in`:

```
include README.md
include LICENSE
include CHANGELOG.md
include INSTALLATION.md
include CLI_GUIDE.md
include pyproject.toml
recursive-include django_context_memory *.py
```

---

## Step-by-Step Publishing Process

### Step 1: Clean Previous Builds

```bash
cd django_context_memory

# Remove old build artifacts
rm -rf build/ dist/ *.egg-info

# On Windows:
# rmdir /s /q build dist
# del /s /q *.egg-info
```

### Step 2: Update Version Number

1. Edit `django_context_memory/__init__.py`:
   ```python
   __version__ = "1.0.0"  # Your version
   ```

2. Edit `setup.py`:
   ```python
   version="1.0.0",  # Match __init__.py
   ```

3. Update `CHANGELOG.md` with release notes

### Step 3: Build Distribution Packages

```bash
cd django_context_memory

# Build both wheel and source distribution
python -m build

# This creates:
# dist/django_context_memory-1.0.0-py3-none-any.whl
# dist/django_context_memory-1.0.0.tar.gz
```

**Output should look like:**
```
* Creating venv isolated environment...
* Installing packages in isolated environment... (setuptools)
* Getting build dependencies for sdist...
* Building sdist...
* Building wheel from sdist...
* Successfully built django_context_memory-1.0.0.tar.gz and django_context_memory-1.0.0-py3-none-any.whl
```

### Step 4: Check the Build

```bash
# Verify the package was built correctly
twine check dist/*

# Should output:
# Checking dist/django_context_memory-1.0.0-py3-none-any.whl: PASSED
# Checking dist/django_context_memory-1.0.0.tar.gz: PASSED
```

### Step 5: Test on Test PyPI (RECOMMENDED)

Upload to Test PyPI first to make sure everything works:

```bash
# Upload to Test PyPI
twine upload --repository testpypi dist/*

# You'll be prompted for:
# Username: __token__
# Password: pypi-... (your Test PyPI API token)
```

**Or use API token directly:**

```bash
# Create ~/.pypirc file
cat > ~/.pypirc << EOF
[testpypi]
  username = __token__
  password = pypi-YOUR_TEST_PYPI_TOKEN_HERE

[pypi]
  username = __token__
  password = pypi-YOUR_PRODUCTION_PYPI_TOKEN_HERE
EOF

# Then upload
twine upload --repository testpypi dist/*
```

### Step 6: Test Installation from Test PyPI

```bash
# Create a test environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install from Test PyPI
pip install --index-url https://test.pypi.org/simple/ django-context-memory

# Test the CLI
django-context --version

# Test imports
python -c "from django_context_memory import Config, ContextBuilder; print('OK')"

# Deactivate and clean up
deactivate
rm -rf test_env
```

### Step 7: Upload to Production PyPI

Once testing is successful:

```bash
# Upload to production PyPI
twine upload dist/*

# You'll be prompted for:
# Username: __token__
# Password: pypi-... (your Production PyPI API token)
```

**Success!** Your package is now live at:
`https://pypi.org/project/django-context-memory/`

### Step 8: Verify Production Install

```bash
# Create fresh environment
python -m venv verify_env
source verify_env/bin/activate  # On Windows: verify_env\Scripts\activate

# Install from production PyPI
pip install django-context-memory

# Verify
django-context --version
python -c "from django_context_memory import Config; print('SUCCESS')"

# Clean up
deactivate
rm -rf verify_env
```

---

## Testing the Published Package

### Test in a Real Django Project

```bash
# Go to a test Django project
cd /path/to/test-django-project

# Install the published package
pip install django-context-memory

# Test the workflow
django-context init
django-context scan-all
django-context build-all
django-context status

# Verify output
ls -la .app_memory/
cat .app_memory/claude_aggregated_context.json
```

### Test Python API

```python
from pathlib import Path
from django_context_memory import Config, ContextBuilder

# Test basic usage
config = Config(Path.cwd())
builder = ContextBuilder(Path.cwd(), config)

# Should work without errors
print("Package installed correctly!")
```

---

## Updating After Publication

### For Bug Fixes (Patch Version)

1. **Update version**: `1.0.0` → `1.0.1`
   - Edit `__init__.py` and `setup.py`
   - Update `CHANGELOG.md`

2. **Build and upload**:
   ```bash
   rm -rf dist/
   python -m build
   twine check dist/*
   twine upload dist/*
   ```

### For New Features (Minor Version)

1. **Update version**: `1.0.1` → `1.1.0`
2. Document new features in `CHANGELOG.md`
3. Update `README.md` if needed
4. Build and upload (same as above)

### For Breaking Changes (Major Version)

1. **Update version**: `1.1.0` → `2.0.0`
2. Document breaking changes clearly
3. Consider migration guide
4. Build and upload

---

## Automating with GitHub Actions (Optional)

Create `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install build twine

      - name: Build package
        run: python -m build
        working-directory: ./django_context_memory

      - name: Publish to PyPI
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
        run: twine upload dist/*
        working-directory: ./django_context_memory
```

**Setup:**
1. Go to your GitHub repo → Settings → Secrets
2. Add secret: `PYPI_API_TOKEN` with your PyPI token
3. Create a release on GitHub
4. Package automatically publishes to PyPI

---

## Troubleshooting

### "File already exists"

**Problem:** You're trying to upload a version that's already on PyPI.

**Solution:** You can't overwrite published versions. Increment the version number:
```python
# In __init__.py and setup.py
__version__ = "1.0.1"  # Increment from 1.0.0
```

### "Invalid distribution"

**Problem:** Package structure is incorrect.

**Solution:**
```bash
# Verify structure
twine check dist/*

# Rebuild
rm -rf dist/ build/
python -m build
```

### "Authentication error"

**Problem:** Wrong credentials or token.

**Solutions:**
1. Make sure username is `__token__`
2. Paste full token including `pypi-` prefix
3. Check you're using the right token (test vs production)
4. Regenerate token if needed

### "README rendering issues"

**Problem:** README.md doesn't display properly on PyPI.

**Solution:**
1. Check Markdown syntax
2. Verify in setup.py:
   ```python
   long_description_content_type="text/markdown"
   ```
3. Test locally:
   ```bash
   pip install readme-renderer
   python -m readme_renderer README.md
   ```

### "Module not found after install"

**Problem:** Package installs but imports fail.

**Solution:**
1. Check `__init__.py` has correct exports:
   ```python
   from .analyzer import CodeAnalyzer
   from .builder import ContextBuilder
   # ... etc

   __all__ = ["CodeAnalyzer", "ContextBuilder", ...]
   ```

2. Verify package structure:
   ```bash
   pip show -f django-context-memory
   ```

---

## Quick Reference

### Complete First-Time Publishing

```bash
# 1. Prepare
cd django_context_memory
rm -rf dist/ build/ *.egg-info

# 2. Update version in __init__.py and setup.py to 1.0.0

# 3. Build
python -m build

# 4. Check
twine check dist/*

# 5. Test PyPI (optional but recommended)
twine upload --repository testpypi dist/*
pip install --index-url https://test.pypi.org/simple/ django-context-memory

# 6. Production PyPI
twine upload dist/*

# 7. Verify
pip install django-context-memory
django-context --version
```

### Update Existing Package

```bash
# 1. Update version number (e.g., 1.0.0 → 1.0.1)
# 2. Update CHANGELOG.md
# 3. Clean and rebuild
rm -rf dist/
python -m build
twine check dist/*
twine upload dist/*
```

---

## After Publishing

### 1. Tag the Release

```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

### 2. Create GitHub Release

1. Go to your repo on GitHub
2. Click "Releases" → "Create a new release"
3. Choose the tag you just created
4. Add release notes from CHANGELOG.md
5. Publish release

### 3. Announce

- Update your README with PyPI installation instructions
- Share on social media, forums, etc.
- Add PyPI badge to README:
  ```markdown
  [![PyPI version](https://badge.fury.io/py/django-context-memory.svg)](https://badge.fury.io/py/django-context-memory)
  ```

---

## Best Practices

1. **Always test on Test PyPI first**
2. **Increment version for every release** (can't reuse versions)
3. **Keep CHANGELOG.md updated**
4. **Use semantic versioning** (MAJOR.MINOR.PATCH)
5. **Test installation in clean environment before publishing**
6. **Don't commit your PyPI tokens to git**
7. **Use API tokens instead of passwords**
8. **Tag releases in git**

---

## Resources

- **PyPI**: https://pypi.org/
- **Test PyPI**: https://test.pypi.org/
- **Packaging Guide**: https://packaging.python.org/
- **Twine Docs**: https://twine.readthedocs.io/
- **Semantic Versioning**: https://semver.org/

---

**You're ready to publish!** 🚀

Run through the checklist, follow the steps, and your library will be available for anyone to install with:

```bash
pip install django-context-memory
```
