import yaml
import logging
from typing import Dict, Any
from relation_to_graph.util.path_validation_util import *

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.INFO)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

class HomoR2GMapperExplicit:
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
    
    def get_entity(self) -> dict[str, object]:
        """
        Returns the entity dictionary.

        Returns:
            dict[str, object]: The configuration dictionary loaded from the YAML file.
        """
        entity_dict = {}
        for entity_desc in self._r2g_cfg["entities"]:
            entity_name = [*entity_desc][0]
            entity = entity_desc[entity_name]
            if entity_name not in entity_dict:
                entity_dict[entity_name] = []
            for k, v in entity.items():
                for adict in v:
                    entity_dict[entity_name].append(adict["name"])
        return entity_dict
