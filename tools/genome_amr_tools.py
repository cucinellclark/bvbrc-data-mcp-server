#!/usr/bin/env python3
"""
BV-BRC Genome AMR Tools

This module contains MCP tools for querying genome antimicrobial resistance data from BV-BRC.
"""

import json
from typing import Optional

from flaskmcp import tool
from data_functions import (
    query_genome_amr_by_id,
    query_genome_amr_by_filters,
    query_genome_amr_by_antibiotic,
    query_genome_amr_by_computational_method,
    query_genome_amr_by_computational_method_version,
    query_genome_amr_by_evidence,
    query_genome_amr_by_genome_id,
    query_genome_amr_by_genome_name,
    query_genome_amr_by_laboratory_typing_method,
    query_genome_amr_by_laboratory_typing_method_version,
    query_genome_amr_by_laboratory_typing_platform,
    query_genome_amr_by_measurement,
    query_genome_amr_by_measurement_sign,
    query_genome_amr_by_measurement_unit,
    query_genome_amr_by_measurement_value,
    query_genome_amr_by_owner,
    query_genome_amr_by_pmid,
    query_genome_amr_by_public_status,
    query_genome_amr_by_resistant_phenotype,
    query_genome_amr_by_source,
    query_genome_amr_by_taxon_id,
    query_genome_amr_by_testing_standard,
    query_genome_amr_by_testing_standard_year,
    query_genome_amr_by_vendor,
    query_genome_amr_by_date_range,
    query_genome_amr_by_modified_date_range,
    query_genome_amr_by_keyword,
    query_genome_amr_all,
    format_query_result
)


def register_genome_amr_tools(base_url: str, default_limit: int):
    """Register all genome AMR-related MCP tools with the Flask app."""
    
    @tool(name="bvbrc_genome_amr_get_by_id", description="Get genome AMR data by ID. Parameters: id (str) - AMR record ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_amr_get_by_id(id: str, limit: int = default_limit,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by ID.
        
        Args:
            id: The AMR record ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_amr_by_id(id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome AMR by ID: {str(e)}"


    @tool(name="bvbrc_genome_amr_query_by_filters", description="Query genome AMR data by custom filters. Parameters: filters_json (str) - JSON string of filter criteria; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_amr_query_by_filters(filters_json: str, limit: int = default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query genome AMR data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
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
            result = query_genome_amr_by_filters(filters, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome AMR by filters: {str(e)}"


    @tool(name="bvbrc_genome_amr_get_by_antibiotic", description="Get genome AMR data by antibiotic. Parameters: antibiotic (str) - antibiotic to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_amr_get_by_antibiotic(antibiotic: str, limit: int = default_limit,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by antibiotic.
        
        Args:
            antibiotic: The antibiotic to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_amr_by_antibiotic(antibiotic, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome AMR by antibiotic: {str(e)}"


    @tool(name="bvbrc_genome_amr_get_by_genome_id", description="Get genome AMR data by genome ID. Parameters: genome_id (str) - genome ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_amr_get_by_genome_id(genome_id: str, limit: int = default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by genome ID.
        
        Args:
            genome_id: The genome ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_amr_by_genome_id(genome_id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome AMR by genome ID: {str(e)}"


    @tool(name="bvbrc_genome_amr_get_by_genome_name", description="Get genome AMR data by genome name. Parameters: genome_name (str) - genome name to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_amr_get_by_genome_name(genome_name: str, limit: int = default_limit,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by genome name.
        
        Args:
            genome_name: The genome name to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_amr_by_genome_name(genome_name, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome AMR by genome name: {str(e)}"


    @tool(name="bvbrc_genome_amr_get_by_resistant_phenotype", description="Get genome AMR data by resistant phenotype. Parameters: resistant_phenotype (str) - resistant phenotype to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_amr_get_by_resistant_phenotype(resistant_phenotype: str, limit: int = default_limit,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by resistant phenotype.
        
        Args:
            resistant_phenotype: The resistant phenotype to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_amr_by_resistant_phenotype(resistant_phenotype, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome AMR by resistant phenotype: {str(e)}"


    @tool(name="bvbrc_genome_amr_get_by_taxon_id", description="Get genome AMR data by taxon ID. Parameters: taxon_id (int) - taxon ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_amr_get_by_taxon_id(taxon_id: int, limit: int = default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_amr_by_taxon_id(taxon_id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome AMR by taxon ID: {str(e)}"


    @tool(name="bvbrc_genome_amr_get_by_pmid", description="Get genome AMR data by PMID. Parameters: pmid (int) - PMID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_amr_get_by_pmid(pmid: int, limit: int = default_limit,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by PMID.
        
        Args:
            pmid: The PMID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_amr_by_pmid(pmid, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome AMR by PMID: {str(e)}"


    @tool(name="bvbrc_genome_amr_get_by_public_status", description="Get genome AMR data by public status. Parameters: is_public (bool) - public status to query (True/False); limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_amr_get_by_public_status(is_public: bool, limit: int = default_limit,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by public status.
        
        Args:
            is_public: The public status to query (True/False)
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_amr_by_public_status(is_public, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome AMR by public status: {str(e)}"


    @tool(name="bvbrc_genome_amr_get_by_date_range", description="Get genome AMR data by date range. Parameters: start_date (str) - start date in YYYY-MM-DD format; end_date (str) - end date in YYYY-MM-DD format; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_amr_get_by_date_range(start_date: str, end_date: str, limit: int = default_limit,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_amr_by_date_range(start_date, end_date, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome AMR by date range: {str(e)}"


    @tool(name="bvbrc_genome_amr_search_by_keyword", description="Search genome AMR data by keyword. Parameters: keyword (str) - keyword to search for; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_amr_search_by_keyword(keyword: str, limit: int = default_limit,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search genome AMR data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_amr_by_keyword(keyword, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching genome AMR by keyword: {str(e)}"


    @tool(name="bvbrc_genome_amr_get_all", description="Get all genome AMR data. Parameters: limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_genome_amr_get_all(limit: int = default_limit,
                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all genome AMR data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_amr_all(options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all genome AMR data: {str(e)}"
