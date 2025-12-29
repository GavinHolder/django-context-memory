# Changelog

All notable changes to Django Context Memory will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-12-29

### Added
- Initial production release of Django Context Memory
- Deep code analysis using Python AST
- Django-aware extraction (models, views, forms, admin, serializers, URLs)
- Project scanning and app discovery
- Context building with summaries
- Aggregated context generation with cross-app analysis
- CLI tools for easy usage (`django-context` command)
- Configuration management with validation
- Auto-generation of project-specific documentation
- Auto-generation of Claude-specific policies
- Pip-installable package
- Comprehensive documentation
- Comprehensive error handling and logging throughout all modules
- Configuration validation with type checking
- Environment variable overrides (DJANGO_CONTEXT_MEMORY_DIR, DJANGO_CONTEXT_VERBOSE, etc.)
- Utility module with helper functions (formatting, file operations, validation)
- Unicode encoding fallback for file reading
- Configurable file size limits and scan timeouts
- Enhanced exclude patterns for common directories (.venv, staticfiles, media)

### Features
- **Code Analyzer**: Extracts functions, classes, models, views, forms, URLs, imports
- **Project Scanner**: Discovers Django apps and scans file structure
- **Context Builder**: Builds structured context with versioning
- **CLI Interface**: Simple commands for initialization and context building
- **Documentation Generator**: Auto-generates README and policies
- **Configuration**: Flexible configuration via JSON file
- **Deep Analysis**: Full AST-based code intelligence
- **Cross-App Analysis**: Maps dependencies and relationships

### Technology Stack
- Python 3.8+
- No runtime dependencies (Django optional)
- Uses Python's built-in `ast` module for parsing

---

## Future Releases

### Planned Features
- Support for more frameworks (Flask, FastAPI)
- Integration with more AI assistants
- Web UI for context visualization
- Real-time context updates
- Context diffing and change detection
- Export to various formats
- Plugin system for custom analyzers

---

For detailed information about each release, see the commit history at:
https://github.com/gavinholder/django-context-memory
