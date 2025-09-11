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



class HeteroR2GMapper:
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
    
    def get_entities(self) -> dict[str, object]:
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

    def get_relations(self) -> dict[str, object]:
        """
        Returns the relations dictionary.

        Returns:
            dict[str, object]: The relations loaded from the config file. The dictionary contains a details object for each relation in the config file.
        """
        rel_dict = {}
        for rel_name, rel_det in self._r2g_cfg["relations"].items():
            if rel_name not in rel_dict:
                rel_dict[rel_name] = {}
            for k, v in rel_det.items():
                for adict in v:
                    rel_dict[rel_name][k] = v
        return rel_dict
    
    def write_mapping(self, file_path:str, ent_rel_mapping:Dict[str, Any]) -> None :
        """
        Writes the given entity-relationship mapping to a YAML file.
        Args:
            file_path (str): The path to the file where the mapping will be written.
            ent_rel_mapping (Dict[str, Any]): The entity-relationship mapping to serialize and write.
        Returns:
            None
        """

        with open(file_path, 'w') as file:
            yaml.dump(ent_rel_mapping, file)

