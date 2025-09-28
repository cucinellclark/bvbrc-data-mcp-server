#!/usr/bin/env python3
"""
BV-BRC Experiment Tools

This module contains MCP tools for querying experiment data from BV-BRC.
"""

import json
from typing import Optional

from flaskmcp import tool
from data_functions import (
    query_experiment_by_id,
    query_experiment_by_filters,
    query_experiment_by_exp_name,
    query_experiment_by_exp_type,
    query_experiment_by_exp_description,
    query_experiment_by_exp_title,
    query_experiment_by_organism,
    query_experiment_by_strain,
    query_experiment_by_genome_id,
    query_experiment_by_taxon_id,
    query_experiment_by_study_name,
    query_experiment_by_study_title,
    query_experiment_by_study_pi,
    query_experiment_by_study_institution,
    query_experiment_by_experimenters,
    query_experiment_by_measurement_technique,
    query_experiment_by_detection_instrument,
    query_experiment_by_pmid,
    query_experiment_by_doi,
    query_experiment_by_public_identifier,
    query_experiment_by_public_repository,
    query_experiment_by_biosets,
    query_experiment_by_samples,
    query_experiment_by_treatment_name,
    query_experiment_by_treatment_type,
    query_experiment_by_treatment_amount,
    query_experiment_by_treatment_duration,
    query_experiment_by_date_inserted_range,
    query_experiment_by_date_modified_range,
    query_experiment_by_biosets_range,
    query_experiment_by_samples_range,
    query_experiment_by_keyword,
    query_experiment_all,
    format_query_result
)


