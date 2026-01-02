"""
Container management operations for Docker MCP server.
"""

import docker
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)


def list_running_containers() -> str:
    """
    List all running Docker containers.

    Returns:
        Formatted string with container information or error message
    """
    try:
        # Connect to Docker daemon
        client = docker.from_env()

        # Get all running containers
        containers = client.containers.list()

        if not containers:
            return "No running containers found."

        # Format container information
        result = f"Found {len(containers)} running container(s):\n\n"

        for container in containers:
            # Extract container details
            container_id = container.short_id
            name = container.name
            image = container.image.tags[0] if container.image.tags else container.image.short_id
            status = container.status

            # Get ports mapping
            ports = container.ports
            ports_str = _format_ports(ports) if ports else "No exposed ports"

            # Build container info string
            result += f"Container: {name}\n"
            result += f"  ID: {container_id}\n"
            result += f"  Image: {image}\n"
            result += f"  Status: {status}\n"
            result += f"  Ports: {ports_str}\n"
            result += "\n"

        return result.strip()

    except docker.errors.DockerException as e:
        logger.error(f"Docker error while listing containers: {e}")
        return f"Error: Unable to connect to Docker daemon. Is Docker running? Details: {str(e)}"

    except Exception as e:
        logger.error(f"Unexpected error while listing containers: {e}")
        return f"Error: An unexpected error occurred while listing containers: {str(e)}"


def _format_ports(ports: Dict[str, Any]) -> str:
    """
    Format port mappings for display.

    Args:
        ports: Dictionary of port mappings from Docker API

    Returns:
        Formatted string of port mappings
    """
    if not ports:
        return "None"

    port_mappings = []

    for container_port, host_bindings in ports.items():
        if host_bindings:
            for binding in host_bindings:
                host_ip = binding.get('HostIp', '0.0.0.0')
                host_port = binding.get('HostPort', '?')
                port_mappings.append(f"{host_ip}:{host_port} -> {container_port}")
        else:
            port_mappings.append(f"{container_port} (not bound)")

    return ", ".join(port_mappings) if port_mappings else "None"
