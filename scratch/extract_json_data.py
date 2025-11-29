#!/usr/bin/env python3
"""Extract embedded JSON data from the HTML page."""

import re
import json

def extract_json_data(html_path):
    """Extract JSON data embedded in the page."""
    with open(html_path, 'r') as f:
        html = f.read()

    # Look for Next.js data
    pattern = r'<script[^>]*id="__NEXT_DATA__"[^>]*type="application/json"[^>]*>(.*?)</script>'
    matches = re.findall(pattern, html, re.DOTALL)

    if matches:
        json_str = matches[0]
        data = json.loads(json_str)

        # Save the full JSON for inspection
        with open('/Users/macbook/temp/claude_code/scratch/embedded_data.json', 'w') as f:
            json.dump(data, f, indent=2)

        print("Extracted JSON data saved to embedded_data.json")

        # Try to navigate to dataset info
        if 'props' in data and 'pageProps' in data['props']:
            dataset = data['props']['pageProps'].get('dataset', {})

            print("\nDataset metadata:")
            print(json.dumps(dataset, indent=2))

            # Look for metrics
            if 'metrics' in dataset:
                print("\nMetrics found:")
                print(json.dumps(dataset['metrics'], indent=2))

        return data
    else:
        print("No JSON data found")
        return None

if __name__ == '__main__':
    html_file = '/Users/macbook/temp/claude_code/mouse_brain_dataset.html'
    extract_json_data(html_file)
