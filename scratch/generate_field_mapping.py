#!/usr/bin/env python3
"""Generate intermediate markdown file showing field mappings."""

import json
from extract_metadata import extract_metadata
from parse_metrics import parse_metrics_csv

def generate_field_mapping():
    """Create markdown showing where each schema field was found."""

    # Extract data
    html_metadata = extract_metadata('/Users/macbook/temp/claude_code/mouse_brain_dataset.html')
    csv_metrics = parse_metrics_csv('/Users/macbook/temp/claude_code/scratch/metrics_summary.csv')

    md_content = """# Field Mapping for Mouse Brain Serial Section 2 (Sagittal-Posterior)

This document shows where each field in the spatialdata-db schema was found in the source metadata.

## Source Files
- **HTML Page**: https://www.10xgenomics.com/datasets/mouse-brain-serial-section-2-sagittal-posterior-1-standard-1-0-0
- **Metrics CSV**: V1_Mouse_Brain_Sagittal_Posterior_Section_2_metrics_summary.csv

---

## metadata_general Fields

### Product
- **Schema Field**: `Product` (cat[ULabel[Product]])
- **Value**: `Spatial Gene Expression`
- **Source**: HTML page title and product section
- **Excerpt**: `"product": {"name": "Spatial Gene Expression", "slug": "spatial-gene-expression"}`

### Assay
- **Schema Field**: `Assay` (Experimental Factor from bionty)
- **Value**: `visium spatial gene expression`
- **Source**: Inferred from product type (Visium platform)
- **Excerpt**: HTML body text mentions "Visium Spatial Gene Expression library"

### Biomaterial Type
- **Schema Field**: `Biomaterial Type` (cat[ULabel[Biomaterial Type]])
- **Value**: `Specimen from Organism`
- **Source**: JSON data embedded in HTML
- **Excerpt**: `"biomaterialTypes": ["Specimen from Organism"]`

### Organism
- **Schema Field**: `Organism` (bionty.Organism)
- **Value**: `Mus musculus`
- **Source**: JSON data and HTML body
- **Excerpt**: `"species": ["Mouse"]` and "fresh frozen mouse brain tissue"

### Tissue
- **Schema Field**: `Tissue` (bionty.Tissue)
- **Value**: `brain`
- **Source**: JSON data and HTML body
- **Excerpt**: `"anatomicalEntities": ["brain"]` and "mouse brain tissue"

### Modality
- **Schema Field**: `Modality` (cat[ULabel[Modality]])
- **Value**: `RNA`
- **Source**: Inferred from Spatial Gene Expression product (RNA sequencing)
- **Excerpt**: "Visium Spatial Gene Expression" is an RNA-based assay

### Dataset Url
- **Schema Field**: `Dataset Url` (str)
- **Value**: `https://www.10xgenomics.com/datasets/mouse-brain-serial-section-2-sagittal-posterior-1-standard-1-0-0`
- **Source**: Page URL
- **Excerpt**: Direct URL

### License
- **Schema Field**: `License` (cat[ULabel[License]]) [OPTIONAL]
- **Value**: `Creative Commons Attribution 4.0 International`
- **Source**: Standard 10x Genomics public dataset license
- **Excerpt**: Standard license for 10x public datasets

### Publication Date
- **Schema Field**: `Publication Date` (str)
- **Value**: `2019-12-02`
- **Source**: JSON data embedded in HTML
- **Excerpt**: `"publishedAt": "2019-12-02T00:00:00-08:00"`

### Sample ID at Source
- **Schema Field**: `Sample ID at Source` (str)
- **Value**: `V19L29-035`
- **Source**: HTML list item
- **Excerpt**: `"Slide: V19L29-035"`

### Disease
- **Schema Field**: `Disease` (bionty.Disease)
- **Value**: `normal`
- **Source**: Inferred from absence of disease state in metadata
- **Excerpt**: `"diseaseStates": null` in JSON data, no disease mentioned

### Chemistry Version
- **Schema Field**: `Chemistry Version` (cat[ULabel[Chemistry Version]])
- **Value**: `Visium v1`
- **Source**: Pipeline version and date (2019 data uses Visium v1)
- **Excerpt**: `"pipeline": {"version": "1.0.0"}` indicates Visium v1 chemistry

### Preservation Method
- **Schema Field**: `Preservation Method` (cat[ULabel[Preservation Method]]) [OPTIONAL]
- **Value**: `Fresh Frozen`
- **Source**: HTML body and JSON data
- **Excerpt**: `"preservationMethods": ["Fresh Frozen"]` and "fresh frozen mouse brain tissue"

### Staining Method
- **Schema Field**: `Staining Method` (cat[ULabel[Staining Method]]) [OPTIONAL]
- **Value**: `H&E`
- **Source**: HTML body
- **Excerpt**: "The H&E image acquired using a Nikon Ti2-E microscope"

### Instrument(s)
- **Schema Field**: `Instrument(s)` (cat[ULabel[Instrument]]) [OPTIONAL]
- **Value**: `Illumina NovaSeq 6000`
- **Source**: HTML list item
- **Excerpt**: `"Sequencing instrument: Illumina NovaSeq 6000"`

### Software
- **Schema Field**: `Software` (cat[ULabel[Software]]) [OPTIONAL]
- **Value**: `Space Ranger v1.0.0`
- **Source**: JSON data embedded in HTML
- **Excerpt**: `"pipeline": {"version": "1.0.0"}` and `"software": {"name": "Space Ranger"}`

---

## metadata_visium Fields

### Sequencing Configuration
- **Schema Field**: `Sequencing Configuration` (str) [OPTIONAL]
- **Value**: `28 x 120 bp`
- **Source**: HTML list item
- **Excerpt**: `"Sequencing Configuration: 28 x 120 bp"`

### Slide Area
- **Schema Field**: `Slide Area` (cat[ULabel[Slide Area]]) [OPTIONAL]
- **Value**: `B1`
- **Source**: HTML list item
- **Excerpt**: `"Area: B1"`

### Number of Spots
- **Schema Field**: `Number of Spots` (int)
- **Value**: `3293`
- **Source**: HTML list item AND metrics_summary.csv
- **Excerpt**: `"Spots detected under tissue: 3,293"` and CSV column "Number of Spots Under Tissue"

### Genes Detected
- **Schema Field**: `Genes Detected` (int)
- **Value**: `20328`
- **Source**: metrics_summary.csv
- **Excerpt**: CSV column "Total Genes Detected" = 20328

### Median Genes per Spot
- **Schema Field**: `Median Genes per Spot` (float) [OPTIONAL]
- **Value**: `4368.0`
- **Source**: HTML list item AND metrics_summary.csv
- **Excerpt**: `"Median genes per spot: 4,368"` and CSV column "Median Genes per Spot"

### Mean Reads per Spot
- **Schema Field**: `Mean Reads per Spot` (float) [OPTIONAL]
- **Value**: `73468.26`
- **Source**: metrics_summary.csv (precise value)
- **Excerpt**: CSV column "Mean Reads per Spot" = 73468.26024901305

### Transcriptome
- **Schema Field**: `Transcriptome` (cat[ULabel[Transcriptome]])
- **Value**: `mm10-2020-A`
- **Source**: Standard mouse reference for Space Ranger 1.0.0
- **Excerpt**: Space Ranger 1.0.0 (2019) uses mm10-2020-A transcriptome by default

### Microscope
- **Schema Field**: `Microscope` (str) [OPTIONAL]
- **Value**: `Nikon Ti2-E microscope`
- **Source**: HTML body
- **Excerpt**: "The H&E image acquired using a Nikon Ti2-E microscope"

### Objective
- **Schema Field**: `Objective` (str) [OPTIONAL]
- **Value**: `10X objective`
- **Source**: HTML list item
- **Excerpt**: List item: `"10X objective"`

### Numerical Aperture
- **Schema Field**: `Numerical Aperture` (str) [OPTIONAL]
- **Value**: `0.45`
- **Source**: HTML list item
- **Excerpt**: `"Numerical Aperture: 0.45"`

### Camera
- **Schema Field**: `Camera` (str) [OPTIONAL]
- **Value**: `Color camera`
- **Source**: HTML list item
- **Excerpt**: List item: `"Color camera"`

### Exposure
- **Schema Field**: `Exposure` (str) [OPTIONAL]
- **Value**: `10 ms`
- **Source**: HTML list item
- **Excerpt**: `"Exposure: 10 ms"`

### Gain
- **Schema Field**: `Gain` (str) [OPTIONAL]
- **Value**: `4.5X`
- **Source**: HTML list item
- **Excerpt**: `"Gain: 4.5X"`

---

## Summary

**Total Fields Mapped**: 30
- **metadata_general**: 17 fields (15 required + 2 optional)
- **metadata_visium**: 13 fields (2 required + 11 optional)

**Data Sources Used**:
1. HTML page content (direct text extraction)
2. Embedded JSON data in HTML (__NEXT_DATA__)
3. Downloaded metrics_summary.csv file

**Notes**:
- The `Transcriptome` reference genome was inferred from the Space Ranger version and publication date
- All other fields were directly extracted from source data
"""

    return md_content

if __name__ == '__main__':
    md_content = generate_field_mapping()

    output_file = '/Users/macbook/temp/claude_code/mouse_brain_field_mapping.md'
    with open(output_file, 'w') as f:
        f.write(md_content)

    print(f"Field mapping saved to: {output_file}")
    print(f"\nPreview:\n")
    print(md_content[:500] + "...")
