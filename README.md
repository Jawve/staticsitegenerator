# staticsitegenerator

# **What It Does, What I Learned, and Features**

This project is a Python based static site generator that converts Markdown content into fully rendered hmtl pages. It uses a custom-built Markdown parser that feeds into an internal HTML node system to generate valid, structured HTML without relying on third-party Markdown libraries.

The generator processes content recursively, applies a shared template for consistent layout, and outputs a deplooyable static site suitable for GitHube Pages and similar hosts.

## **What I Learned**

Through this project, I gained hands-on experience with:
- parsing strategies for both block-level and inline Markdown syntax
- Designing and using AST-like internal representations (via HTML node trees)
- Recursive file traversal and build-style workflows
- Implementing tooling without relying on external parsing libraries

## **Features**

- Custom Markldown to HTML parser implemented from scratch
- Support for common markdown syntax: (headings, paragraphs, bold, code, lists, etc.)
- Structured project layout for easy content input and output generation
- Template-based rendering to ensure consistent theming across pages.
- Recursive static asset copying
- CLI-driven workflow
- Deployed output available via GitHub pages: https://jawve.github.io/staticsitegenerator/

# Status
Complete
