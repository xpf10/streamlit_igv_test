import streamlit as st
import streamlit.components.v1 as components
import json

# IGV browser options
igv_options = {
    "genome": "mm39",
    "locus": "chr1:0-1280",
    "tracks": [
        {
            "name": "Example Track",
            "url": "http://127.0.0.1:8000/Target2.bam.rmdup.bigwig",
            "format": "bigwig",
            "type": "wig"
        }
    ]
}

# Convert options to JSON to pass into the HTML
options_json = json.dumps(igv_options)

# Read and inject options into HTML
with open("igv_browser.html", "r") as f:
    html_template = f.read().replace('{{ igv_options|tojson|safe }}', options_json)

# Render the HTML with Streamlit components
components.html(html_template, height=600)
