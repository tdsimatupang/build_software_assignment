# Non-Automated Tests for Analysis Script

This document outlines the non-automated tests that should be performed to ensure the correct functioning of the Analysis script.

1. **Configuration File Test**: Manually check if the 'system_config.yml' file exists in the correct directory and has the appropriate structure and content.

2. **Data Loading Test**: After running the `load_data()` function, manually inspect the `data` attribute of the `Analysis` object to ensure the data has been loaded correctly.

3. **Data Analysis Test**: After running the `compute_analysis()` function, manually inspect the output to ensure it is a list and contains expected results.

4. **Data Plotting Test**: After running the `plot_data()` function, manually inspect the generated plot to ensure it visualizes the data correctly.

5. **Notification Test**: After running the `notify_done()` function, manually check the notification system (e.g., email, logs) to ensure the notification "Analysis complete!" has been sent.

Please note that these tests are meant to supplement the automated tests, not replace them. Always run the automated tests first.
