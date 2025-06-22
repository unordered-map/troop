# Desc: Standard Interface for all the models.

from .hf_model import hugging_face
from .openai_model import open_ai


def call_appropriate_func(model):
    if model == "hugging-face":
        hugging_face()
    else:
        open_ai()
