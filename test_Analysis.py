import pytest
from Analysis import Analysis

def test_init():
    analysis = Analysis('system_config.yml')
    assert isinstance(analysis, Analysis)
    assert analysis.config is not None

def test_load_data():
    analysis = Analysis('system_config.yml')
    analysis.load_data()
    assert analysis.data is not None

def test_compute_analysis():
    analysis = Analysis('system_config.yml')
    analysis.load_data()
    results = analysis.compute_analysis()
    assert isinstance(results[0], list)
    assert len(results) > 0

def test_plot_data():
    analysis = Analysis('system_config.yml')
    analysis.load_data()
    results = analysis.compute_analysis()
    fig = analysis.plot_data()
    assert fig is not None

def test_notify_done():
    analysis = Analysis('system_config.yml')
    analysis.load_data()
    results = analysis.compute_analysis()
    analysis.notify_done("Analysis complete!")
