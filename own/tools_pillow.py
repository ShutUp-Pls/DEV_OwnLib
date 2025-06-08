from . import ImageDraw, ImageFont

class PillowTools:

    @staticmethod
    def put_text_by_char(draw:ImageDraw, text:str, text_font:ImageFont, text_color:str, text_space:int, pos_x:int, pos_y:int, direction:str='rtl', point_space:bool=True, point_steps:int=3):
        if direction == 'rtl':
            chars = reversed(text)
            step_sign = -1
        else:
            chars = text
            step_sign = 1

        for i, char in enumerate(chars):
            bbox_char = draw.textbbox((0, 0), char, font=text_font)
            char_ancho = bbox_char[2] - bbox_char[0]
            draw.text((pos_x, pos_y), char, fill=text_color, font=text_font)

            if point_space and ((i + 1) % point_steps) == 0: pos_x += step_sign * (char_ancho - 2 * text_space)
            else: pos_x += step_sign * (char_ancho - text_space)