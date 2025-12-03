# Metadata Visualizer - Usage Guide

## Overview

The spatialdata-db-visualizer skill creates a self-contained HTML file that allows you to visually verify parsed metadata against the original source documents.

## Prerequisites

Before using this skill, you should have:

1. **Parsed metadata JSON** - Output from the spatialdata-db-parser skill
2. **Source HTML files** - The cached HTML pages used during parsing
3. **Mapping file** - A JSON file linking each metadata field to text excerpts in the source documents

## Creating the Mapping File

The mapping file is crucial for the visualizer to work. It connects each metadata field to the specific text excerpts in the source HTML where the value was found.

### Format

```json
{
  "FieldName": {
    "value": "extracted value",
    "excerpts": [
      {
        "file": "source_file.html",
        "text": "text to highlight",
        "context": "surrounding text for context (optional)"
      }
    ]
  }
}
```

### Example

See `example_mapping.json` in this directory for a complete example.

### Generating the Mapping File

You can either:

1. **Manual creation**: Create the mapping file by hand while parsing
2. **Automated**: Modify the spatialdata-db-parser skill to output the mapping file alongside the JSON
3. **Post-processing**: Write a script to match parsed values back to the source HTML

## Using the Visualizer Skill

### Input Files Required

1. `metadata.json` - The parsed metadata
2. `source_file_1.html`, `source_file_2.html`, ... - Source HTML files
3. `mapping.json` - The field-to-excerpt mapping

### Example Usage

```
Use the spatialdata-db-visualizer skill to create a viewer for:
- Metadata: /path/to/metadata.json
- Sources: /path/to/source1.html, /path/to/source2.html
- Mapping: /path/to/mapping.json
```

### Output

The skill will generate a single HTML file (e.g., `metadata_viewer.html`) that you can open in any web browser.

## Features of the Generated HTML

### Sidebar (Left)
- Shows all metadata fields organized by category:
  - Sample Level
  - Xenium Specific
  - Visium Specific
- Each field displays its name and parsed value
- Click on any field to see where the value came from

### Tab Bar (Top)
- One tab for each source HTML file
- Tabs are highlighted in orange when they contain excerpts for the selected field
- Click to switch between different source documents

### Document Viewer (Center)
- Displays the selected HTML document
- When you click a metadata field, relevant text is highlighted in orange
- Automatically scrolls to the first highlighted excerpt

### Controls
- **Clear Highlights** button to reset the view

## Workflow Example

1. **Parse metadata**:
   ```
   Use spatialdata-db-parser skill on https://example.com/dataset.html
   ```

2. **Create mapping** (while parsing or after):
   - Note which text excerpts contain each field value
   - Save to `mapping.json`

3. **Generate visualizer**:
   ```
   Use spatialdata-db-visualizer skill with:
   - metadata.json
   - dataset.html
   - mapping.json
   ```

4. **Verify metadata**:
   - Open the generated HTML file
   - Click through each metadata field
   - Verify the highlighted text matches the extracted value
   - Check for any extraction errors

## Tips

- **Exact text matching**: The `text` field in mapping should be the exact string to highlight
- **Multiple excerpts**: A field can have multiple excerpts if the value appears in multiple places
- **Multiple files**: Excerpts can come from different source files
- **Context**: The `context` field is optional but helps with better matching when the same text appears multiple times

## Troubleshooting

### Highlights not appearing
- Check that the `text` field in mapping.json exactly matches the text in the HTML
- Ensure the `file` field matches the actual filename

### Wrong text highlighted
- The text matcher is case-sensitive
- Check for extra spaces or special characters

### Page too slow
- Large HTML files may take time to render
- Consider splitting very large source documents

## Technical Details

- **Self-contained**: No internet connection required
- **No dependencies**: Pure HTML/CSS/JavaScript
- **Browser compatibility**: Works in all modern browsers (Chrome, Firefox, Safari, Edge)
- **File protocol**: Can be opened directly from filesystem (file://)

## Security Note

The generated HTML embeds the source HTML content. Ensure your source files don't contain sensitive information before sharing the visualizer file.
