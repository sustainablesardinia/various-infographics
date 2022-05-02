# helpers.py

"""A collection of helpers for the infographics"""

# Copyright 2022 Sustainable Sardinia

import matplotlib


def html_to_rgb(html_string):
    """Convert an HTML string to a list of doubles for matplotlib"""
    return [int(html_string[i : i + 2], 16) / 255.0 for i in (0, 2, 4)]


def set_style():
    """Set the default style for the infographic"""
    style_options = {
        "edge_color": "#666A6D",
        "foreground_color": "white",
        "background_color": "black",
        "missing_color": "#A9A9A9",
        "description_text_color": "#BFBFBF",
        "title_size": 26,
        "axis_label_size": 18,
        "tick_label_size": 15,
        "description_text_size": 14,
        "small_text_size": 10,
        "max_description_text_characters": 100,
    }
    matplotlib.rcParams["font.family"] = "sans-serif"
    matplotlib.rcParams["font.sans-serif"] = "Source Sans Pro"
    matplotlib.rcParams["text.color"] = style_options["foreground_color"]
    matplotlib.rcParams["axes.edgecolor"] = style_options["foreground_color"]
    return style_options


def break_text(text, num_characters):
    """Break the given text to multiple lines with a certain number of characters"""
    words = text.split(" ")
    output_string = ""
    length_current_line = 0
    for index, curr_word in enumerate(words):
        length_curr_word = len(curr_word)

        if index == 0:
            length_current_line = length_curr_word
            curr_separator = ""
        elif length_current_line + 1 + length_curr_word <= num_characters:
            length_current_line += 1 + length_curr_word
            curr_separator = " "
        else:
            length_current_line = length_curr_word
            curr_separator = "\n"
        output_string += curr_separator + curr_word
    return output_string
