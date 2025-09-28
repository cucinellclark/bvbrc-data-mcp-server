#!/usr/bin/env python3
"""
BV-BRC Genome Sequence Tools

This module contains MCP tools for querying genome sequence data from BV-BRC.
"""

import json
from typing import Optional

from flaskmcp import tool
from data_functions import (
    query_genome_sequence_by_id,
    query_genome_sequence_by_filters,
    query_genome_sequence_by_accession,
    query_genome_sequence_by_chromosome,
    query_genome_sequence_by_description,
    query_genome_sequence_by_gc_content,
    query_genome_sequence_by_genome_id,
    query_genome_sequence_by_genome_name,
    query_genome_sequence_by_gi,
    query_genome_sequence_by_length,
    query_genome_sequence_by_mol_type,
    query_genome_sequence_by_owner,
    query_genome_sequence_by_p2_sequence_id,
    query_genome_sequence_by_plasmid,
    query_genome_sequence_by_public_status,
    query_genome_sequence_by_segment,
    query_genome_sequence_by_sequence_md5,
    query_genome_sequence_by_sequence_status,
    query_genome_sequence_by_sequence_type,
    query_genome_sequence_by_taxon_id,
    query_genome_sequence_by_topology,
    query_genome_sequence_by_version,
    query_genome_sequence_by_length_range,
    query_genome_sequence_by_gc_content_range,
    query_genome_sequence_by_date_inserted_range,
    query_genome_sequence_by_date_modified_range,
    query_genome_sequence_by_release_date_range,
    query_genome_sequence_by_keyword,
    query_genome_sequence_all,
    format_query_result
)


def register_genome_sequence_tools(base_url: str, default_limit: int):
    """Register all genome sequence-related MCP tools with the Flask app."""
    
    @tool(name="bvbrc_genome_sequence_get_by_id", description="Get genome sequence data by sequence ID. Parameters: sequence_id (str) - sequence ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_sequence_get_by_id(sequence_id: str, limit: int = default_limit,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by sequence ID.
        
        Args:
            sequence_id: The sequence ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_sequence_by_id(sequence_id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome sequence by ID: {str(e)}"


    @tool(name="bvbrc_genome_sequence_query_by_filters", description="Query genome sequence data by custom filters. Parameters: filters_json (str) - JSON string of filter criteria; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_sequence_query_by_filters(filters_json: str, limit: int = default_limit,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query genome sequence data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
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
            result = query_genome_sequence_by_filters(filters, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome sequence by filters: {str(e)}"


    @tool(name="bvbrc_genome_sequence_get_by_accession", description="Get genome sequence data by accession. Parameters: accession (str) - accession to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_sequence_get_by_accession(accession: str, limit: int = default_limit,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by accession.
        
        Args:
            accession: The accession to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_sequence_by_accession(accession, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome sequence by accession: {str(e)}"


    @tool(name="bvbrc_genome_sequence_get_by_genome_id", description="Get genome sequence data by genome ID. Parameters: genome_id (str) - genome ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_sequence_get_by_genome_id(genome_id: str, limit: int = default_limit,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by genome ID.
        
        Args:
            genome_id: The genome ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_sequence_by_genome_id(genome_id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome sequence by genome ID: {str(e)}"


    @tool(name="bvbrc_genome_sequence_get_by_genome_name", description="Get genome sequence data by genome name. Parameters: genome_name (str) - genome name to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_sequence_get_by_genome_name(genome_name: str, limit: int = default_limit,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by genome name.
        
        Args:
            genome_name: The genome name to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_sequence_by_genome_name(genome_name, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome sequence by genome name: {str(e)}"


    @tool(name="bvbrc_genome_sequence_get_by_length", description="Get genome sequence data by length. Parameters: length (int) - length to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_sequence_get_by_length(length: int, limit: int = default_limit,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by length.
        
        Args:
            length: The length to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_sequence_by_length(length, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome sequence by length: {str(e)}"


    @tool(name="bvbrc_genome_sequence_get_by_gc_content", description="Get genome sequence data by GC content. Parameters: gc_content (float) - GC content to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_sequence_get_by_gc_content(gc_content: float, limit: int = default_limit,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by GC content.
        
        Args:
            gc_content: The GC content to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_sequence_by_gc_content(gc_content, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome sequence by GC content: {str(e)}"


    @tool(name="bvbrc_genome_sequence_get_by_sequence_type", description="Get genome sequence data by sequence type. Parameters: sequence_type (str) - sequence type to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_sequence_get_by_sequence_type(sequence_type: str, limit: int = default_limit,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by sequence type.
        
        Args:
            sequence_type: The sequence type to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_sequence_by_sequence_type(sequence_type, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome sequence by sequence type: {str(e)}"


    @tool(name="bvbrc_genome_sequence_get_by_taxon_id", description="Get genome sequence data by taxon ID. Parameters: taxon_id (int) - taxon ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_sequence_get_by_taxon_id(taxon_id: int, limit: int = default_limit,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_sequence_by_taxon_id(taxon_id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome sequence by taxon ID: {str(e)}"


    @tool(name="bvbrc_genome_sequence_get_by_length_range", description="Get genome sequence data by length range. Parameters: min_length (int) - minimum length; max_length (int) - maximum length; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_sequence_get_by_length_range(min_length: int, max_length: int, limit: int = default_limit,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by length range.
        
        Args:
            min_length: Minimum length
            max_length: Maximum length
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_sequence_by_length_range(min_length, max_length, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome sequence by length range: {str(e)}"


    @tool(name="bvbrc_genome_sequence_get_by_gc_content_range", description="Get genome sequence data by GC content range. Parameters: min_gc_content (float) - minimum GC content; max_gc_content (float) - maximum GC content; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_sequence_get_by_gc_content_range(min_gc_content: float, max_gc_content: float, limit: int = default_limit,
                                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by GC content range.
        
        Args:
            min_gc_content: Minimum GC content
            max_gc_content: Maximum GC content
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_sequence_by_gc_content_range(min_gc_content, max_gc_content, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome sequence by GC content range: {str(e)}"


    @tool(name="bvbrc_genome_sequence_get_by_date_inserted_range", description="Get genome sequence data by date inserted range. Parameters: start_date (str) - start date in YYYY-MM-DD format; end_date (str) - end date in YYYY-MM-DD format; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_sequence_get_by_date_inserted_range(start_date: str, end_date: str, limit: int = default_limit,
                                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_sequence_by_date_inserted_range(start_date, end_date, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome sequence by date inserted range: {str(e)}"


    @tool(name="bvbrc_genome_sequence_search_by_keyword", description="Search genome sequence data by keyword. Parameters: keyword (str) - keyword to search for; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_sequence_search_by_keyword(keyword: str, limit: int = default_limit,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search genome sequence data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_sequence_by_keyword(keyword, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching genome sequence by keyword: {str(e)}"


    @tool(name="bvbrc_genome_sequence_get_all", description="Get all genome sequence data. Parameters: limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_sequence_get_all(limit: int = default_limit,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all genome sequence data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_sequence_all(options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all genome sequence data: {str(e)}"
