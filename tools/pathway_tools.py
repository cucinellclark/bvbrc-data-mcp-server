#!/usr/bin/env python3
"""
BV-BRC Pathway Tools

This module contains MCP tools for querying pathway data from BV-BRC.
"""

import json
from typing import Optional

from flaskmcp import tool
from data_functions import (
    query_pathway_by_id,
    query_pathway_by_filters,
    query_pathway_by_accession,
    query_pathway_by_alt_locus_tag,
    query_pathway_by_annotation,
    query_pathway_by_ec_description,
    query_pathway_by_ec_number,
    query_pathway_by_feature_id,
    query_pathway_by_gene,
    query_pathway_by_genome_ec,
    query_pathway_by_genome_id,
    query_pathway_by_genome_name,
    query_pathway_by_owner,
    query_pathway_by_pathway_class,
    query_pathway_by_pathway_ec,
    query_pathway_by_pathway_id,
    query_pathway_by_pathway_name,
    query_pathway_by_patric_id,
    query_pathway_by_product,
    query_pathway_by_public_status,
    query_pathway_by_refseq_locus_tag,
    query_pathway_by_sequence_id,
    query_pathway_by_taxon_id,
    query_pathway_by_user_read,
    query_pathway_by_user_write,
    query_pathway_by_version,
    query_pathway_by_date_inserted_range,
    query_pathway_by_date_modified_range,
    query_pathway_by_keyword,
    query_pathway_all,
    format_query_result
)


def register_pathway_tools(base_url: str, default_limit: int):
    """Register all pathway-related MCP tools with the Flask app."""
    
    @tool(name="bvbrc_pathway_get_by_id", description="Get pathway data by ID. Parameters: id (str) - ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_pathway_get_by_id(id: str, limit: int = default_limit,
                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by ID.
        
        Args:
            id: The ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_by_id(id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway by ID: {str(e)}"


    @tool(name="bvbrc_pathway_query_by_filters", description="Query pathway data by custom filters. Parameters: filters_json (str) - JSON string of filter criteria; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_pathway_query_by_filters(filters_json: str, limit: int = default_limit,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query pathway data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
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
            result = query_pathway_by_filters(filters, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway by filters: {str(e)}"


    @tool(name="bvbrc_pathway_get_by_genome_id", description="Get pathway data by genome ID. Parameters: genome_id (str) - genome ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_pathway_get_by_genome_id(genome_id: str, limit: int = default_limit,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by genome ID.
        
        Args:
            genome_id: The genome ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_by_genome_id(genome_id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway by genome ID: {str(e)}"


    @tool(name="bvbrc_pathway_get_by_genome_name", description="Get pathway data by genome name. Parameters: genome_name (str) - genome name to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_pathway_get_by_genome_name(genome_name: str, limit: int = default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by genome name.
        
        Args:
            genome_name: The genome name to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_by_genome_name(genome_name, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway by genome name: {str(e)}"


    @tool(name="bvbrc_pathway_get_by_pathway_id", description="Get pathway data by pathway ID. Parameters: pathway_id (str) - pathway ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_pathway_get_by_pathway_id(pathway_id: str, limit: int = default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by pathway ID.
        
        Args:
            pathway_id: The pathway ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_by_pathway_id(pathway_id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway by pathway ID: {str(e)}"


    @tool(name="bvbrc_pathway_get_by_pathway_name", description="Get pathway data by pathway name. Parameters: pathway_name (str) - pathway name to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_pathway_get_by_pathway_name(pathway_name: str, limit: int = default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by pathway name.
        
        Args:
            pathway_name: The pathway name to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_by_pathway_name(pathway_name, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway by pathway name: {str(e)}"


    @tool(name="bvbrc_pathway_get_by_ec_number", description="Get pathway data by EC number. Parameters: ec_number (str) - EC number to query (e.g., '1.1.1.1'); limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_pathway_get_by_ec_number(ec_number: str, limit: int = default_limit,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by EC number.
        
        Args:
            ec_number: The EC number to query (e.g., "1.1.1.1")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_by_ec_number(ec_number, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway by EC number: {str(e)}"


    @tool(name="bvbrc_pathway_get_by_gene", description="Get pathway data by gene. Parameters: gene (str) - gene to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_pathway_get_by_gene(gene: str, limit: int = default_limit,
                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by gene.
        
        Args:
            gene: The gene to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_by_gene(gene, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway by gene: {str(e)}"


    @tool(name="bvbrc_pathway_get_by_taxon_id", description="Get pathway data by taxon ID. Parameters: taxon_id (int) - taxon ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_pathway_get_by_taxon_id(taxon_id: int, limit: int = default_limit,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_by_taxon_id(taxon_id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway by taxon ID: {str(e)}"


    @tool(name="bvbrc_pathway_get_by_date_inserted_range", description="Get pathway data by date inserted range. Parameters: start_date (str) - start date in YYYY-MM-DD format; end_date (str) - end date in YYYY-MM-DD format; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_pathway_get_by_date_inserted_range(start_date: str, end_date: str, limit: int = default_limit,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_by_date_inserted_range(start_date, end_date, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway by date inserted range: {str(e)}"


    @tool(name="bvbrc_pathway_search_by_keyword", description="Search pathway data by keyword. Parameters: keyword (str) - keyword to search for; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_pathway_search_by_keyword(keyword: str, limit: int = default_limit,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search pathway data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_by_keyword(keyword, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching pathway by keyword: {str(e)}"


    @tool(name="bvbrc_pathway_get_all", description="Get all pathway data. Parameters: limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_pathway_get_all(limit: int = default_limit,
                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all pathway data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_all(options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all pathway data: {str(e)}"
