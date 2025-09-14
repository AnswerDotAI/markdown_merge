

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working
with code in this repository.

## Development Commands

### Building

- `nbdev_export` - Export notebooks to Python modules (standard nbdev
  workflow)

## Architecture Overview

This is an nbdev-based Python library for sending templated emails in
markdown format. The codebase follows nbdev conventions where the actual
implementation is written in Jupyter notebooks and auto-generated into
Python modules.

### Key Components

**Core Module**: `markdown_merge/markdown_merge.py` (auto-generated from
`00_markdown_merge.ipynb`) - `MarkdownMerge`: Main class for sending
templated email merge messages - `get_addr()`: Convert email/name to
Address objects - `md2email()`: Create multipart email from markdown -
`smtp_connection()`: Context manager for SMTP connections -
`attach_file()`: Attach files to email messages

**Source Files**: - `00_markdown_merge.ipynb`: Main implementation
notebook with API code - `index.ipynb`: Documentation and usage examples
(generates README.md)

### Development Workflow

1.  Edit notebooks (`.ipynb` files) - never edit the generated `.py`
    files directly
2.  Run `nbdev_export` to regenerate Python modules from notebooks
3.  The library supports email templating with variable substitution
    using `{variable}` syntax

### Configuration

- `settings.ini`: nbdev configuration with package metadata
- Uses standard SMTP configuration with support for SSL/TLS connections

### Dependencies

- `fastcore`: Utility functions
- `markdown`: Markdown to HTML conversion
- Standard library: `smtplib`, `email` modules for email handling
