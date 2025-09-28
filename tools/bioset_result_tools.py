#!/usr/bin/env python3
"""
BV-BRC Bioset Result Tools

This module contains MCP tools for querying bioset_result data from BV-BRC.
"""

import json
from typing import Optional

from flaskmcp import tool
from data_functions import (
    query_bioset_result_by_id,
    query_bioset_result_by_filters,
    query_bioset_result_by_bioset_id,
    query_bioset_result_by_bioset_name,
    query_bioset_result_by_bioset_description,
    query_bioset_result_by_bioset_type,
    query_bioset_result_by_entity_id,
    query_bioset_result_by_entity_name,
    query_bioset_result_by_entity_type,
    query_bioset_result_by_exp_id,
    query_bioset_result_by_exp_name,
    query_bioset_result_by_exp_title,
    query_bioset_result_by_exp_type,
    query_bioset_result_by_feature_id,
    query_bioset_result_by_gene,
    query_bioset_result_by_gene_id,
    query_bioset_result_by_genome_id,
    query_bioset_result_by_locus_tag,
    query_bioset_result_by_organism,
    query_bioset_result_by_patric_id,
    query_bioset_result_by_product,
    query_bioset_result_by_protein_id,
    query_bioset_result_by_result_type,
    query_bioset_result_by_strain,
    query_bioset_result_by_taxon_id,
    query_bioset_result_by_uniprot_id,
    query_bioset_result_by_other_id,
    query_bioset_result_by_treatment_name,
    query_bioset_result_by_treatment_type,
    query_bioset_result_by_treatment_amount,
    query_bioset_result_by_treatment_duration,
    query_bioset_result_by_counts_range,
    query_bioset_result_by_fpkm_range,
    query_bioset_result_by_log2_fc_range,
    query_bioset_result_by_p_value_range,
    query_bioset_result_by_tpm_range,
    query_bioset_result_by_other_value_range,
    query_bioset_result_by_z_score_range,
    query_bioset_result_by_version,
    query_bioset_result_by_date_inserted_range,
    query_bioset_result_by_date_modified_range,
    query_bioset_result_by_keyword,
    query_bioset_result_all,
    format_query_result
)


