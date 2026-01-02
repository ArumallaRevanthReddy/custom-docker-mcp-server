#!/usr/bin/env python3
"""
Docker MCP Server

Provides Docker management tools via the Model Context Protocol.
"""

from mcp.server.fastmcp import FastMCP
from src.containers import list_running_containers

# Initialize the MCP server
mcp = FastMCP("docker")


@mcp.tool()
async def list_containers() -> str:
    """
    List all running Docker containers.

    Returns:
        Formatted list of running containers with their details including:
        - Container ID
        - Name
        - Image
        - Status
        - Port mappings
    """
    return list_running_containers()


def main():
    """Run the MCP server."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
