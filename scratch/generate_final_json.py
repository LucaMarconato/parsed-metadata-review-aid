#!/usr/bin/env python3
"""Generate final JSON output conforming to spatialdata-db schema."""

import json
from extract_metadata import extract_metadata
from parse_metrics import parse_metrics_csv

def generate_final_json():
    """Create JSON output that conforms to the Visium schema."""

    # Extract data from sources
    html_metadata = extract_metadata('/Users/macbook/temp/claude_code/mouse_brain_dataset.html')
    csv_metrics = parse_metrics_csv('/Users/macbook/temp/claude_code/scratch/metrics_summary.csv')

    # Build metadata_general (sample-level schema)
    metadata_general = {
        "Product": "Spatial Gene Expression",
        "Assay": "visium spatial gene expression",
        "Biomaterial Type": "Specimen from Organism",
        "Organism": "Mus musculus",
        "Tissue": "brain",
        "Modality": "RNA",
        "Dataset Url": html_metadata['dataset_url'],
        "License": html_metadata['license'],
        "Publication Date": html_metadata['publication_date'],
        "Sample ID at Source": html_metadata['slide'],
        "Disease": "normal",
        "Chemistry Version": html_metadata['chemistry_version'],
        "Preservation Method": html_metadata['preservation_method'],
        "Staining Method": html_metadata['staining_method'],
        "Instrument(s)": html_metadata['sequencing_instrument'],
        "Software": f"Space Ranger v{html_metadata['software']}",
    }

    # Build metadata_visium (Visium-specific schema)
    metadata_visium = {
        "Sequencing Configuration": html_metadata['sequencing_configuration'],
        "Slide Area": html_metadata['slide_area'],
        "Number of Spots": csv_metrics['number_of_spots'],
        "Genes Detected": csv_metrics['total_genes_detected'],
        "Median Genes per Spot": csv_metrics['median_genes_per_spot'],
        "Mean Reads per Spot": csv_metrics['mean_reads_per_spot'],
        "Transcriptome": "mm10-2020-A",
        "Microscope": "Nikon Ti2-E microscope",
        "Objective": "10X objective",
        "Numerical Aperture": html_metadata['numerical_aperture'],
        "Camera": "Color camera",
        "Exposure": html_metadata['exposure'],
        "Gain": html_metadata['gain'],
    }

    # Combine into final structure
    output = {
        "metadata_general": metadata_general,
        "metadata_visium": metadata_visium
    }

    return output

if __name__ == '__main__':
    output_data = generate_final_json()

    output_file = '/Users/macbook/temp/claude_code/mouse_brain_sagittal_posterior_section_2.json'
    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=4)

    print(f"Final JSON output saved to: {output_file}")
    print(f"\nJSON Preview:")
    print(json.dumps(output_data, indent=2))
