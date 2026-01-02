# Docker MCP Server

A Model Context Protocol (MCP) server providing Docker management tools for Claude Code.

## Overview

This MCP server exposes Docker functionality through MCP tools, allowing Claude to interact with Docker containers, images, networks, and volumes.

## Features

Tools for Docker operations including:
- Container management (list, start, stop, inspect)
- Image management (list, pull, build)
- Network operations
- Volume management
- Docker Compose integration

## Installation

### Prerequisites

- Python 3.11 or higher
- Docker installed and running
- `uv` package manager (recommended) or `pip`

### Setup

```bash
# Install dependencies
uv sync

# Or with pip
pip install -e .
```

## Usage

### With Claude Code

Add the server to your Claude Code configuration:

```bash
claude mcp add --transport stdio docker -- python /path/to/custom-docker-mcp-server/server.py
```

Or configure in `.mcp.json`:

```json
{
  "mcpServers": {
    "docker": {
      "command": "python",
      "args": ["/absolute/path/to/server.py"]
    }
  }
}
```

### Standalone Testing

Test the server using MCP Inspector:

```bash
mcp-inspector -- python server.py
```

## Available Tools

### `list_containers`

Lists all running Docker containers with detailed information.

**Parameters:** None

**Returns:**
- Container ID (short form)
- Container name
- Image name/tag
- Status
- Port mappings

**Example usage:**
```
User: "Show me all running containers"
Claude: Uses list_containers tool
Result: Displays formatted list of running containers
```

## Development

### Project Structure

```
custom-docker-mcp-server/
├── src/                    # Business logic
│   ├── __init__.py        # Package initialization
│   └── containers.py      # Container operations
├── server.py              # Main MCP server implementation
├── pyproject.toml         # Project configuration
├── README.md              # This file
└── .gitignore            # Git ignore rules
```

### Adding New Tools

Tools are implemented using the FastMCP framework with business logic separated in the `src/` directory:

1. **Add business logic** in appropriate module under `src/` (e.g., `src/containers.py`)
2. **Define the MCP tool** in `server.py` using `@mcp.tool()` decorator
3. **Import and call** the business logic from the tool

See `server.py` and `src/containers.py` for examples.

## Requirements

- Docker Engine API access
- Appropriate permissions to manage Docker resources

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.
