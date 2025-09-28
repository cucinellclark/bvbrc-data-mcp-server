#!/usr/bin/env python3
"""
BV-BRC SP Gene Reference Tools

This module contains MCP tools for querying SP gene reference data from BV-BRC.
"""

import json
from typing import Optional

from flaskmcp import tool
from data_functions import (
    query_sp_gene_ref_by_id,
    query_sp_gene_ref_by_filters,
    query_sp_gene_ref_by_antibiotics,
    query_sp_gene_ref_by_gene_symbol,
    query_sp_gene_ref_by_source,
    query_sp_gene_ref_by_taxon_id,
    query_sp_gene_ref_by_date_inserted_range,
    query_sp_gene_ref_by_date_modified_range,
    query_sp_gene_ref_by_keyword,
    query_sp_gene_ref_all,
    format_query_result
)


def register_sp_gene_ref_tools(base_url: str, default_limit: int):
    """Register all SP gene reference-related MCP tools with the Flask app."""
    
    @tool(name="bvbrc_sp_gene_ref_get_by_id", description="Get SP gene reference data by ID. Parameters: id (str) - ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_sp_gene_ref_get_by_id(id: str, limit: int = default_limit,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get SP gene reference data by ID.
        
        Args:
            id: The ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted SP gene reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sp_gene_ref_by_id(id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying SP gene reference by ID: {str(e)}"


    @tool(name="bvbrc_sp_gene_ref_query_by_filters", description="Query SP gene reference data by custom filters. Parameters: filters_json (str) - JSON string of filter criteria; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_sp_gene_ref_query_by_filters(filters_json: str, limit: int = default_limit,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query SP gene reference data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted SP gene reference data
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
            result = query_sp_gene_ref_by_filters(filters, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying SP gene reference by filters: {str(e)}"


    @tool(name="bvbrc_sp_gene_ref_get_by_antibiotics", description="Get SP gene reference data by antibiotics. Parameters: antibiotics (str) - antibiotics to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_sp_gene_ref_get_by_antibiotics(antibiotics: str, limit: int = default_limit,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get SP gene reference data by antibiotics.
        
        Args:
            antibiotics: The antibiotics to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted SP gene reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sp_gene_ref_by_antibiotics(antibiotics, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying SP gene reference by antibiotics: {str(e)}"


    @tool(name="bvbrc_sp_gene_ref_get_by_gene_symbol", description="Get SP gene reference data by gene symbol. Parameters: gene_symbol (str) - gene symbol to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_sp_gene_ref_get_by_gene_symbol(gene_symbol: str, limit: int = default_limit,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get SP gene reference data by gene symbol.
        
        Args:
            gene_symbol: The gene symbol to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted SP gene reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sp_gene_ref_by_gene_symbol(gene_symbol, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying SP gene reference by gene symbol: {str(e)}"


    @tool(name="bvbrc_sp_gene_ref_get_by_taxon_id", description="Get SP gene reference data by taxon ID. Parameters: taxon_id (int) - taxon ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_sp_gene_ref_get_by_taxon_id(taxon_id: int, limit: int = default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get SP gene reference data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted SP gene reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sp_gene_ref_by_taxon_id(taxon_id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying SP gene reference by taxon ID: {str(e)}"


    @tool(name="bvbrc_sp_gene_ref_get_by_date_inserted_range", description="Get SP gene reference data by date inserted range. Parameters: start_date (str) - start date in YYYY-MM-DD format; end_date (str) - end date in YYYY-MM-DD format; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_sp_gene_ref_get_by_date_inserted_range(start_date: str, end_date: str, limit: int = default_limit,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get SP gene reference data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted SP gene reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sp_gene_ref_by_date_inserted_range(start_date, end_date, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying SP gene reference by date inserted range: {str(e)}"


    @tool(name="bvbrc_sp_gene_ref_search_by_keyword", description="Search SP gene reference data by keyword. Parameters: keyword (str) - keyword to search for; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_sp_gene_ref_search_by_keyword(keyword: str, limit: int = default_limit,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search SP gene reference data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted SP gene reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sp_gene_ref_by_keyword(keyword, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching SP gene reference by keyword: {str(e)}"


    @tool(name="bvbrc_sp_gene_ref_get_all", description="Get all SP gene reference data. Parameters: limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_sp_gene_ref_get_all(limit: int = default_limit,
                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all SP gene reference data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted SP gene reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sp_gene_ref_all(options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all SP gene reference data: {str(e)}"
