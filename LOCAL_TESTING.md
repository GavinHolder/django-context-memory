# Local Testing Guide

## Testing the Library Without PyPI/GitHub

You can test the library locally before publishing. Here's how:

---

## Step 1: Install Library in Editable Mode

From the project root (`D:\Projects\2025\WebAppManager`):

```bash
# Install the library in editable/development mode
pip install -e ./django_context_memory

# Verify installation
pip list | grep django-context-memory
```

**What this does:**
- Installs the library from local directory
- Changes to code are immediately available (no need to reinstall)
- CLI command `django-context` becomes available globally

---

## Step 2: Test CLI Commands

You can now test CLI commands from **any** directory:

```bash
# Test CLI is working
django-context --version
django-context --help

# Go to your Django project (the current WebAppManager project)
cd D:\Projects\2025\WebAppManager

# Test initialization
django-context init

# Test scanning
django-context scan-all

# Test building
django-context build-all

# Check status
django-context status

# View generated files
dir .app_memory
type .app_memory\claude_aggregated_context.json
```

---

## Step 3: Test Python API

Create a test script to verify Python API:

**Create `test_library.py`:**

```python
"""
Test script for django_context_memory library
"""
from pathlib import Path
from django_context_memory import Config, ProjectScanner, ContextBuilder

# Test in current project
PROJECT_ROOT = Path(__file__).parent

print("=" * 60)
print("Testing Django Context Memory Library")
print("=" * 60)

# Test 1: Configuration
print("\n1. Testing Configuration...")
config = Config(PROJECT_ROOT)
print(f"   ✓ Project: {config.project_name}")
print(f"   ✓ Memory dir: {config.memory_dir}")
print(f"   ✓ Deep analysis: {config.get('deep_analysis')}")

# Test 2: Scanner
print("\n2. Testing Project Scanner...")
scanner = ProjectScanner(PROJECT_ROOT, config)
apps = scanner.discover_apps()
print(f"   ✓ Found {len(apps)} Django apps:")
for app in apps:
    print(f"     - {app['name']} ({app['path']})")

# Test 3: Context Builder
print("\n3. Testing Context Builder...")
builder = ContextBuilder(PROJECT_ROOT, config)

if apps:
    first_app = apps[0]['name']
    print(f"   Testing with app: {first_app}")

    # Create snapshot
    snapshot = builder.create_snapshot(first_app, stage='test')
    print(f"   ✓ Snapshot created: {len(snapshot['files'])} files")

    # Build context
    context = builder.build_app_context(first_app)
    print(f"   ✓ Context built:")
    summary = context.get('summary', {})
    print(f"     - Models: {len(summary.get('models', []))}")
    print(f"     - Views: {len(summary.get('views', []))}")
    print(f"     - Functions: {len(summary.get('functions', []))}")

# Test 4: Aggregated Context
print("\n4. Testing Aggregated Context...")
aggregated = builder.build_aggregated_context()
print(f"   ✓ Aggregated context built:")
print(f"     - Total apps: {aggregated['total_apps']}")
print(f"     - Total files: {aggregated['total_files']}")

print("\n" + "=" * 60)
print("All tests passed! ✓")
print("=" * 60)
```

**Run the test:**

```bash
cd D:\Projects\2025\WebAppManager
python test_library.py
```

---

## Step 4: Test Django Web UI Integration

Test the web dashboard in your current Django project:

### 4.1 Update settings.py

Add to `INSTALLED_APPS`:

```python
# OpsMan/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your existing apps
    'core',
    'infrastructure',
    'settings',
    # ... other apps ...

    # Add Django Context Memory web UI
    'django_context_memory',  # <-- Add this line
]
```

### 4.2 Update urls.py

Add to URL patterns:

```python
# OpsMan/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Your existing URLs
    path('', include('core.urls')),
    path('infrastructure/', include('infrastructure.urls')),
    # ... other URLs ...

    # Add Django Context Memory dashboard
    path('context-memory/', include('django_context_memory.urls')),  # <-- Add this line
]
```

### 4.3 Test the Web UI

```bash
# Make sure dev server is running
python manage.py runserver

# Open browser and visit:
# http://localhost:8000/context-memory/

# You should see the Context Memory dashboard!
```

**Test features:**
1. View discovered apps
2. Click "Build All Apps" button
3. Watch progress
4. See statistics update
5. Check `.app_memory/` directory for generated files

---

## Step 5: Verify Generated Files

After running tests, verify the output:

```bash
# List generated files
dir .app_memory

# Should see:
# - claude_aggregated_context.json (main file for AI)
# - aggregated_context.json (human-readable)
# - app_name/ directories for each app

# View aggregated context
type .app_memory\claude_aggregated_context.json

# View individual app context
type .app_memory\infrastructure\claude_context.json
```

---

## Step 6: Test in Another Django Project

To verify it works in **any** Django project:

```bash
# Go to a different Django project
cd C:\path\to\another\django\project

# Use CLI (no installation in that project needed)
django-context init
django-context build-all

# Should work immediately!
```

---

## Troubleshooting Local Testing

### Issue: "django-context: command not found"

**Solution:**
```bash
# Reinstall in editable mode
pip uninstall django-context-memory
pip install -e D:\Projects\2025\WebAppManager\django_context_memory

# Verify
django-context --version
```

### Issue: "cannot import name 'Config'"

**Solution:**
```bash
# Check installation
pip show django-context-memory

# Should show:
# Location: d:\projects\2025\webappmanager\django_context_memory

# If not found, reinstall
pip install -e D:\Projects\2025\WebAppManager\django_context_memory
```

### Issue: Web UI shows 404

**Solution:**
```bash
# Make sure URL pattern is added
# Check OpsMan/urls.py includes:
# path('context-memory/', include('django_context_memory.urls')),

# Restart Django server
python manage.py runserver
```

### Issue: Template not found

**Solution:**
```bash
# Verify template exists
dir django_context_memory\django_context_memory\templates\django_context_memory\index.html

# If missing, make sure package_data in setup.py includes templates
```

---

## Quick Test Checklist

- [ ] Install library: `pip install -e ./django_context_memory`
- [ ] Test CLI version: `django-context --version`
- [ ] Test CLI init: `django-context init`
- [ ] Test CLI build: `django-context build-all`
- [ ] Run Python test script: `python test_library.py`
- [ ] Add to INSTALLED_APPS in settings.py
- [ ] Add URL pattern in urls.py
- [ ] Access web UI: `http://localhost:8000/context-memory/`
- [ ] Click "Build All Apps" button
- [ ] Verify files in `.app_memory/`

---

## Next Steps After Local Testing

Once local testing passes:

1. **Push to GitHub** (see `GITHUB_SETUP.md`)
2. **Create a release** on GitHub (v1.0.0)
3. **Automatic PyPI publish** via GitHub Actions
4. **Test PyPI install**: `pip install django-context-memory`

---

## Clean Up After Testing

If you want to clean up test data:

```bash
# Remove generated files
django-context clean

# Or manually
rmdir /s .app_memory

# Uninstall library
pip uninstall django-context-memory
```

---

## Summary

**Local testing workflow:**

1. Install editable: `pip install -e ./django_context_memory`
2. Test CLI: `django-context build-all`
3. Test API: `python test_library.py`
4. Test Web UI: Add to INSTALLED_APPS → browse to `/context-memory/`
5. Verify output in `.app_memory/`

**All testing can be done locally before publishing to PyPI!**
