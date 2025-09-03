# test_dash_app.py

import dash
from dash import html, dcc
import pytest

# Assume your actual app is imported as 'app' from 'app.py'
from app import app

def test_header_is_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element('.header-class')  # Replace with actual class or id
    assert header is not None
    assert 'Expected Header Text' in header.text  # Edit to match header content

def test_visualisation_is_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element('#visualisation-id')  # Replace with actual graph id
    assert graph is not None

def test_region_picker_is_present(dash_duo):
    dash_duo.start_server(app)
    dropdown = dash_duo.find_element('#region-filter')  # Replace with actual dropdown id
    assert dropdown is not None
