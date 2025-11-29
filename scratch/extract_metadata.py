#!/usr/bin/env python3
"""Extract metadata from 10x Genomics HTML page."""

import re
import json

def extract_metadata(html_path):
    """Extract all metadata from the HTML file."""
    with open(html_path, 'r') as f:
        html = f.read()

    # Extract comprehensive metadata
    metadata = {
        # From URL and title
        'dataset_url': 'https://www.10xgenomics.com/datasets/mouse-brain-serial-section-2-sagittal-posterior-1-standard-1-0-0',
        'product': 'Spatial Gene Expression',
        'assay': 'visium spatial gene expression',
        'biomaterial_type': 'Specimen from Organism',
        'organism': 'Mus musculus',
        'tissue': 'brain',
        'modality': 'RNA',
        'disease': 'normal',
        'license': 'Creative Commons Attribution 4.0 International',
    }

    # Extract from HTML content
    patterns = {
        'sex': r'Sex:\s*(\w+)',
        'age': r'Age:\s*([^<\n]+)',
        'strain': r'Strain:\s*([^<\n]+)',
        'section_orientation': r'Section Orientation:\s*([^<\n]+)',
        'numerical_aperture': r'Numerical Aperture:\s*([^<\n]+)',
        'exposure': r'Exposure:\s*([^<\n]+)',
        'gain': r'Gain:\s*([^<\n]+)',
        'sequencing_instrument': r'Sequencing instrument:\s*([^<\n]+)',
        'sequencing_depth': r'Sequencing Depth:\s*([^<\n]+)',
        'sequencing_configuration': r'Sequencing Configuration:\s*([^<\n]+)',
        'slide': r'Slide:\s*([^<\n]+)',
        'slide_area': r'Area:\s*([^<\n]+)',
        'spots_detected': r'Spots detected under tissue:\s*([0-9,]+)',
        'median_umi': r'Median UMI counts per spot:\s*([0-9,]+)',
        'median_genes_per_spot': r'Median genes per spot:\s*([0-9,]+)',
        'software': r'Space Ranger\s+([v0-9\.]+)',
        'publication_date': r'([0-9]{4}-[0-9]{2}-[0-9]{2})',
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, html)
        if match:
            value = match.group(1).strip()
            # Convert numeric values
            if key in ['spots_detected', 'median_umi', 'median_genes_per_spot']:
                value = int(value.replace(',', ''))
            else:
                # Clean HTML entities for string values
                value = value.replace('&gt;', '>').replace('&lt;', '<').replace('&amp;', '&')
            metadata[key] = value

    # Search for preservation method
    if re.search(r'Fresh Frozen', html, re.IGNORECASE):
        metadata['preservation_method'] = 'Fresh Frozen'
    elif re.search(r'FFPE', html, re.IGNORECASE):
        metadata['preservation_method'] = 'FFPE'

    # Search for staining
    if re.search(r'H&amp;E|H&E', html, re.IGNORECASE):
        metadata['staining_method'] = 'H&E'

    # Search for chemistry version
    metadata['chemistry_version'] = 'Visium v1'

    return metadata

if __name__ == '__main__':
    html_file = '/Users/macbook/temp/claude_code/mouse_brain_dataset.html'
    metadata = extract_metadata(html_file)
    print(json.dumps(metadata, indent=2))
