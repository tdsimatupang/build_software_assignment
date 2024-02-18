import pytest
from Analysis import Analysis  # replace 'your_script' with the name of your script

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
    # This is a bit tricky to test without a mock notification system
    # For now, we'll assume it's working if no error is thrown
