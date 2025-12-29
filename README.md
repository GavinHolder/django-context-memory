# Django Context Memory

A standalone library for generating deep code intelligence and context for AI assistants like Claude Code.

## What It Does

Converts your Django codebase into structured, machine-readable context that AI assistants can use to:
- Understand your models, views, and URL structure
- Track dependencies and cross-app relationships
- Navigate your architecture intelligently
- Provide better suggestions with full project context

## Features

- **Deep Code Analysis**: Extracts functions, classes, models, views, forms, URLs, and imports
- **Cross-App Intelligence**: Maps dependencies and relationships between apps
- **Technology Stack Detection**: Identifies Django components and third-party packages
- **Auto-Generated Documentation**: Creates project-specific README and policies
- **CLI Tools**: Simple commands for initialization and context building
- **Framework-Aware**: Understands Django patterns (models, views, admin, serializers)

## Installation

```bash
pip install django-context-memory
```

Or install from source:
```bash
cd django_context_memory
pip install -e .
```

## Quick Start

### 1. Initialize in Your Project

```bash
cd /path/to/your/django/project
django-context init
```

This will:
- Create `.app_memory/` directory
- Scan your project structure
- Generate initial configuration
- Create project-specific README and policies

### 2. Build Context for an App

```bash
django-context scan infrastructure
django-context build infrastructure
```

### 3. Build Context for All Apps

```bash
django-context scan-all
django-context build-all
```

### 4. Use in Your Code

```python
from django_context_memory import ContextBuilder, CodeAnalyzer

# Analyze a single file
analyzer = CodeAnalyzer('/path/to/models.py', '/path/to/app')
analysis = analyzer.analyze()

# Build app context
builder = ContextBuilder('/path/to/project')
context = builder.build_app_context('infrastructure')

# Build aggregated context
aggregated = builder.build_aggregated_context()
```

## CLI Commands

| Command | Description |
|---------|-------------|
| `django-context init` | Initialize context memory in project |
| `django-context scan <app>` | Scan and snapshot a specific app |
| `django-context scan-all` | Scan all apps in project |
| `django-context build <app>` | Build context for specific app |
| `django-context build-all` | Build aggregated context for all apps |
| `django-context status` | Show current context status |
| `django-context clean` | Clean all generated context files |

## Configuration

Create `.context_memory_config.json` in your project root:

```json
{
  "project_name": "MyProject",
  "memory_dir": ".app_memory",
  "exclude_patterns": [
    "*/migrations/*",
    "*/__pycache__/*",
    "*.pyc",
    ".git/*"
  ],
  "deep_analysis": true,
  "auto_generate_docs": true
}
```

## Output Structure

```
.app_memory/
├── claude_aggregated_context.json    # Main file for Claude
├── aggregated_context.json           # Human-readable summary
├── infrastructure/
│   ├── snapshot.json                 # Raw scan data
│   ├── app_memory.json              # Versioned context
│   └── claude_context.json          # Machine-readable context
├── dashboard/
│   └── ...
└── settings/
    └── ...
```

## Context Data Structure

Each app context includes:
- **Models**: Fields, types, relationships, methods
- **Views**: Function/class-based views with signatures
- **URLs**: Route patterns mapped to views
- **Forms**: Form classes and fields
- **Dependencies**: Django, third-party, and local imports
- **Classes & Functions**: All code structures
- **Constants**: Module-level variables

## Use Cases

### With Claude Code
1. Build context: `django-context build-all`
2. Claude reads `.app_memory/claude_aggregated_context.json`
3. Claude has full project intelligence
4. Better suggestions, fewer hallucinations

### With Other AI Tools
- Use as knowledge base for AI pair programming
- Feed to custom GPT models
- Integrate with IDE extensions
- Build custom analysis tools

## Advanced Usage

### Custom Analysis

```python
from django_context_memory import CodeAnalyzer

class CustomAnalyzer(CodeAnalyzer):
    def _extract_custom_patterns(self):
        # Add your custom extraction logic
        pass

analyzer = CustomAnalyzer(file_path, app_root)
analysis = analyzer.analyze()
```

### Programmatic Context Building

```python
from django_context_memory import ContextBuilder

builder = ContextBuilder(
    project_root='/path/to/project',
    memory_dir='.app_memory',
    deep_analysis=True
)

# Build with custom options
context = builder.build_app_context(
    'infrastructure',
    include_tests=False,
    include_migrations=False
)
```

## Integration with Django Management Commands

The library can integrate with Django's management commands:

```python
# In your project's settings.py
INSTALLED_APPS = [
    ...
    'django_context_memory',
]
```

Then use:
```bash
python manage.py build_context infrastructure
python manage.py build_all_contexts
```

## Requirements

- Python 3.8+
- Django 3.2+ (for Django projects)
- No additional dependencies for core functionality

## Development

```bash
git clone https://github.com/yourusername/django-context-memory
cd django-context-memory
pip install -e ".[dev]"
pytest
```

## License

MIT License

## Contributing

Contributions welcome! Please read CONTRIBUTING.md first.

## Changelog

See CHANGELOG.md for version history.

## Support

- Issues: https://github.com/yourusername/django-context-memory/issues
- Docs: https://django-context-memory.readthedocs.io

---

**Built for better AI-assisted development** 🚀
