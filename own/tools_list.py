class ListTools:

    @staticmethod
    def difference(source_list:list, filter_list:list):
        filter_set = set(filter_list)
        return [item for item in source_list if not(item in filter_set)]

    @staticmethod
    def common(source_list:list, filter_list:list):
        filter_set = set(filter_list)
        return [item for item in source_list if item in filter_set]

    @staticmethod
    def toggle_item(item, toggle_list:list):
        if item in toggle_list: toggle_list.remove(item)
        else: toggle_list.append(item)
        return toggle_list

    @staticmethod
    def next_in(value, lst):
        if value in lst: return lst[(lst.index(value) + 1) % len(lst)]
        else: raise ValueError(f"El valor '{value}' no se encuentra en la lista proporcionada.")

    @staticmethod
    def get_next_available_int_value(self, column:str, rows:list, columns:list[str]):
        column_idx = columns.index(column)

        values = {row[column_idx] for row in rows if isinstance(row[column_idx], (int, float))}

        if values: next_value = min(set(range(1, max(values) + 2)) - values)
        else: next_value = 1

        return next_value