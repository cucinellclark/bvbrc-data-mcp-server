#!/usr/bin/env python3
"""
BV-BRC Antibiotics Tools

This module contains MCP tools for querying antibiotic data from BV-BRC.
"""

import json
from typing import Optional

from flaskmcp import tool
from data_functions import (
    query_antibiotics_by_pubchem_cid,
    query_antibiotics_by_filters,
    query_antibiotics_by_keyword,
    query_antibiotics_by_name,
    query_antibiotics_by_cas_id,
    query_antibiotics_by_molecular_formula,
    query_antibiotics_by_atc_classification,
    query_antibiotics_by_mechanism_of_action,
    query_antibiotics_by_pharmacological_class,
    query_antibiotics_by_synonym,
    query_antibiotics_by_molecular_weight_range,
    query_antibiotics_by_date_range,
    query_antibiotics_all,
    format_query_result
)


def register_antibiotics_tools(base_url: str, default_limit: int):
    """Register all antibiotics-related MCP tools with the Flask app."""
    
    @tool(name="bvbrc_antibiotics_get_by_pubchem_cid", description="Get antibiotic data by PubChem CID. Parameters: pubchem_cid (str) - PubChem CID to query (e.g., '2244'); limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_antibiotics_get_by_pubchem_cid(pubchem_cid: str, limit: int = default_limit,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get antibiotic data by PubChem CID.
        
        Args:
            pubchem_cid: The PubChem CID to query (e.g., "2244")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_antibiotics_by_pubchem_cid(pubchem_cid, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying antibiotics by PubChem CID: {str(e)}"


    @tool(name="bvbrc_antibiotics_query_by_filters", description="Query antibiotic data by custom filters. Parameters: filters_json (str) - JSON string of filter criteria (e.g., '{\"antibiotic_name\": \"penicillin\", \"mechanism_of_action\": \"cell wall synthesis inhibitor\"}'); limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_antibiotics_query_by_filters(filters_json: str, limit: int = default_limit,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query antibiotic data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria (e.g., '{"antibiotic_name": "penicillin", "mechanism_of_action": "cell wall synthesis inhibitor"}')
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
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
            result = query_antibiotics_by_filters(filters, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying antibiotics by filters: {str(e)}"


    @tool(name="bvbrc_antibiotics_search_by_keyword", description="Search antibiotic data by keyword. Parameters: keyword (str) - keyword to search for (e.g., 'penicillin'); limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_antibiotics_search_by_keyword(keyword: str, limit: int = default_limit,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search antibiotic data by keyword.
        
        Args:
            keyword: The keyword to search for (e.g., "penicillin")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_antibiotics_by_keyword(keyword, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching antibiotics by keyword: {str(e)}"


    @tool(name="bvbrc_antibiotics_get_by_name", description="Get antibiotic data by antibiotic name. Parameters: antibiotic_name (str) - antibiotic name to query (e.g., 'penicillin'); limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_antibiotics_get_by_name(antibiotic_name: str, limit: int = default_limit,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get antibiotic data by antibiotic name.
        
        Args:
            antibiotic_name: The antibiotic name to query (e.g., "penicillin")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_antibiotics_by_name(antibiotic_name, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying antibiotics by name: {str(e)}"


    @tool(name="bvbrc_antibiotics_get_by_cas_id", description="Get antibiotic data by CAS ID. Parameters: cas_id (str) - CAS ID to query (e.g., '61-33-6'); limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_antibiotics_get_by_cas_id(cas_id: str, limit: int = default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get antibiotic data by CAS ID.
        
        Args:
            cas_id: The CAS ID to query (e.g., "61-33-6")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_antibiotics_by_cas_id(cas_id, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying antibiotics by CAS ID: {str(e)}"


    @tool(name="bvbrc_antibiotics_get_by_molecular_formula", description="Get antibiotic data by molecular formula. Parameters: molecular_formula (str) - molecular formula to query (e.g., 'C16H18N2O4S'); limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_antibiotics_get_by_molecular_formula(molecular_formula: str, limit: int = default_limit,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get antibiotic data by molecular formula.
        
        Args:
            molecular_formula: The molecular formula to query (e.g., "C16H18N2O4S")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_antibiotics_by_molecular_formula(molecular_formula, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying antibiotics by molecular formula: {str(e)}"


    @tool(name="bvbrc_antibiotics_get_by_atc_classification", description="Get antibiotic data by ATC classification. Parameters: atc_classification (str) - ATC classification to query (e.g., 'J01CA04'); limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_antibiotics_get_by_atc_classification(atc_classification: str, limit: int = default_limit,
                                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get antibiotic data by ATC classification.
        
        Args:
            atc_classification: The ATC classification to query (e.g., "J01CA04")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_antibiotics_by_atc_classification(atc_classification, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying antibiotics by ATC classification: {str(e)}"


    @tool(name="bvbrc_antibiotics_get_by_mechanism_of_action", description="Get antibiotic data by mechanism of action. Parameters: mechanism_of_action (str) - mechanism of action to query (e.g., 'cell wall synthesis inhibitor'); limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_antibiotics_get_by_mechanism_of_action(mechanism_of_action: str, limit: int = default_limit,
                                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get antibiotic data by mechanism of action.
        
        Args:
            mechanism_of_action: The mechanism of action to query (e.g., "cell wall synthesis inhibitor")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_antibiotics_by_mechanism_of_action(mechanism_of_action, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying antibiotics by mechanism of action: {str(e)}"


    @tool(name="bvbrc_antibiotics_get_by_pharmacological_class", description="Get antibiotic data by pharmacological class. Parameters: pharmacological_class (str) - pharmacological class to query (e.g., 'beta-lactam'); limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_antibiotics_get_by_pharmacological_class(pharmacological_class: str, limit: int = default_limit,
                                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get antibiotic data by pharmacological class.
        
        Args:
            pharmacological_class: The pharmacological class to query (e.g., "beta-lactam")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_antibiotics_by_pharmacological_class(pharmacological_class, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying antibiotics by pharmacological class: {str(e)}"


    @tool(name="bvbrc_antibiotics_get_by_synonym", description="Get antibiotic data by synonym. Parameters: synonym (str) - synonym to query (e.g., 'benzylpenicillin'); limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_antibiotics_get_by_synonym(synonym: str, limit: int = default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get antibiotic data by synonym.
        
        Args:
            synonym: The synonym to query (e.g., "benzylpenicillin")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_antibiotics_by_synonym(synonym, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying antibiotics by synonym: {str(e)}"


    @tool(name="bvbrc_antibiotics_get_by_molecular_weight_range", description="Get antibiotic data by molecular weight range. Parameters: min_weight (float) - minimum molecular weight; max_weight (float) - maximum molecular weight; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_antibiotics_get_by_molecular_weight_range(min_weight: float, max_weight: float, limit: int = default_limit,
                                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get antibiotic data by molecular weight range.
        
        Args:
            min_weight: Minimum molecular weight
            max_weight: Maximum molecular weight
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_antibiotics_by_molecular_weight_range(min_weight, max_weight, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying antibiotics by molecular weight range: {str(e)}"


    @tool(name="bvbrc_antibiotics_get_by_date_range", description="Get antibiotic data by date range. Parameters: start_date (str) - start date in YYYY-MM-DD format; end_date (str) - end date in YYYY-MM-DD format; limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_antibiotics_get_by_date_range(start_date: str, end_date: str, limit: int = default_limit,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get antibiotic data by date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_antibiotics_by_date_range(start_date, end_date, options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying antibiotics by date range: {str(e)}"


    @tool(name="bvbrc_antibiotics_get_all", description="Get all antibiotic data. Parameters: limit (int, optional) - max results (default: 1000); select (str, optional) - comma-separated field list; sort (str, optional) - sort field")
    def bvbrc_antibiotics_get_all(limit: int = default_limit,
                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all antibiotic data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_antibiotics_all(options, base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all antibiotics: {str(e)}"
