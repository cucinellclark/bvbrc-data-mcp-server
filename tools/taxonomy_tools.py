#!/usr/bin/env python3
"""
BV-BRC Taxonomy Tools

This module contains MCP tools for querying taxonomy data from BV-BRC.
"""

import json
from typing import Optional

from flaskmcp import tool
from data_functions import (
    query_taxonomy_by_id,
    query_taxonomy_by_filters,
    query_taxonomy_by_taxon_name,
    query_taxonomy_by_taxon_rank,
    query_taxonomy_by_lineage,
    query_taxonomy_by_lineage_ids,
    query_taxonomy_by_lineage_names,
    query_taxonomy_by_parent_id,
    query_taxonomy_by_division,
    query_taxonomy_by_genetic_code,
    query_taxonomy_by_genome_count,
    query_taxonomy_by_core_families,
    query_taxonomy_by_cds_mean,
    query_taxonomy_by_genome_length_mean,
    query_taxonomy_by_cds_mean_range,
    query_taxonomy_by_core_families_range,
    query_taxonomy_by_genetic_code_range,
    query_taxonomy_by_genome_count_range,
    query_taxonomy_by_genome_length_mean_range,
    query_taxonomy_by_parent_id_range,
    query_taxonomy_by_keyword,
    query_taxonomy_all,
    format_query_result
)


def register_taxonomy_tools(base_url: str, default_limit: int):
    """Register all taxonomy-related MCP tools with the Flask app."""
    
    @tool(name="bvbrc_taxonomy_get_by_id", description="Get taxonomy data by taxon ID. Parameters: taxon_id (str) - taxon ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_taxonomy_get_by_id(taxon_id: str, limit: int = default_limit,
                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get taxonomy data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted taxonomy data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_taxonomy_by_id(taxon_id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying taxonomy by taxon ID: {str(e)}"


    @tool(name="bvbrc_taxonomy_query_by_filters", description="Query taxonomy data by custom filters. Parameters: filters_json (str) - JSON string of filter criteria; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_taxonomy_query_by_filters(filters_json: str, limit: int = default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query taxonomy data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted taxonomy data
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
            result = query_taxonomy_by_filters(filters, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying taxonomy by filters: {str(e)}"


    @tool(name="bvbrc_taxonomy_get_by_taxon_name", description="Get taxonomy data by taxon name. Parameters: taxon_name (str) - taxon name to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_taxonomy_get_by_taxon_name(taxon_name: str, limit: int = default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get taxonomy data by taxon name.
        
        Args:
            taxon_name: The taxon name to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted taxonomy data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_taxonomy_by_taxon_name(taxon_name, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying taxonomy by taxon name: {str(e)}"


    @tool(name="bvbrc_taxonomy_get_by_taxon_rank", description="Get taxonomy data by taxon rank. Parameters: taxon_rank (str) - taxon rank to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_taxonomy_get_by_taxon_rank(taxon_rank: str, limit: int = default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get taxonomy data by taxon rank.
        
        Args:
            taxon_rank: The taxon rank to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted taxonomy data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_taxonomy_by_taxon_rank(taxon_rank, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying taxonomy by taxon rank: {str(e)}"


    @tool(name="bvbrc_taxonomy_get_by_lineage", description="Get taxonomy data by lineage. Parameters: lineage (str) - lineage to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_taxonomy_get_by_lineage(lineage: str, limit: int = default_limit,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get taxonomy data by lineage.
        
        Args:
            lineage: The lineage to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted taxonomy data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_taxonomy_by_lineage(lineage, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying taxonomy by lineage: {str(e)}"


    @tool(name="bvbrc_taxonomy_get_by_division", description="Get taxonomy data by division. Parameters: division (str) - division to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_taxonomy_get_by_division(division: str, limit: int = default_limit,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get taxonomy data by division.
        
        Args:
            division: The division to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted taxonomy data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_taxonomy_by_division(division, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying taxonomy by division: {str(e)}"


    @tool(name="bvbrc_taxonomy_get_by_genetic_code", description="Get taxonomy data by genetic code. Parameters: genetic_code (int) - genetic code to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_taxonomy_get_by_genetic_code(genetic_code: int, limit: int = default_limit,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get taxonomy data by genetic code.
        
        Args:
            genetic_code: The genetic code to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted taxonomy data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_taxonomy_by_genetic_code(genetic_code, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying taxonomy by genetic code: {str(e)}"


    @tool(name="bvbrc_taxonomy_get_by_genome_count", description="Get taxonomy data by genome count. Parameters: genome_count (int) - genome count to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_taxonomy_get_by_genome_count(genome_count: int, limit: int = default_limit,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get taxonomy data by genome count.
        
        Args:
            genome_count: The genome count to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted taxonomy data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_taxonomy_by_genome_count(genome_count, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying taxonomy by genome count: {str(e)}"


    @tool(name="bvbrc_taxonomy_get_by_cds_mean_range", description="Get taxonomy data by CDS mean range. Parameters: min_cds_mean (float) - minimum CDS mean; max_cds_mean (float) - maximum CDS mean; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_taxonomy_get_by_cds_mean_range(min_cds_mean: float, max_cds_mean: float, limit: int = default_limit,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get taxonomy data by CDS mean range.
        
        Args:
            min_cds_mean: Minimum CDS mean
            max_cds_mean: Maximum CDS mean
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted taxonomy data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_taxonomy_by_cds_mean_range(min_cds_mean, max_cds_mean, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying taxonomy by CDS mean range: {str(e)}"


    @tool(name="bvbrc_taxonomy_get_by_genome_count_range", description="Get taxonomy data by genome count range. Parameters: min_genome_count (int) - minimum genome count; max_genome_count (int) - maximum genome count; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_taxonomy_get_by_genome_count_range(min_genome_count: int, max_genome_count: int, limit: int = default_limit,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get taxonomy data by genome count range.
        
        Args:
            min_genome_count: Minimum genome count
            max_genome_count: Maximum genome count
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted taxonomy data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_taxonomy_by_genome_count_range(min_genome_count, max_genome_count, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying taxonomy by genome count range: {str(e)}"


    @tool(name="bvbrc_taxonomy_search_by_keyword", description="Search taxonomy data by keyword. Parameters: keyword (str) - keyword to search for; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_taxonomy_search_by_keyword(keyword: str, limit: int = default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search taxonomy data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted taxonomy data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_taxonomy_by_keyword(keyword, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching taxonomy by keyword: {str(e)}"


    @tool(name="bvbrc_taxonomy_get_all", description="Get all taxonomy data. Parameters: limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_taxonomy_get_all(limit: int = default_limit,
                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all taxonomy data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted taxonomy data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_taxonomy_all(options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all taxonomy data: {str(e)}"