def register_experiment_tools(base_url: str, default_limit: int):
    """Register all experiment-related MCP tools with the Flask app."""
    
    @tool(name="bvbrc_experiment_get_by_id", description="Get experiment data by experiment ID. Parameters: exp_id (str) - experiment ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_experiment_get_by_id(exp_id: str, limit: int = default_limit,
                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by experiment ID.
        
        Args:
            exp_id: The experiment ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_id(exp_id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by ID: {str(e)}"


    @tool(name="bvbrc_experiment_query_by_filters", description="Query experiment data by custom filters. Parameters: filters_json (str) - JSON string of filter criteria; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_experiment_query_by_filters(filters_json: str, limit: int = default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query experiment data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
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
            result = query_experiment_by_filters(filters, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by filters: {str(e)}"


    @tool(name="bvbrc_experiment_get_by_exp_name", description="Get experiment data by experiment name. Parameters: exp_name (str) - experiment name to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_experiment_get_by_exp_name(exp_name: str, limit: int = default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by experiment name.
        
        Args:
            exp_name: The experiment name to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_exp_name(exp_name, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by experiment name: {str(e)}"


    @tool(name="bvbrc_experiment_get_by_exp_type", description="Get experiment data by experiment type. Parameters: exp_type (str) - experiment type to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_experiment_get_by_exp_type(exp_type: str, limit: int = default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by experiment type.
        
        Args:
            exp_type: The experiment type to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_exp_type(exp_type, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by experiment type: {str(e)}"


    @tool(name="bvbrc_experiment_get_by_organism", description="Get experiment data by organism. Parameters: organism (str) - organism to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_experiment_get_by_organism(organism: str, limit: int = default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by organism.
        
        Args:
            organism: The organism to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_organism(organism, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by organism: {str(e)}"


    @tool(name="bvbrc_experiment_get_by_strain", description="Get experiment data by strain. Parameters: strain (str) - strain to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_experiment_get_by_strain(strain: str, limit: int = default_limit,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by strain.
        
        Args:
            strain: The strain to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_strain(strain, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by strain: {str(e)}"


    @tool(name="bvbrc_experiment_get_by_genome_id", description="Get experiment data by genome ID. Parameters: genome_id (str) - genome ID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_experiment_get_by_genome_id(genome_id: str, limit: int = default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by genome ID.
        
        Args:
            genome_id: The genome ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_genome_id(genome_id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by genome ID: {str(e)}"


    @tool(name="bvbrc_experiment_get_by_study_name", description="Get experiment data by study name. Parameters: study_name (str) - study name to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_experiment_get_by_study_name(study_name: str, limit: int = default_limit,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by study name.
        
        Args:
            study_name: The study name to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_study_name(study_name, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by study name: {str(e)}"


    @tool(name="bvbrc_experiment_get_by_study_pi", description="Get experiment data by study principal investigator. Parameters: study_pi (str) - study principal investigator to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_experiment_get_by_study_pi(study_pi: str, limit: int = default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by study principal investigator.
        
        Args:
            study_pi: The study principal investigator to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_study_pi(study_pi, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by study principal investigator: {str(e)}"


    @tool(name="bvbrc_experiment_get_by_pmid", description="Get experiment data by PMID. Parameters: pmid (str) - PMID to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_experiment_get_by_pmid(pmid: str, limit: int = default_limit,
                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by PMID.
        
        Args:
            pmid: The PMID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_pmid(pmid, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by PMID: {str(e)}"


    @tool(name="bvbrc_experiment_get_by_doi", description="Get experiment data by DOI. Parameters: doi (str) - DOI to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_experiment_get_by_doi(doi: str, limit: int = default_limit,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by DOI.
        
        Args:
            doi: The DOI to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_doi(doi, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by DOI: {str(e)}"


    @tool(name="bvbrc_experiment_get_by_treatment_name", description="Get experiment data by treatment name. Parameters: treatment_name (str) - treatment name to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_experiment_get_by_treatment_name(treatment_name: str, limit: int = default_limit,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by treatment name.
        
        Args:
            treatment_name: The treatment name to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_treatment_name(treatment_name, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by treatment name: {str(e)}"


    @tool(name="bvbrc_experiment_get_by_treatment_type", description="Get experiment data by treatment type. Parameters: treatment_type (str) - treatment type to query; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_experiment_get_by_treatment_type(treatment_type: str, limit: int = default_limit,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by treatment type.
        
        Args:
            treatment_type: The treatment type to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_treatment_type(treatment_type, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by treatment type: {str(e)}"


    @tool(name="bvbrc_experiment_get_by_biosets_range", description="Get experiment data by biosets range. Parameters: min_biosets (int) - minimum biosets; max_biosets (int) - maximum biosets; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_experiment_get_by_biosets_range(min_biosets: int, max_biosets: int, limit: int = default_limit,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by biosets range.
        
        Args:
            min_biosets: Minimum biosets
            max_biosets: Maximum biosets
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_biosets_range(min_biosets, max_biosets, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by biosets range: {str(e)}"


    @tool(name="bvbrc_experiment_get_by_samples_range", description="Get experiment data by samples range. Parameters: min_samples (int) - minimum samples; max_samples (int) - maximum samples; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_experiment_get_by_samples_range(min_samples: int, max_samples: int, limit: int = default_limit,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by samples range.
        
        Args:
            min_samples: Minimum samples
            max_samples: Maximum samples
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_samples_range(min_samples, max_samples, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by samples range: {str(e)}"


    @tool(name="bvbrc_experiment_get_by_date_inserted_range", description="Get experiment data by date inserted range. Parameters: start_date (str) - start date in YYYY-MM-DD format; end_date (str) - end date in YYYY-MM-DD format; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_experiment_get_by_date_inserted_range(start_date: str, end_date: str, limit: int = default_limit,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_date_inserted_range(start_date, end_date, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by date inserted range: {str(e)}"


    @tool(name="bvbrc_experiment_search_by_keyword", description="Search experiment data by keyword. Parameters: keyword (str) - keyword to search for; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_experiment_search_by_keyword(keyword: str, limit: int = default_limit,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search experiment data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_keyword(keyword, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching experiment by keyword: {str(e)}"


    @tool(name="bvbrc_experiment_get_all", description="Get all experiment data. Parameters: limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_experiment_get_all(limit: int = default_limit,
                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all experiment data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_all(options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all experiment data: {str(e)}"
