#!/usr/bin/env python3
"""
BV-BRC Data MCP Server

This MCP server provides access to BV-BRC (Bacterial and Viral Bioinformatics Resource Center) 
data through the bvbrc-solr-python-api module. It exposes genome and genome feature data 
querying capabilities through MCP tools using FastMCP.
"""

import json
import sys
from typing import Any, Dict, List, Optional

from fastmcp import FastMCP
from data_functions import (
    query_genome_by_id,
    query_genome_by_taxon_id,
    query_genome_by_genome_name,
    format_query_result
)

# Load configuration
try:
    with open('config.json', 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    print("Warning: config.json not found, using defaults", file=sys.stderr)
    config = {
        "base_url": "https://www.bv-brc.org/api",
        "port": 8059,
        "default_limit": 1000
    }

# Get configuration values
base_url = config.get("base_url", "https://www.bv-brc.org/api")
default_limit = config.get("default_limit", 1000)
port = config.get("port", 8059)
mcp_url = config.get("mcp_url", "127.0.0.1")

# Create FastMCP server
mcp = FastMCP("BV-BRC Data MCP Server")

# Register the first 3 genome tools directly
@mcp.tool()
def bvbrc_genome_get_by_id(genome_id: str, limit: int = default_limit, 
                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
    """
    Get genome data by genome ID.
    
    Args:
        genome_id: The genome ID to query (e.g., "208964.12")
        limit: Maximum number of results to return (default: 1000)
        select: Comma-separated list of fields to select (optional)
        sort: Field to sort by (optional)
    
    Returns:
        Formatted genome data
    """
    options = {"limit": limit}
    if select:
        options["select"] = select.split(",")
    if sort:
        options["sort"] = sort
    
    try:
        result = query_genome_by_id(genome_id, options, base_url)
        return format_query_result(result)
    except Exception as e:
        return f"Error querying genome by ID: {str(e)}"


@mcp.tool()
def bvbrc_genome_get_by_taxon_id(taxon_id: int, limit: int = default_limit,
                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
    """
    Get genome data by taxon ID.
    
    Args:
        taxon_id: The taxon ID to query (e.g., 562)
        limit: Maximum number of results to return (default: 1000)
        select: Comma-separated list of fields to select (optional)
        sort: Field to sort by (optional)
    
    Returns:
        Formatted genome data
    """
    options = {"limit": limit}
    if select:
        options["select"] = select.split(",")
    if sort:
        options["sort"] = sort
    
    try:
        result = query_genome_by_taxon_id(taxon_id, options, base_url)
        return format_query_result(result)
    except Exception as e:
        return f"Error querying genome by taxon ID: {str(e)}"


@mcp.tool()
def bvbrc_genome_get_by_genome_name(genome_name: str, limit: int = default_limit,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
    """
    Get genome data by genome name.
    
    Args:
        genome_name: The genome name to query (e.g., "Escherichia coli")
        limit: Maximum number of results to return (default: 1000)
        select: Comma-separated list of fields to select (optional)
        sort: Field to sort by (optional)
    
    Returns:
        Formatted genome data
    """
    options = {"limit": limit}
    if select:
        options["select"] = select.split(",")
    if sort:
        options["sort"] = sort
    
    try:
        result = query_genome_by_genome_name(genome_name, options, base_url)
        return format_query_result(result)
    except Exception as e:
        return f"Error querying genome by genome name: {str(e)}"


@mcp.tool()
def search(query: str) -> str:
    """
    Search for documents from the vast collection of bands I listen to.
    
    Args:
        query: The search query string
        
    Returns:
        JSON string containing search results
    """
    results = []
    results.append({
        "id": "100",
        "title": "Bands, important bands",
        "text": "I listen to bands Lamb of God, Pantera, Malevolence.",
        "url": f"https://platform.openai.com/storage/files/malevolence"
    })
    results.append({
        "id": "101",
        "title": "My favorite bands",
        "text": "My favorite bands are Cannibal Corpse, Grima, Nile.",
        "url": f"https://platform.openai.com/storage/files/cannibalcorpse"
    })

    print(f"Search tool returned {len(results)} results", file=sys.stderr)
    return json.dumps({"results": results})


@mcp.tool()
def fetch(id: str) -> str:
    """
    Retrieve a document by its ID. Due to the test nature of this server,
    it can only return one of the records.
    
    Args:
        id: The document ID to fetch
        
    Returns:
        JSON string containing the document data
    """
    result = {
        "id": "100",
        "title": "Bands, important bands",
        "text": "I listen to bands Lamb of God, Pantera, Malevolence.",
        "url": f"https://platform.openai.com/storage/files/malevolence",
        "metadata": None
    }
    
    print(f"Fetch tool returned bands: Lamb of God, Pantera, Malevolence", file=sys.stderr)
    return json.dumps(result)


def main() -> int:
    try:
        mcp.run(transport="http", host=mcp_url, port=port)
    except KeyboardInterrupt:
        print("Server stopped.", file=sys.stderr)
    except Exception as e:
        print(f"Server error: {e}", file=sys.stderr)
        return 1
    
    return 0


if __name__ == "__main__":
    main()