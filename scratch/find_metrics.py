#!/usr/bin/env python3
"""Search for metrics data in the JSON."""

import json

def find_metrics():
    """Find metrics in embedded JSON data."""
    with open('/Users/macbook/temp/claude_code/scratch/embedded_data.json', 'r') as f:
        data = json.load(f)

    print("Searching for metrics data...\n")

    # Check filesetMap
    fileset_map = data['props']['pageProps'].get('filesetMap', {})
    print(f"filesetMap keys: {list(fileset_map.keys())}\n")

    # Recursively search for 'genes' or 'metrics' keys
    def search_dict(d, path=""):
        results = []
        if isinstance(d, dict):
            for k, v in d.items():
                current_path = f"{path}.{k}" if path else k
                if any(keyword in k.lower() for keyword in ['gene', 'metric', 'spot', 'count']):
                    results.append((current_path, v))
                results.extend(search_dict(v, current_path))
        elif isinstance(d, list):
            for i, item in enumerate(d):
                results.extend(search_dict(item, f"{path}[{i}]"))
        return results

    print("Searching for gene/metric-related keys...\n")
    findings = search_dict(data)

    if findings:
        for path, value in findings[:20]:  # Limit to first 20
            if isinstance(value, (str, int, float, bool)):
                print(f"{path}: {value}")
            elif isinstance(value, (list, dict)):
                value_preview = str(value)[:100]
                print(f"{path}: {value_preview}...")
    else:
        print("No specific metric fields found in JSON")

    # Since we can't find genes detected in the HTML, we may need to estimate or
    # acknowledge it's not available
    print("\n\nNote: 'Genes Detected' (total unique genes) not found in webpage.")
    print("This is a required field in the schema.")
    print("Options:")
    print("1. Download and parse the metrics_summary.csv file")
    print("2. Use a reasonable estimate based on median genes per spot")
    print("3. Mark as unavailable/unknown")

if __name__ == '__main__':
    find_metrics()
