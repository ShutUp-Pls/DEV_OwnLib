class FormatTools:

    @staticmethod
    def safe_cast_value(value):
        try: return float(value) if value not in (None, "") else None
        except ValueError: return str(value)

    @staticmethod
    def number_to_str(number_raw):
        try: number_float = float(number_raw)
        except ValueError: return None

        if number_float.is_integer():
            number_int = int(number_float)
            return f"{number_int:,}".replace(",", ".")
        
        else: return f"{number_float:,.0f}".replace(",", ".")

    @staticmethod
    def str_to_number(str_value):
        if isinstance(str_value, str):
            try: return int(str_value)
            except:
                try: return float(str_value)
                except: return str_value

        else: return str_value