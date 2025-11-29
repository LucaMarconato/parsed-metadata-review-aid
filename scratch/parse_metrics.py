#!/usr/bin/env python3
"""Parse the metrics_summary.csv file."""

import csv
import json

def parse_metrics_csv(csv_path):
    """Parse metrics from CSV file."""
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        row = next(reader)  # Get first (and only) row

    metrics = {
        'total_genes_detected': int(row['Total Genes Detected']),
        'number_of_spots': int(row['Number of Spots Under Tissue']),
        'median_genes_per_spot': float(row['Median Genes per Spot']),
        'median_umi_per_spot': float(row['Median UMI Counts per Spot']),
        'mean_reads_per_spot': float(row['Mean Reads per Spot']),
        'fraction_reads_in_spots': float(row['Fraction Reads in Spots Under Tissue']),
        'reads_mapped_to_genome': float(row['Reads Mapped to Genome']),
        'sequencing_saturation': float(row['Sequencing Saturation']),
    }

    return metrics

if __name__ == '__main__':
    csv_file = '/Users/macbook/temp/claude_code/scratch/metrics_summary.csv'
    metrics = parse_metrics_csv(csv_file)
    print("Parsed Metrics:")
    print(json.dumps(metrics, indent=2))
