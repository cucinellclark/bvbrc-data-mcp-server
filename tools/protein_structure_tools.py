#!/usr/bin/env python3
"""
BV-BRC Protein Structure Tools

This module contains MCP tools for querying protein structure data from BV-BRC.
"""

import json
from typing import Optional

from flaskmcp import tool
from data_functions import (
    query_protein_structure_by_id,
    query_protein_structure_by_filters,
    query_protein_structure_by_feature_id,
    query_protein_structure_by_genome_id,
    query_protein_structure_by_patric_id,
    query_protein_structure_by_organism_name,
    query_protein_structure_by_title,
    query_protein_structure_by_resolution,
    query_protein_structure_by_institution,
    query_protein_structure_by_file_path,
    query_protein_structure_by_author,
    query_protein_structure_by_method,
    query_protein_structure_by_gene,
    query_protein_structure_by_product,
    query_protein_structure_by_sequence,
    query_protein_structure_by_sequence_md5,
    query_protein_structure_by_uniprotkb_accession,
    query_protein_structure_by_pmid,
    query_protein_structure_by_taxon_id,
    query_protein_structure_by_taxon_lineage_id,
    query_protein_structure_by_taxon_lineage_name,
    query_protein_structure_by_alignment,
    query_protein_structure_by_release_date_range,
    query_protein_structure_by_date_inserted_range,
    query_protein_structure_by_date_modified_range,
    query_protein_structure_by_keyword,
    query_protein_structure_all,
    format_query_result
)


def register_protein_structure_tools(base_url: str, default_limit: int):
    """Register all protein structure-related MCP tools with the Flask app."""
    
    @tool(name="bvbrc_protein_structure_get_by_id", description="Get protein structure data by PDB ID. Parameters: pdb_id (str) - PDB ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_protein_structure_get_by_id(pdb_id: str, limit: int = default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by PDB ID.
        
        Args:
            pdb_id: The PDB ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_structure_by_id(pdb_id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein structure by PDB ID: {str(e)}"


    @tool(name="bvbrc_protein_structure_query_by_filters", description="Query protein structure data by custom filters. Parameters: filters_json (str) - JSON string of filter criteria; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_protein_structure_query_by_filters(filters_json: str, limit: int = default_limit,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query protein structure data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        try:
            filters = json.loads(filters_json)
        except json.JSONDecodeError as e:
            return f"Error parsing filters JSON: {str(e)}"
        
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_structure_by_filters(filters, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein structure by filters: {str(e)}"


    @tool(name="bvbrc_protein_structure_get_by_feature_id", description="Get protein structure data by feature ID. Parameters: feature_id (str) - feature ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_protein_structure_get_by_feature_id(feature_id: str, limit: int = default_limit,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by feature ID.
        
        Args:
            feature_id: The feature ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_structure_by_feature_id(feature_id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein structure by feature ID: {str(e)}"


    @tool(name="bvbrc_protein_structure_get_by_genome_id", description="Get protein structure data by genome ID. Parameters: genome_id (str) - genome ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_protein_structure_get_by_genome_id(genome_id: str, limit: int = default_limit,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by genome ID.
        
        Args:
            genome_id: The genome ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_structure_by_genome_id(genome_id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein structure by genome ID: {str(e)}"


    @tool(name="bvbrc_protein_structure_get_by_organism_name", description="Get protein structure data by organism name. Parameters: organism_name (str) - organism name to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_protein_structure_get_by_organism_name(organism_name: str, limit: int = default_limit,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by organism name.
        
        Args:
            organism_name: The organism name to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_structure_by_organism_name(organism_name, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein structure by organism name: {str(e)}"


    @tool(name="bvbrc_protein_structure_get_by_title", description="Get protein structure data by title. Parameters: title (str) - title to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_protein_structure_get_by_title(title: str, limit: int = default_limit,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by title.
        
        Args:
            title: The title to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_structure_by_title(title, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein structure by title: {str(e)}"


    @tool(name="bvbrc_protein_structure_get_by_resolution", description="Get protein structure data by resolution. Parameters: resolution (str) - resolution to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_protein_structure_get_by_resolution(resolution: str, limit: int = default_limit,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by resolution.
        
        Args:
            resolution: The resolution to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_structure_by_resolution(resolution, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein structure by resolution: {str(e)}"


    @tool(name="bvbrc_protein_structure_get_by_taxon_id", description="Get protein structure data by taxon ID. Parameters: taxon_id (int) - taxon ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_protein_structure_get_by_taxon_id(taxon_id: int, limit: int = default_limit,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_structure_by_taxon_id(taxon_id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein structure by taxon ID: {str(e)}"


    @tool(name="bvbrc_protein_structure_get_by_pmid", description="Get protein structure data by PMID. Parameters: pmid (str) - PMID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_protein_structure_get_by_pmid(pmid: str, limit: int = default_limit,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by PMID.
        
        Args:
            pmid: The PMID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_structure_by_pmid(pmid, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein structure by PMID: {str(e)}"


    @tool(name="bvbrc_protein_structure_get_by_release_date_range", description="Get protein structure data by release date range. Parameters: start_date (str) - start date in YYYY-MM-DD format; end_date (str) - end date in YYYY-MM-DD format; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_protein_structure_get_by_release_date_range(start_date: str, end_date: str, limit: int = default_limit,
                                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by release date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_structure_by_release_date_range(start_date, end_date, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein structure by release date range: {str(e)}"


    @tool(name="bvbrc_protein_structure_search_by_keyword", description="Search protein structure data by keyword. Parameters: keyword (str) - keyword to search for; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_protein_structure_search_by_keyword(keyword: str, limit: int = default_limit,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search protein structure data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_structure_by_keyword(keyword, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching protein structure by keyword: {str(e)}"


    @tool(name="bvbrc_protein_structure_get_all", description="Get all protein structure data. Parameters: limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_protein_structure_get_all(limit: int = default_limit,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all protein structure data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_structure_all(options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all protein structure data: {str(e)}"
