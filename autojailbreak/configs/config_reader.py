import yaml

BASE_CONFIG_FIELDNAME = "GeneralFields"
SUBSTITUTION_CONFIG_FIELDNAME = "Substitutions"


class ConfigReader:
    def __init__(self, config_path):
        self.config_path = config_path

    def read_config(self):
        loaded_config = yaml.safe_load(open(self.config_path))
        if BASE_CONFIG_FIELDNAME not in loaded_config.keys():
            return [self.__process_simple_config(loaded_config)]
        else:
            list_of_configs = self.__process_config_with_placeholders(loaded_config)
            return list_of_configs

    def __process_simple_config(self, loaded_config):
        return loaded_config

    def __process_config_with_placeholders(self, loaded_config):
        base_config = loaded_config[BASE_CONFIG_FIELDNAME]
        substitutions_config = loaded_config[SUBSTITUTION_CONFIG_FIELDNAME]

        if len(substitutions_config) == 0:
            raise ValueError("Substitutions config is empty. Please provide at least one substitution.")
        num_experiments = len(list(substitutions_config.values())[0])

        list_of_configs = []
        for substitution_name, substitution_values in substitutions_config.items():
            if len(substitution_values) != num_experiments:
                raise ValueError(f"All substitution lists must have the same length. Substitution {substitution_name} has length {len(substitution_values)}, expected {num_experiments}.")
        
        for i in range(num_experiments):
            config_copy = base_config.copy()
            for substitution_name, substitution_values in substitutions_config.items():
                config_copy[substitution_name] = substitution_values[i]
            list_of_configs.append(config_copy)

        return list_of_configs
        