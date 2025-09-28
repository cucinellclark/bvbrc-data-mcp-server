#!/usr/bin/env python3
"""
BV-BRC Surveillance Tools

This module contains MCP tools for querying surveillance data from BV-BRC.
"""

import json
from typing import Optional

from flaskmcp import tool
from data_functions import (
    query_surveillance_by_id,
    query_surveillance_by_filters,
    query_surveillance_by_host_species,
    query_surveillance_by_host_common_name,
    query_surveillance_by_sample_identifier,
    query_surveillance_by_sample_accession,
    query_surveillance_by_collection_country,
    query_surveillance_by_collection_city,
    query_surveillance_by_collection_year,
    query_surveillance_by_species,
    query_surveillance_by_strain,
    query_surveillance_by_subtype,
    query_surveillance_by_pathogen_type,
    query_surveillance_by_genome_id,
    query_surveillance_by_disease_status,
    query_surveillance_by_diagnosis,
    query_surveillance_by_treatment,
    query_surveillance_by_hospitalized,
    query_surveillance_by_vaccination_type,
    query_surveillance_by_exposure,
    query_surveillance_by_pathogen_test_type,
    query_surveillance_by_pathogen_test_result,
    query_surveillance_by_collection_date_range,
    query_surveillance_by_date_inserted_range,
    query_surveillance_by_date_modified_range,
    query_surveillance_by_keyword,
    query_surveillance_all,
    format_query_result
)


def register_surveillance_tools(base_url: str, default_limit: int):
    """Register all surveillance-related MCP tools with the Flask app."""
    
    @tool(name="bvbrc_surveillance_get_by_id", description="Get surveillance data by ID. Parameters: id (str) - ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_surveillance_get_by_id(id: str, limit: int = default_limit,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get surveillance data by ID.
        
        Args:
            id: The ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted surveillance data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_surveillance_by_id(id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying surveillance by ID: {str(e)}"


    @tool(name="bvbrc_surveillance_query_by_filters", description="Query surveillance data by custom filters. Parameters: filters_json (str) - JSON string of filter criteria; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_surveillance_query_by_filters(filters_json: str, limit: int = default_limit,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query surveillance data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted surveillance data
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
            result = query_surveillance_by_filters(filters, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying surveillance by filters: {str(e)}"


    @tool(name="bvbrc_surveillance_get_by_host_species", description="Get surveillance data by host species. Parameters: host_species (str) - host species to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_surveillance_get_by_host_species(host_species: str, limit: int = default_limit,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get surveillance data by host species.
        
        Args:
            host_species: The host species to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted surveillance data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_surveillance_by_host_species(host_species, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying surveillance by host species: {str(e)}"


    @tool(name="bvbrc_surveillance_get_by_collection_country", description="Get surveillance data by collection country. Parameters: collection_country (str) - collection country to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_surveillance_get_by_collection_country(collection_country: str, limit: int = default_limit,
                                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get surveillance data by collection country.
        
        Args:
            collection_country: The collection country to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted surveillance data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_surveillance_by_collection_country(collection_country, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying surveillance by collection country: {str(e)}"


    @tool(name="bvbrc_surveillance_get_by_species", description="Get surveillance data by species. Parameters: species (str) - species to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_surveillance_get_by_species(species: str, limit: int = default_limit,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get surveillance data by species.
        
        Args:
            species: The species to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted surveillance data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_surveillance_by_species(species, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying surveillance by species: {str(e)}"


    @tool(name="bvbrc_surveillance_get_by_strain", description="Get surveillance data by strain. Parameters: strain (str) - strain to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_surveillance_get_by_strain(strain: str, limit: int = default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get surveillance data by strain.
        
        Args:
            strain: The strain to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted surveillance data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_surveillance_by_strain(strain, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying surveillance by strain: {str(e)}"


    @tool(name="bvbrc_surveillance_get_by_disease_status", description="Get surveillance data by disease status. Parameters: disease_status (str) - disease status to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_surveillance_get_by_disease_status(disease_status: str, limit: int = default_limit,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get surveillance data by disease status.
        
        Args:
            disease_status: The disease status to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted surveillance data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_surveillance_by_disease_status(disease_status, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying surveillance by disease status: {str(e)}"


    @tool(name="bvbrc_surveillance_get_by_collection_date_range", description="Get surveillance data by collection date range. Parameters: start_date (str) - start date in YYYY-MM-DD format; end_date (str) - end date in YYYY-MM-DD format; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_surveillance_get_by_collection_date_range(start_date: str, end_date: str, limit: int = default_limit,
                                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get surveillance data by collection date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted surveillance data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_surveillance_by_collection_date_range(start_date, end_date, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying surveillance by collection date range: {str(e)}"


    @tool(name="bvbrc_surveillance_search_by_keyword", description="Search surveillance data by keyword. Parameters: keyword (str) - keyword to search for; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_surveillance_search_by_keyword(keyword: str, limit: int = default_limit,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search surveillance data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted surveillance data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_surveillance_by_keyword(keyword, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching surveillance by keyword: {str(e)}"


    @tool(name="bvbrc_surveillance_get_all", description="Get all surveillance data. Parameters: limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_surveillance_get_all(limit: int = default_limit,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all surveillance data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted surveillance data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_surveillance_all(options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all surveillance data: {str(e)}"
