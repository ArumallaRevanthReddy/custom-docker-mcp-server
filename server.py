#!/usr/bin/env python3
"""
Docker MCP Server

Provides Docker management tools via the Model Context Protocol.
"""

from mcp.server.fastmcp import FastMCP
import docker

# Initialize the MCP server
mcp = FastMCP("docker")


# Tools will be implemented here


def main():
    """Run the MCP server."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
