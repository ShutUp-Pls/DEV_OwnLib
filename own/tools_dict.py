from . import zip_longest

class DictTools:

    @staticmethod
    def merge_dicts_absent(target_dict, source_dict):
        for key, value in source_dict.items():
            if key not in target_dict: target_dict[key] = value
        return target_dict

    @staticmethod
    def safe_dict_assign(target_dict, key, value, default=None):
        target_dict[key] = value if value else default

    @staticmethod
    def build_dict(keys, values, fill_keys=False, fill_values=False, default_key="default_key", default_value=None):
        max_length = max(len(keys), len(values))
        
        if fill_keys: keys = (keys + [f"{default_key}_{i}" for i in range(len(keys), max_length)]) if len(keys) < max_length else keys
        if fill_values: values = (values + [default_value] * (max_length - len(values))) if len(values) < max_length else values

        return dict(zip_longest(keys, values, fillvalue=default_value))

    @staticmethod
    def common_filter_list(source_dict: dict, filter_list: list):
        filter_set = set(filter_list)
        return {key: value for key, value in source_dict.items() if key in filter_set}