def register_bioset_result_tools(base_url: str, default_limit: int):
    """Register all bioset_result-related MCP tools with the Flask app."""

    def build_options(limit: int, select: Optional[str], sort: Optional[str]):
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        return options

    @tool(name="bvbrc_bioset_result_get_by_id", description="Get bioset_result by id. Parameters: id (str) - document id; limit (int, optional); select (str, optional); sort (str, optional)")
    def bvbrc_bioset_result_get_by_id(id: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_id(id, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by id: {str(e)}"

    @tool(name="bvbrc_bioset_result_query_by_filters", description="Query bioset_result by filters JSON. Parameters: filters_json (str); limit (int, optional); select (str, optional); sort (str, optional)")
    def bvbrc_bioset_result_query_by_filters(filters_json: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            filters = json.loads(filters_json)
        except json.JSONDecodeError as e:
            return f"Error parsing filters JSON: {str(e)}"
        try:
            return format_query_result(query_bioset_result_by_filters(filters, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by filters: {str(e)}"

    # Auto-generate simple one-arg tools to keep file compact
    def gen_simple_tool(func, name: str, param: str, desc: str):
        @tool(name=name, description=desc)
        def _inner(value: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:  # type: ignore
            try:
                return format_query_result(func(value, build_options(limit, select, sort), base_url))
            except Exception as e:
                return f"Error querying {name}: {str(e)}"
        return _inner

    gen_simple_tool(query_bioset_result_by_bioset_id, "bvbrc_bioset_result_get_by_bioset_id", "bioset_id", "Get bioset_result by bioset_id. Parameters: bioset_id (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_bioset_name, "bvbrc_bioset_result_get_by_bioset_name", "bioset_name", "Get bioset_result by bioset_name. Parameters: bioset_name (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_bioset_description, "bvbrc_bioset_result_get_by_bioset_description", "bioset_description", "Get bioset_result by bioset_description. Parameters: bioset_description (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_bioset_type, "bvbrc_bioset_result_get_by_bioset_type", "bioset_type", "Get bioset_result by bioset_type. Parameters: bioset_type (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_entity_id, "bvbrc_bioset_result_get_by_entity_id", "entity_id", "Get bioset_result by entity_id. Parameters: entity_id (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_entity_name, "bvbrc_bioset_result_get_by_entity_name", "entity_name", "Get bioset_result by entity_name. Parameters: entity_name (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_entity_type, "bvbrc_bioset_result_get_by_entity_type", "entity_type", "Get bioset_result by entity_type. Parameters: entity_type (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_exp_id, "bvbrc_bioset_result_get_by_exp_id", "exp_id", "Get bioset_result by exp_id. Parameters: exp_id (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_exp_name, "bvbrc_bioset_result_get_by_exp_name", "exp_name", "Get bioset_result by exp_name. Parameters: exp_name (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_exp_title, "bvbrc_bioset_result_get_by_exp_title", "exp_title", "Get bioset_result by exp_title. Parameters: exp_title (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_exp_type, "bvbrc_bioset_result_get_by_exp_type", "exp_type", "Get bioset_result by exp_type. Parameters: exp_type (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_feature_id, "bvbrc_bioset_result_get_by_feature_id", "feature_id", "Get bioset_result by feature_id. Parameters: feature_id (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_gene, "bvbrc_bioset_result_get_by_gene", "gene", "Get bioset_result by gene. Parameters: gene (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_gene_id, "bvbrc_bioset_result_get_by_gene_id", "gene_id", "Get bioset_result by gene_id. Parameters: gene_id (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_genome_id, "bvbrc_bioset_result_get_by_genome_id", "genome_id", "Get bioset_result by genome_id. Parameters: genome_id (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_locus_tag, "bvbrc_bioset_result_get_by_locus_tag", "locus_tag", "Get bioset_result by locus_tag. Parameters: locus_tag (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_organism, "bvbrc_bioset_result_get_by_organism", "organism", "Get bioset_result by organism. Parameters: organism (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_patric_id, "bvbrc_bioset_result_get_by_patric_id", "patric_id", "Get bioset_result by patric_id. Parameters: patric_id (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_product, "bvbrc_bioset_result_get_by_product", "product", "Get bioset_result by product. Parameters: product (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_protein_id, "bvbrc_bioset_result_get_by_protein_id", "protein_id", "Get bioset_result by protein_id. Parameters: protein_id (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_result_type, "bvbrc_bioset_result_get_by_result_type", "result_type", "Get bioset_result by result_type. Parameters: result_type (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_strain, "bvbrc_bioset_result_get_by_strain", "strain", "Get bioset_result by strain. Parameters: strain (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_taxon_id, "bvbrc_bioset_result_get_by_taxon_id", "taxon_id", "Get bioset_result by taxon_id. Parameters: taxon_id (int); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_uniprot_id, "bvbrc_bioset_result_get_by_uniprot_id", "uniprot_id", "Get bioset_result by uniprot_id. Parameters: uniprot_id (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_other_id, "bvbrc_bioset_result_get_by_other_id", "other_id", "Get bioset_result by other_id. Parameters: other_id (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_treatment_name, "bvbrc_bioset_result_get_by_treatment_name", "treatment_name", "Get bioset_result by treatment_name. Parameters: treatment_name (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_treatment_type, "bvbrc_bioset_result_get_by_treatment_type", "treatment_type", "Get bioset_result by treatment_type. Parameters: treatment_type (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_treatment_amount, "bvbrc_bioset_result_get_by_treatment_amount", "treatment_amount", "Get bioset_result by treatment_amount. Parameters: treatment_amount (str); limit; select; sort")
    gen_simple_tool(query_bioset_result_by_treatment_duration, "bvbrc_bioset_result_get_by_treatment_duration", "treatment_duration", "Get bioset_result by treatment_duration. Parameters: treatment_duration (str); limit; select; sort")

    # Range tools (two numeric args)
    def gen_range_tool(func, name: str, p1: str, p2: str, desc: str):
        @tool(name=name, description=desc)
        def _inner(min_value: float, max_value: float, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:  # type: ignore
            try:
                return format_query_result(func(min_value, max_value, build_options(limit, select, sort), base_url))
            except Exception as e:
                return f"Error querying {name}: {str(e)}"
        return _inner

    gen_range_tool(query_bioset_result_by_counts_range, "bvbrc_bioset_result_get_by_counts_range", "min_counts", "max_counts", "Get bioset_result by counts range. Parameters: min_counts (float), max_counts (float); limit; select; sort")
    gen_range_tool(query_bioset_result_by_fpkm_range, "bvbrc_bioset_result_get_by_fpkm_range", "min_fpkm", "max_fpkm", "Get bioset_result by fpkm range. Parameters: min_fpkm (float), max_fpkm (float); limit; select; sort")
    gen_range_tool(query_bioset_result_by_log2_fc_range, "bvbrc_bioset_result_get_by_log2_fc_range", "min_log2_fc", "max_log2_fc", "Get bioset_result by log2_fc range. Parameters: min_log2_fc (float), max_log2_fc (float); limit; select; sort")
    gen_range_tool(query_bioset_result_by_p_value_range, "bvbrc_bioset_result_get_by_p_value_range", "min_p_value", "max_p_value", "Get bioset_result by p_value range. Parameters: min_p_value (float), max_p_value (float); limit; select; sort")
    gen_range_tool(query_bioset_result_by_tpm_range, "bvbrc_bioset_result_get_by_tpm_range", "min_tpm", "max_tpm", "Get bioset_result by tpm range. Parameters: min_tpm (float), max_tpm (float); limit; select; sort")
    gen_range_tool(query_bioset_result_by_other_value_range, "bvbrc_bioset_result_get_by_other_value_range", "min_value", "max_value", "Get bioset_result by other_value range. Parameters: min_value (float), max_value (float); limit; select; sort")
    gen_range_tool(query_bioset_result_by_z_score_range, "bvbrc_bioset_result_get_by_z_score_range", "min_z_score", "max_z_score", "Get bioset_result by z_score range. Parameters: min_z_score (float), max_z_score (float); limit; select; sort")

    @tool(name="bvbrc_bioset_result_get_by_version", description="Get bioset_result by version. Parameters: version (int); limit; select; sort")
    def bvbrc_bioset_result_get_by_version(version: int, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_version(version, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by version: {str(e)}"

    @tool(name="bvbrc_bioset_result_get_by_date_inserted_range", description="Get bioset_result by date_inserted range. Parameters: start_date (YYYY-MM-DD), end_date (YYYY-MM-DD); limit; select; sort")
    def bvbrc_bioset_result_get_by_date_inserted_range(start_date: str, end_date: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_date_inserted_range(start_date, end_date, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by date_inserted range: {str(e)}"

    @tool(name="bvbrc_bioset_result_get_by_date_modified_range", description="Get bioset_result by date_modified range. Parameters: start_date (YYYY-MM-DD), end_date (YYYY-MM-DD); limit; select; sort")
    def bvbrc_bioset_result_get_by_date_modified_range(start_date: str, end_date: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_date_modified_range(start_date, end_date, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by date_modified range: {str(e)}"

    @tool(name="bvbrc_bioset_result_search_by_keyword", description="Search bioset_result by keyword. Parameters: keyword (str); limit; select; sort")
    def bvbrc_bioset_result_search_by_keyword(keyword: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_keyword(keyword, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error searching bioset_result by keyword: {str(e)}"

    @tool(name="bvbrc_bioset_result_get_all", description="Get all bioset_result data. Parameters: limit; select; sort")
    def bvbrc_bioset_result_get_all(limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_all({"limit": limit, **({"select": select.split(",")} if select else {}), **({"sort": sort} if sort else {})}, base_url))
        except Exception as e:
            return f"Error querying all bioset_result: {str(e)}"


