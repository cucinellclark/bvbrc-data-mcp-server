#!/usr/bin/env python3
"""
BV-BRC Serology Tools

This module contains MCP tools for querying serology data from BV-BRC.
"""

import json
from typing import Optional

from flaskmcp import tool
from data_functions import (
    query_serology_by_id,
    query_serology_by_filters,
    query_serology_by_collection_city,
    query_serology_by_collection_country,
    query_serology_by_collection_state,
    query_serology_by_collection_year,
    query_serology_by_host_species,
    query_serology_by_host_type,
    query_serology_by_serotype,
    query_serology_by_strain,
    query_serology_by_test_type,
    query_serology_by_test_result,
    query_serology_by_test_interpretation,
    query_serology_by_test_pathogen,
    query_serology_by_test_antigen,
    query_serology_by_sample_accession,
    query_serology_by_sample_identifier,
    query_serology_by_virus_identifier,
    query_serology_by_project_identifier,
    query_serology_by_contributing_institution,
    query_serology_by_geographic_group,
    query_serology_by_host_common_name,
    query_serology_by_host_health,
    query_serology_by_host_identifier,
    query_serology_by_host_sex,
    query_serology_by_host_age,
    query_serology_by_host_age_group,
    query_serology_by_positive_definition,
    query_serology_by_taxon_lineage_id,
    query_serology_by_collection_date_range,
    query_serology_by_date_inserted_range,
    query_serology_by_date_modified_range,
    query_serology_by_keyword,
    query_serology_all,
    format_query_result
)


def register_serology_tools(base_url: str, default_limit: int):
    """Register all serology-related MCP tools with the Flask app."""
    
    @tool(name="bvbrc_serology_get_by_id", description="Get serology data by ID. Parameters: id (str) - ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_serology_get_by_id(id: str, limit: int = default_limit,
                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by ID.
        
        Args:
            id: The ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_serology_by_id(id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying serology by ID: {str(e)}"


    @tool(name="bvbrc_serology_query_by_filters", description="Query serology data by custom filters. Parameters: filters_json (str) - JSON string of filter criteria; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_serology_query_by_filters(filters_json: str, limit: int = default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query serology data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
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
            result = query_serology_by_filters(filters, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying serology by filters: {str(e)}"


    @tool(name="bvbrc_serology_get_by_collection_country", description="Get serology data by collection country. Parameters: collection_country (str) - collection country to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_serology_get_by_collection_country(collection_country: str, limit: int = default_limit,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by collection country.
        
        Args:
            collection_country: The collection country to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_serology_by_collection_country(collection_country, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying serology by collection country: {str(e)}"


    @tool(name="bvbrc_serology_get_by_host_species", description="Get serology data by host species. Parameters: host_species (str) - host species to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_serology_get_by_host_species(host_species: str, limit: int = default_limit,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by host species.
        
        Args:
            host_species: The host species to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_serology_by_host_species(host_species, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying serology by host species: {str(e)}"


    @tool(name="bvbrc_serology_get_by_serotype", description="Get serology data by serotype. Parameters: serotype (str) - serotype to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_serology_get_by_serotype(serotype: str, limit: int = default_limit,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by serotype.
        
        Args:
            serotype: The serotype to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_serology_by_serotype(serotype, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying serology by serotype: {str(e)}"


    @tool(name="bvbrc_serology_get_by_test_type", description="Get serology data by test type. Parameters: test_type (str) - test type to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_serology_get_by_test_type(test_type: str, limit: int = default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by test type.
        
        Args:
            test_type: The test type to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_serology_by_test_type(test_type, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying serology by test type: {str(e)}"


    @tool(name="bvbrc_serology_get_by_test_result", description="Get serology data by test result. Parameters: test_result (str) - test result to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_serology_get_by_test_result(test_result: str, limit: int = default_limit,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by test result.
        
        Args:
            test_result: The test result to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_serology_by_test_result(test_result, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying serology by test result: {str(e)}"


    @tool(name="bvbrc_serology_get_by_collection_date_range", description="Get serology data by collection date range. Parameters: start_date (str) - start date in YYYY-MM-DD format; end_date (str) - end date in YYYY-MM-DD format; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_serology_get_by_collection_date_range(start_date: str, end_date: str, limit: int = default_limit,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by collection date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_serology_by_collection_date_range(start_date, end_date, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying serology by collection date range: {str(e)}"


    @tool(name="bvbrc_serology_search_by_keyword", description="Search serology data by keyword. Parameters: keyword (str) - keyword to search for; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_serology_search_by_keyword(keyword: str, limit: int = default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search serology data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_serology_by_keyword(keyword, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching serology by keyword: {str(e)}"


    @tool(name="bvbrc_serology_get_all", description="Get all serology data. Parameters: limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_serology_get_all(limit: int = default_limit,
                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all serology data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_serology_all(options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all serology data: {str(e)}"
