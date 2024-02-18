import requests
import yaml
import matplotlib.pyplot as plt
import logging
from typing import Any, Optional
from plyer import notification

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Analysis():
    """
    A class used to perform an analysis using data from the NASA Near Earth Object API.

    Attributes
    ----------
    config : dict
        a dictionary holding the configuration for the analysis
    data : dict
        a dictionary holding the data loaded from the API

    """

    def __init__(self, analysis_config: str) -> None:
        """
        Parameters
        ----------
        analysis_config : str
            path to the analysis configuration file

        Returns
        -------
        analysis_obj : Analysis
            Analysis object containing consolidated parameters from the configuration files

        Notes
        -----
        Constructs all the necessary attributes for the Analysis object.
        The configuration files should include parameters for:
            * GitHub API token
            * Plot color
            * Plot title
            * Plot x and y axis titles
            * Figure size
            * Default save path
        """

        CONFIG_PATHS = ['system_config.yml', 'user_config.yml']

        # add the analysis config to the list of paths to load
        paths = CONFIG_PATHS + [analysis_config]

        # initialize empty dictionary to hold the configuration
        config = {}

        # load each config file and update the config dictionary
        for path in paths:
            with open(path, 'r') as f:
                this_config = yaml.safe_load(f)
            config.update(this_config)

        self.config = config
        self.data = None

    def load_data(self) -> None:
        """
        Load data from the NASA Near Earth Object API.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        This method sends a GET request to the API, parses the JSON response, 
        and stores it in the data attribute of the Analysis object.
        """
        try:
            # API endpoint URL
            api_url = "https://api.nasa.gov/neo/rest/v1/feed"

            # Parameters for the request
            params = {
            'start_date': '2024-01-01',
            'end_date': '2024-01-07',
            'api_key': 'Mpcd3Ntz24s9dKXmhEvd9utKpYiw36mkxyyjOeMr'
            }

            # Make a GET request to the API
            response = requests.get(api_url, params=params)
            response.raise_for_status()

            # Parse the JSON response and store it in the data attribute
            self.data = response.json()
        except requests.exceptions.HTTPError as err:
            logger.error(f"HTTP error occurred: {err}")
        except Exception as err:
            logger.error(f"Other error occurred: {err}")

    def compute_analysis(self) -> Any:
        """
        Compute the analysis using the loaded data.

        Parameters
        ----------
        None

        Returns
        -------
        tuple
            A tuple containing a list of dictionaries, each containing the name, estimated diameter, 
            and potentially hazardous status of a near earth object, and the mean and median of the estimated diameters.

        Notes
        -----
        This method loops over each date in the near earth objects data and 
        extracts the fields of interest. It then creates a dictionary with 
        the extracted data and adds it to the results list.
        """
        # Initialize an empty list to hold the results
        results = []

        # Loop over each date in the near earth objects data
        for date in self.data['near_earth_objects']:
            # Loop over each near earth object for this date
            for neo in self.data['near_earth_objects'][date]:
                # Extract the fields you're interested in
                name = neo['name']
                estimated_diameter = neo['estimated_diameter']['meters']['estimated_diameter_max']
                potentially_hazardous = neo['is_potentially_hazardous_asteroid']

                # Create a dictionary with the extracted data and add it to the results list
                results.append({
                    'Name': name,
                    'Estimated Diameter (meters)': estimated_diameter,
                    'Potentially Hazardous': potentially_hazardous
                })

        # Extract the estimated diameters into a list
        diameters = [result['Estimated Diameter (meters)'] for result in results]

        # Calculate the mean and median
        mean_diameter = sum(diameters) / len(diameters)
        median_diameter = sorted(diameters)[len(diameters) // 2]

        # Return the results list, mean and median diameter
        return results, mean_diameter, median_diameter


    def plot_data(self, save_path: Optional[str] = None) -> plt.Figure:
        """
        Analyze and plot data.

        Generates a plot, display it to screen, and save it to the path in the parameter `save_path`, or 
        the path from the configuration file if not specified.

        Parameters
        ----------
        save_path : str, optional
            Save path for the generated figure

        Returns
        -------
        fig : matplotlib.Figure
        """
        # Implement your plotting here
        # For now, let's just create an empty figure
        fig = plt.figure()
        title = self.config.get('figure_title', 'Default Title')
        plt.title(title)
        plt.xlabel(self.config.get('x_axis_title', 'Default X-axis Title'))  # handle missing x_axis_title
        plt.ylabel(self.config.get('y_axis_title', 'Default Y-axis Title'))  # handle missing y_axis_title
        if save_path is not None:
            plt.savefig(save_path)
        return fig


    def notify_done(self, message: str) -> None:
        """
        Send a notification with the provided message.

        Parameters
        ----------
        message : str
            The message to be included in the notification.

        Returns
        -------
        None

        Notes
        -----
        This method sends a notification with the provided message.
        """
        notification.notify(
            title='Analysis Complete',
            message=message,
            timeout=10
        )

if __name__ == "__main__":
    analysis = Analysis('system_config.yml')
    analysis.load_data()
    results = analysis.compute_analysis()
    results, mean_diameter, median_diameter = analysis.compute_analysis()

    # Print each result in the desired format
    for result in results:
        print(f"Name: {result['Name']}")
        print(f"Estimated Diameter (meters): {result['Estimated Diameter (meters)']}")
        print(f"Potentially Hazardous: {result['Potentially Hazardous']}")
        print("------")
    
    # Print the mean and median diameter
    print(f"Mean Diameter (meters): {mean_diameter}")
    print(f"Median Diameter (meters): {median_diameter}")

    analysis.notify_done("Analysis complete!")
