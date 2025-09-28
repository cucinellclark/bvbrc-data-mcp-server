#!/usr/bin/env python3
"""
BV-BRC ID Reference Tools

This module contains MCP tools for querying ID reference data from BV-BRC.
"""

import json
from typing import Optional

from flaskmcp import tool
from data_functions import (
    query_id_ref_by_id,
    query_id_ref_by_filters,
    query_id_ref_by_id_type,
    query_id_ref_by_id_value,
    query_id_ref_by_uniprotkb_accession,
    query_id_ref_by_date_inserted_range,
    query_id_ref_by_date_modified_range,
    query_id_ref_by_keyword,
    query_id_ref_all,
    format_query_result
)


def register_id_ref_tools(base_url: str, default_limit: int):
    """Register all ID reference-related MCP tools with the Flask app."""
    
    @tool(name="bvbrc_id_ref_get_by_id", description="Get ID reference data by ID. Parameters: id (str) - ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_id_ref_get_by_id(id: str, limit: int = default_limit,
                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get ID reference data by ID.
        
        Args:
            id: The ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted ID reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_id_ref_by_id(id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying ID reference by ID: {str(e)}"


    @tool(name="bvbrc_id_ref_query_by_filters", description="Query ID reference data by custom filters. Parameters: filters_json (str) - JSON string of filter criteria; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_id_ref_query_by_filters(filters_json: str, limit: int = default_limit,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query ID reference data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted ID reference data
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
            result = query_id_ref_by_filters(filters, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying ID reference by filters: {str(e)}"


    @tool(name="bvbrc_id_ref_get_by_id_type", description="Get ID reference data by ID type. Parameters: id_type (str) - ID type to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_id_ref_get_by_id_type(id_type: str, limit: int = default_limit,
                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get ID reference data by ID type.
        
        Args:
            id_type: The ID type to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted ID reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_id_ref_by_id_type(id_type, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying ID reference by ID type: {str(e)}"


    @tool(name="bvbrc_id_ref_get_by_id_value", description="Get ID reference data by ID value. Parameters: id_value (str) - ID value to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_id_ref_get_by_id_value(id_value: str, limit: int = default_limit,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get ID reference data by ID value.
        
        Args:
            id_value: The ID value to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted ID reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_id_ref_by_id_value(id_value, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying ID reference by ID value: {str(e)}"


    @tool(name="bvbrc_id_ref_get_by_uniprotkb_accession", description="Get ID reference data by UniProtKB accession. Parameters: uniprotkb_accession (str) - UniProtKB accession to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_id_ref_get_by_uniprotkb_accession(uniprotkb_accession: str, limit: int = default_limit,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get ID reference data by UniProtKB accession.
        
        Args:
            uniprotkb_accession: The UniProtKB accession to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted ID reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_id_ref_by_uniprotkb_accession(uniprotkb_accession, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying ID reference by UniProtKB accession: {str(e)}"


    @tool(name="bvbrc_id_ref_get_by_date_inserted_range", description="Get ID reference data by date inserted range. Parameters: start_date (str) - start date in YYYY-MM-DD format; end_date (str) - end date in YYYY-MM-DD format; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_id_ref_get_by_date_inserted_range(start_date: str, end_date: str, limit: int = default_limit,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get ID reference data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted ID reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_id_ref_by_date_inserted_range(start_date, end_date, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying ID reference by date inserted range: {str(e)}"


    @tool(name="bvbrc_id_ref_get_by_date_modified_range", description="Get ID reference data by date modified range. Parameters: start_date (str) - start date in YYYY-MM-DD format; end_date (str) - end date in YYYY-MM-DD format; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_id_ref_get_by_date_modified_range(start_date: str, end_date: str, limit: int = default_limit,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get ID reference data by date modified range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted ID reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_id_ref_by_date_modified_range(start_date, end_date, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying ID reference by date modified range: {str(e)}"


    @tool(name="bvbrc_id_ref_search_by_keyword", description="Search ID reference data by keyword. Parameters: keyword (str) - keyword to search for; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_id_ref_search_by_keyword(keyword: str, limit: int = default_limit,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search ID reference data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted ID reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_id_ref_by_keyword(keyword, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching ID reference by keyword: {str(e)}"


    @tool(name="bvbrc_id_ref_get_all", description="Get all ID reference data. Parameters: limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_id_ref_get_all(limit: int = default_limit,
                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all ID reference data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted ID reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_id_ref_all(options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all ID reference data: {str(e)}"
