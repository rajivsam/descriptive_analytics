import yaml
import logging
from typing import Dict, Any, List
from relation_to_graph.util.path_validation_util import *
import pandas as pd

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.INFO)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

class EntityFilter:
    def __init__(self, config_file: str) ->None:
        """
        Initializes the parser with the given configuration file.

        Args:
            config_file (str): Path to the YAML configuration file.

        Raises:
            FileNotFoundError: If the specified config_file does not exist.
            yaml.YAMLError: If the configuration file cannot be parsed as valid YAML.
            ValueError: If the configuration file fails validation.
        """
        is_valid_config_file = valid_config_file(config_file)
        if not is_valid_config_file:
            logging.info("Check if file exists and has the right permissions")
        with open(config_file, "r") as file:
            self._r2g_cfg = yaml.safe_load(file)
        return
    
    def get_predictors(self) -> List[str]:
        """
        Returns the entity dictionary.

        Returns:
            dict[str, object]: The predictors dictionary.
        """

        pred_info = self._r2g_cfg["predictors"]

        pred_names = [ p["name"] for p in pred_info ]

        return pred_names
    
    def get_target(self) -> str:
        """
        Returns the target variable name.

        Returns:
            str: The target variable name.
        """

        target_info = self._r2g_cfg["target"]

        target_name = target_info["name"]

        return target_name
    
    def get_data_frame(self) -> pd.DataFrame:
        """
        Returns the data frame path.

        Returns:
            str: The data frame path.
        """

        prefix = "../data/sba_loans_data_raw/"
        df_path = prefix + self._r2g_cfg["raw_data"]["source_file"]
        df = pd.read_csv(df_path)
        df = df[self.get_predictors() + [self.get_target()]]

        return df

    

    
