#!/usr/bin/env python3
"""
BV-BRC Sequence Feature Tools

This module contains MCP tools for querying sequence feature data from BV-BRC.
"""

import json
from typing import Optional

from flaskmcp import tool
from data_functions import (
    query_sequence_feature_by_id,
    query_sequence_feature_by_filters,
    query_sequence_feature_by_feature_id,
    query_sequence_feature_by_genome_id,
    query_sequence_feature_by_genome_name,
    query_sequence_feature_by_gene,
    query_sequence_feature_by_product,
    query_sequence_feature_by_patric_id,
    query_sequence_feature_by_genbank_accession,
    query_sequence_feature_by_refseq_locus_tag,
    query_sequence_feature_by_sf_category,
    query_sequence_feature_by_sf_id,
    query_sequence_feature_by_sf_name,
    query_sequence_feature_by_source,
    query_sequence_feature_by_source_id,
    query_sequence_feature_by_source_strain,
    query_sequence_feature_by_segment,
    query_sequence_feature_by_subtype,
    query_sequence_feature_by_taxon_id,
    query_sequence_feature_by_evidence_code,
    query_sequence_feature_by_aa_sequence_md5,
    query_sequence_feature_by_aa_variant,
    query_sequence_feature_by_sf_sequence_md5,
    query_sequence_feature_by_source_aa_sequence,
    query_sequence_feature_by_source_sf_location,
    query_sequence_feature_by_variant_types,
    query_sequence_feature_by_start,
    query_sequence_feature_by_end,
    query_sequence_feature_by_length,
    query_sequence_feature_by_position_range,
    query_sequence_feature_by_length_range,
    query_sequence_feature_by_date_range,
    query_sequence_feature_by_modified_date_range,
    query_sequence_feature_by_keyword,
    query_sequence_feature_all,
    format_query_result
)


def register_sequence_feature_tools(base_url: str, default_limit: int):
    """Register all sequence feature-related MCP tools with the Flask app."""
    
    @tool(name="bvbrc_sequence_feature_get_by_id", description="Get sequence feature data by ID. Parameters: id (str) - ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_sequence_feature_get_by_id(id: str, limit: int = default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by ID.
        
        Args:
            id: The ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sequence_feature_by_id(id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying sequence feature by ID: {str(e)}"


    @tool(name="bvbrc_sequence_feature_query_by_filters", description="Query sequence feature data by custom filters. Parameters: filters_json (str) - JSON string of filter criteria; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_sequence_feature_query_by_filters(filters_json: str, limit: int = default_limit,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query sequence feature data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
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
            result = query_sequence_feature_by_filters(filters, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying sequence feature by filters: {str(e)}"


    @tool(name="bvbrc_sequence_feature_get_by_genome_id", description="Get sequence feature data by genome ID. Parameters: genome_id (str) - genome ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_sequence_feature_get_by_genome_id(genome_id: str, limit: int = default_limit,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by genome ID.
        
        Args:
            genome_id: The genome ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sequence_feature_by_genome_id(genome_id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying sequence feature by genome ID: {str(e)}"


    @tool(name="bvbrc_sequence_feature_get_by_genome_name", description="Get sequence feature data by genome name. Parameters: genome_name (str) - genome name to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_sequence_feature_get_by_genome_name(genome_name: str, limit: int = default_limit,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by genome name.
        
        Args:
            genome_name: The genome name to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sequence_feature_by_genome_name(genome_name, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying sequence feature by genome name: {str(e)}"


    @tool(name="bvbrc_sequence_feature_get_by_gene", description="Get sequence feature data by gene. Parameters: gene (str) - gene to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_sequence_feature_get_by_gene(gene: str, limit: int = default_limit,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by gene.
        
        Args:
            gene: The gene to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sequence_feature_by_gene(gene, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying sequence feature by gene: {str(e)}"


    @tool(name="bvbrc_sequence_feature_get_by_taxon_id", description="Get sequence feature data by taxon ID. Parameters: taxon_id (int) - taxon ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_sequence_feature_get_by_taxon_id(taxon_id: int, limit: int = default_limit,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sequence_feature_by_taxon_id(taxon_id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying sequence feature by taxon ID: {str(e)}"


    @tool(name="bvbrc_sequence_feature_get_by_sf_category", description="Get sequence feature data by SF category. Parameters: sf_category (str) - SF category to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_sequence_feature_get_by_sf_category(sf_category: str, limit: int = default_limit,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by SF category.
        
        Args:
            sf_category: The SF category to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sequence_feature_by_sf_category(sf_category, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying sequence feature by SF category: {str(e)}"


    @tool(name="bvbrc_sequence_feature_get_by_position_range", description="Get sequence feature data by position range. Parameters: start (int) - start position; end (int) - end position; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_sequence_feature_get_by_position_range(start: int, end: int, limit: int = default_limit,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by position range.
        
        Args:
            start: Start position
            end: End position
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sequence_feature_by_position_range(start, end, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying sequence feature by position range: {str(e)}"


    @tool(name="bvbrc_sequence_feature_get_by_length_range", description="Get sequence feature data by length range. Parameters: min_length (int) - minimum length; max_length (int) - maximum length; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_sequence_feature_get_by_length_range(min_length: int, max_length: int, limit: int = default_limit,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by length range.
        
        Args:
            min_length: Minimum length
            max_length: Maximum length
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sequence_feature_by_length_range(min_length, max_length, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying sequence feature by length range: {str(e)}"


    @tool(name="bvbrc_sequence_feature_get_by_date_range", description="Get sequence feature data by date range. Parameters: start_date (str) - start date in YYYY-MM-DD format; end_date (str) - end date in YYYY-MM-DD format; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_sequence_feature_get_by_date_range(start_date: str, end_date: str, limit: int = default_limit,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sequence_feature_by_date_range(start_date, end_date, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying sequence feature by date range: {str(e)}"


    @tool(name="bvbrc_sequence_feature_search_by_keyword", description="Search sequence feature data by keyword. Parameters: keyword (str) - keyword to search for; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_sequence_feature_search_by_keyword(keyword: str, limit: int = default_limit,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search sequence feature data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sequence_feature_by_keyword(keyword, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching sequence feature by keyword: {str(e)}"


    @tool(name="bvbrc_sequence_feature_get_all", description="Get all sequence feature data. Parameters: limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_sequence_feature_get_all(limit: int = default_limit,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all sequence feature data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sequence_feature_all(options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all sequence feature data: {str(e)}"
