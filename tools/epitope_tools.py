#!/usr/bin/env python3
"""
BV-BRC Epitope Tools

This module contains MCP tools for querying epitope data from BV-BRC.
"""

import json
from typing import Optional

from flaskmcp import tool
from data_functions import (
    query_epitope_by_id,
    query_epitope_by_filters,
    query_epitope_by_epitope_sequence,
    query_epitope_by_epitope_type,
    query_epitope_by_host_name,
    query_epitope_by_organism,
    query_epitope_by_protein_accession,
    query_epitope_by_protein_id,
    query_epitope_by_protein_name,
    query_epitope_by_start,
    query_epitope_by_end,
    query_epitope_by_taxon_id,
    query_epitope_by_bcell_assays,
    query_epitope_by_mhc_assays,
    query_epitope_by_tcell_assays,
    query_epitope_by_total_assays,
    query_epitope_by_comment,
    query_epitope_by_assay_result,
    query_epitope_by_taxon_lineage_id,
    query_epitope_by_taxon_lineage_name,
    query_epitope_by_position_range,
    query_epitope_by_total_assays_range,
    query_epitope_by_date_inserted_range,
    query_epitope_by_date_modified_range,
    query_epitope_by_keyword,
    query_epitope_all,
    format_query_result
)


def register_epitope_tools(base_url: str, default_limit: int):
    """Register all epitope-related MCP tools with the Flask app."""
    
    @tool(name="bvbrc_epitope_get_by_id", description="Get epitope data by epitope ID. Parameters: epitope_id (str) - epitope ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_epitope_get_by_id(epitope_id: str, limit: int = default_limit,
                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by epitope ID.
        
        Args:
            epitope_id: The epitope ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_by_id(epitope_id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope by ID: {str(e)}"


    @tool(name="bvbrc_epitope_query_by_filters", description="Query epitope data by custom filters. Parameters: filters_json (str) - JSON string of filter criteria; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_epitope_query_by_filters(filters_json: str, limit: int = default_limit,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query epitope data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
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
            result = query_epitope_by_filters(filters, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope by filters: {str(e)}"


    @tool(name="bvbrc_epitope_get_by_epitope_sequence", description="Get epitope data by epitope sequence. Parameters: epitope_sequence (str) - epitope sequence to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_epitope_get_by_epitope_sequence(epitope_sequence: str, limit: int = default_limit,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by epitope sequence.
        
        Args:
            epitope_sequence: The epitope sequence to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_by_epitope_sequence(epitope_sequence, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope by epitope sequence: {str(e)}"


    @tool(name="bvbrc_epitope_get_by_epitope_type", description="Get epitope data by epitope type. Parameters: epitope_type (str) - epitope type to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_epitope_get_by_epitope_type(epitope_type: str, limit: int = default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by epitope type.
        
        Args:
            epitope_type: The epitope type to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_by_epitope_type(epitope_type, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope by epitope type: {str(e)}"


    @tool(name="bvbrc_epitope_get_by_organism", description="Get epitope data by organism. Parameters: organism (str) - organism to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_epitope_get_by_organism(organism: str, limit: int = default_limit,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by organism.
        
        Args:
            organism: The organism to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_by_organism(organism, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope by organism: {str(e)}"


    @tool(name="bvbrc_epitope_get_by_protein_accession", description="Get epitope data by protein accession. Parameters: protein_accession (str) - protein accession to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_epitope_get_by_protein_accession(protein_accession: str, limit: int = default_limit,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by protein accession.
        
        Args:
            protein_accession: The protein accession to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_by_protein_accession(protein_accession, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope by protein accession: {str(e)}"


    @tool(name="bvbrc_epitope_get_by_protein_name", description="Get epitope data by protein name. Parameters: protein_name (str) - protein name to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_epitope_get_by_protein_name(protein_name: str, limit: int = default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by protein name.
        
        Args:
            protein_name: The protein name to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_by_protein_name(protein_name, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope by protein name: {str(e)}"


    @tool(name="bvbrc_epitope_get_by_taxon_id", description="Get epitope data by taxon ID. Parameters: taxon_id (int) - taxon ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_epitope_get_by_taxon_id(taxon_id: int, limit: int = default_limit,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_by_taxon_id(taxon_id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope by taxon ID: {str(e)}"


    @tool(name="bvbrc_epitope_get_by_total_assays", description="Get epitope data by total assays. Parameters: total_assays (int) - total assays to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_epitope_get_by_total_assays(total_assays: int, limit: int = default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by total assays.
        
        Args:
            total_assays: The total assays to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_by_total_assays(total_assays, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope by total assays: {str(e)}"


    @tool(name="bvbrc_epitope_get_by_position_range", description="Get epitope data by position range. Parameters: min_start (int) - minimum start position; max_end (int) - maximum end position; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_epitope_get_by_position_range(min_start: int, max_end: int, limit: int = default_limit,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by position range.
        
        Args:
            min_start: Minimum start position
            max_end: Maximum end position
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_by_position_range(min_start, max_end, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope by position range: {str(e)}"


    @tool(name="bvbrc_epitope_get_by_total_assays_range", description="Get epitope data by total assays range. Parameters: min_assays (int) - minimum total assays; max_assays (int) - maximum total assays; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_epitope_get_by_total_assays_range(min_assays: int, max_assays: int, limit: int = default_limit,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by total assays range.
        
        Args:
            min_assays: Minimum total assays
            max_assays: Maximum total assays
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_by_total_assays_range(min_assays, max_assays, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope by total assays range: {str(e)}"


    @tool(name="bvbrc_epitope_get_by_date_inserted_range", description="Get epitope data by date inserted range. Parameters: start_date (str) - start date in YYYY-MM-DD format; end_date (str) - end date in YYYY-MM-DD format; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_epitope_get_by_date_inserted_range(start_date: str, end_date: str, limit: int = default_limit,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_by_date_inserted_range(start_date, end_date, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope by date inserted range: {str(e)}"


    @tool(name="bvbrc_epitope_search_by_keyword", description="Search epitope data by keyword. Parameters: keyword (str) - keyword to search for; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_epitope_search_by_keyword(keyword: str, limit: int = default_limit,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search epitope data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_by_keyword(keyword, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching epitope by keyword: {str(e)}"


    @tool(name="bvbrc_epitope_get_all", description="Get all epitope data. Parameters: limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_epitope_get_all(limit: int = default_limit,
                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all epitope data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_all(options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all epitope data: {str(e)}"
