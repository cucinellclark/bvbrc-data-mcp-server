#!/usr/bin/env python3
"""
BV-BRC Spike Variant Tools

This module contains MCP tools for querying spike variant data from BV-BRC.
"""

import json
from typing import Optional

from flaskmcp import tool
from data_functions import (
    query_spike_variant_by_id,
    query_spike_variant_by_filters,
    query_spike_variant_by_aa_variant,
    query_spike_variant_by_country,
    query_spike_variant_by_region,
    query_spike_variant_by_month,
    query_spike_variant_by_sequence_feature,
    query_spike_variant_by_growth_rate,
    query_spike_variant_by_prevalence,
    query_spike_variant_by_lineage_count,
    query_spike_variant_by_total_isolates,
    query_spike_variant_by_growth_rate_range,
    query_spike_variant_by_prevalence_range,
    query_spike_variant_by_lineage_count_range,
    query_spike_variant_by_total_isolates_range,
    query_spike_variant_by_date_range,
    query_spike_variant_by_modified_date_range,
    query_spike_variant_by_keyword,
    query_spike_variant_all,
    format_query_result
)


def register_spike_variant_tools(base_url: str, default_limit: int):
    """Register all spike variant-related MCP tools with the Flask app."""
    
    @tool(name="bvbrc_spike_variant_get_by_id", description="Get spike variant data by ID. Parameters: id (str) - ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_spike_variant_get_by_id(id: str, limit: int = default_limit,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike variant data by ID.
        
        Args:
            id: The ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_spike_variant_by_id(id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying spike variant by ID: {str(e)}"


    @tool(name="bvbrc_spike_variant_query_by_filters", description="Query spike variant data by custom filters. Parameters: filters_json (str) - JSON string of filter criteria; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_spike_variant_query_by_filters(filters_json: str, limit: int = default_limit,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query spike variant data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
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
            result = query_spike_variant_by_filters(filters, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying spike variant by filters: {str(e)}"


    @tool(name="bvbrc_spike_variant_get_by_aa_variant", description="Get spike variant data by amino acid variant. Parameters: aa_variant (str) - amino acid variant to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_spike_variant_get_by_aa_variant(aa_variant: str, limit: int = default_limit,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike variant data by amino acid variant.
        
        Args:
            aa_variant: The amino acid variant to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_spike_variant_by_aa_variant(aa_variant, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying spike variant by amino acid variant: {str(e)}"


    @tool(name="bvbrc_spike_variant_get_by_country", description="Get spike variant data by country. Parameters: country (str) - country to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_spike_variant_get_by_country(country: str, limit: int = default_limit,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike variant data by country.
        
        Args:
            country: The country to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_spike_variant_by_country(country, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying spike variant by country: {str(e)}"


    @tool(name="bvbrc_spike_variant_get_by_region", description="Get spike variant data by region. Parameters: region (str) - region to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_spike_variant_get_by_region(region: str, limit: int = default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike variant data by region.
        
        Args:
            region: The region to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_spike_variant_by_region(region, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying spike variant by region: {str(e)}"


    @tool(name="bvbrc_spike_variant_get_by_growth_rate_range", description="Get spike variant data by growth rate range. Parameters: min_growth_rate (float) - minimum growth rate; max_growth_rate (float) - maximum growth rate; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_spike_variant_get_by_growth_rate_range(min_growth_rate: float, max_growth_rate: float, limit: int = default_limit,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike variant data by growth rate range.
        
        Args:
            min_growth_rate: Minimum growth rate
            max_growth_rate: Maximum growth rate
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_spike_variant_by_growth_rate_range(min_growth_rate, max_growth_rate, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying spike variant by growth rate range: {str(e)}"


    @tool(name="bvbrc_spike_variant_get_by_prevalence_range", description="Get spike variant data by prevalence range. Parameters: min_prevalence (float) - minimum prevalence; max_prevalence (float) - maximum prevalence; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_spike_variant_get_by_prevalence_range(min_prevalence: float, max_prevalence: float, limit: int = default_limit,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike variant data by prevalence range.
        
        Args:
            min_prevalence: Minimum prevalence
            max_prevalence: Maximum prevalence
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_spike_variant_by_prevalence_range(min_prevalence, max_prevalence, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying spike variant by prevalence range: {str(e)}"


    @tool(name="bvbrc_spike_variant_get_by_date_range", description="Get spike variant data by date range. Parameters: start_date (str) - start date in YYYY-MM-DD format; end_date (str) - end date in YYYY-MM-DD format; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_spike_variant_get_by_date_range(start_date: str, end_date: str, limit: int = default_limit,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike variant data by date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_spike_variant_by_date_range(start_date, end_date, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying spike variant by date range: {str(e)}"


    @tool(name="bvbrc_spike_variant_search_by_keyword", description="Search spike variant data by keyword. Parameters: keyword (str) - keyword to search for; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_spike_variant_search_by_keyword(keyword: str, limit: int = default_limit,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search spike variant data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_spike_variant_by_keyword(keyword, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching spike variant by keyword: {str(e)}"


    @tool(name="bvbrc_spike_variant_get_all", description="Get all spike variant data. Parameters: limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_spike_variant_get_all(limit: int = default_limit,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all spike variant data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_spike_variant_all(options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all spike variant data: {str(e)}"
