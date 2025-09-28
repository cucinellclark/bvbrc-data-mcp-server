#!/usr/bin/env python3
"""
BV-BRC Data MCP Server

This MCP server provides access to BV-BRC (Bacterial and Viral Bioinformatics Resource Center) 
data through the bvbrc-solr-python-api module. It exposes genome and genome feature data 
querying capabilities through MCP tools using FlaskMCP.
"""

import json
import sys
from typing import Any, Dict, List, Optional

from flask import Flask
from flaskmcp import create_app

# Import tool modules
from tools import (
    register_genome_tools,
    register_genome_feature_tools,
    register_antibiotics_tools,
    register_bioset_tools,
    register_bioset_result_tools,
    register_enzyme_class_ref_tools,
    register_epitope_assay_tools,
    register_epitope_tools,
    register_experiment_tools,
    register_gene_ontology_ref_tools,
    register_genome_amr_tools,
    register_genome_sequence_tools,
    register_id_ref_tools,
    register_misc_niaid_sgc_tools,
    register_pathway_ref_tools,
    register_pathway_tools,
    register_ppi_tools,
    register_protein_family_ref_tools,
    register_protein_feature_tools,
    register_protein_structure_tools,
    register_sequence_feature_vt_tools,
    register_sequence_feature_tools,
    register_serology_tools,
    register_sp_gene_ref_tools,
    register_sp_gene_tools,
    register_spike_lineage_tools,
    register_spike_variant_tools,
    register_strain_tools,
    register_structured_assertion_tools,
    register_subsystem_ref_tools,
    register_subsystem_tools,
    register_surveillance_tools,
    register_taxonomy_tools,
    register_common_tools
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

# Create Flask app and MCP server
app = create_app({'DEBUG': True})

# Register all tools from the modular files
register_genome_tools(base_url, default_limit)
register_genome_feature_tools(base_url, default_limit)
register_antibiotics_tools(base_url, default_limit)
register_bioset_tools(base_url, default_limit)
register_bioset_result_tools(base_url, default_limit)
register_enzyme_class_ref_tools(base_url, default_limit)
register_epitope_assay_tools(base_url, default_limit)
register_epitope_tools(base_url, default_limit)
register_experiment_tools(base_url, default_limit)
register_gene_ontology_ref_tools(base_url, default_limit)
register_genome_amr_tools(base_url, default_limit)
register_genome_sequence_tools(base_url, default_limit)
register_id_ref_tools(base_url, default_limit)
register_misc_niaid_sgc_tools(base_url, default_limit)
register_pathway_ref_tools(base_url, default_limit)
register_pathway_tools(base_url, default_limit)
register_ppi_tools(base_url, default_limit)
register_protein_family_ref_tools(base_url, default_limit)
register_protein_feature_tools(base_url, default_limit)
register_protein_structure_tools(base_url, default_limit)
register_sequence_feature_vt_tools(base_url, default_limit)
register_sequence_feature_tools(base_url, default_limit)
register_serology_tools(base_url, default_limit)
register_sp_gene_ref_tools(base_url, default_limit)
register_sp_gene_tools(base_url, default_limit)
register_spike_lineage_tools(base_url, default_limit)
register_spike_variant_tools(base_url, default_limit)
register_strain_tools(base_url, default_limit)
register_structured_assertion_tools(base_url, default_limit)
register_subsystem_ref_tools(base_url, default_limit)
register_subsystem_tools(base_url, default_limit)
register_surveillance_tools(base_url, default_limit)
register_taxonomy_tools(base_url, default_limit)
register_common_tools(base_url, default_limit)


# Optional: Add a health check route
@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    from flask import jsonify
    return jsonify({"status": "healthy", "service": "bvbrc-data-mcp"})


def main() -> int:
    """Main entry point for the BV-BRC Data MCP Server."""
    print(f"Starting BV-BRC Data MCP Flask Server on port {port}...", file=sys.stderr)
    
    try:
        app.run(host="127.0.0.1", port=port, debug=True)
    except KeyboardInterrupt:
        print("Server stopped.", file=sys.stderr)
    except Exception as e:
        print(f"Server error: {e}", file=sys.stderr)
        return 1
    
    return 0


if __name__ == "__main__":
    main()