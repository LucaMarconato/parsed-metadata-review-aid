#!/usr/bin/env python3
"""Search for total genes detected in the HTML."""

import re

def search_genes_detected(html_path):
    """Search for genes detected information."""
    with open(html_path, 'r') as f:
        html = f.read()

    print("Searching for 'Genes Detected' information:\n")

    # Extract all text content from list items
    all_li = re.findall(r'<li[^>]*>([^<]+(?:<[^>]+>[^<]*</[^>]+>)*[^<]*)</li>', html)
    print(f"Found {len(all_li)} list items\n")

    # Clean and print all list items
    print("All list items:")
    for i, item in enumerate(all_li, 1):
        clean = re.sub(r'<[^>]+>', '', item)
        clean = clean.replace('&gt;', '>').replace('&lt;', '<').replace('&amp;', '&')
        if clean.strip():
            print(f"  {i}. {clean.strip()}")

    # Search for any mention of genes (total, detected, unique, etc.)
    print("\n\nSearching for gene-related metrics in full HTML:")
    gene_patterns = [
        r'Total\s+genes[^:]*:\s*([0-9,]+)',
        r'([0-9,]+)\s+total\s+genes',
        r'Genes\s+detected[^:]*:\s*([0-9,]+)',
        r'([0-9,]+)\s+genes\s+detected',
        r'Unique\s+genes[^:]*:\s*([0-9,]+)',
        r'([0-9,]+)\s+unique\s+genes',
    ]

    for pattern in gene_patterns:
        matches = re.findall(pattern, html, re.IGNORECASE)
        if matches:
            print(f"  Pattern '{pattern}': {matches}")

    # Search for tables or divs that might contain metrics
    print("\n\nSearching for metric tables or sections:")
    table_sections = re.findall(r'<table[^>]*>.*?</table>', html, re.DOTALL | re.IGNORECASE)
    print(f"  Found {len(table_sections)} table(s)")

    # Look for JSON data embedded in the page
    print("\n\nSearching for JSON data:")
    json_patterns = [
        r'<script[^>]*type=["\']application/json["\'][^>]*>(.*?)</script>',
        r'window\.__NEXT_DATA__\s*=\s*({.*?});',
    ]

    for pattern in json_patterns:
        matches = re.findall(pattern, html, re.DOTALL)
        if matches:
            print(f"  Found {len(matches)} JSON block(s)")
            for i, match in enumerate(matches[:2], 1):
                snippet = match[:200] if len(match) > 200 else match
                print(f"    Block {i} preview: {snippet}...")

if __name__ == '__main__':
    html_file = '/Users/macbook/temp/claude_code/mouse_brain_dataset.html'
    search_genes_detected(html_file)
