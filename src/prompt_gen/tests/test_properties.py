import pytest
from prompt_gen import PromptGenerator


@pytest.fixture
def get_prompt_model():
    return PromptGenerator()


@pytest.fixture
def get_prompt_model_with_args():
    return PromptGenerator(
        styles=['style1', 'style2'],
        perspectives=['perspective1', 'perspective2'],
        vibes=['vibe1', 'vibe2'],
        boosters=['booster1', 'booster2'],
        formats=['format1', 'format2'],
        characters=['character1', 'character2'],
        scenarios=['scenario1', 'scenario2'],
        locations=['location1', 'location2'])


def test_class_init_with_args(get_prompt_model):
    assert isinstance(get_prompt_model, PromptGenerator)
    assert isinstance(get_prompt_model.styles, list)
    assert isinstance(get_prompt_model.perspectives, list)
    assert isinstance(get_prompt_model.vibes, list)
    assert isinstance(get_prompt_model.boosters, list)
    assert isinstance(get_prompt_model.formats, list)
    assert isinstance(get_prompt_model.characters, list)
    assert isinstance(get_prompt_model.scenarios, list)
    assert isinstance(get_prompt_model.locations, list)
    assert len(get_prompt_model.styles) > 0
    assert len(get_prompt_model.perspectives) > 0
    assert len(get_prompt_model.vibes) > 0
    assert len(get_prompt_model.boosters) > 0
    assert len(get_prompt_model.formats) > 0
    assert len(get_prompt_model.characters) > 0
    assert len(get_prompt_model.scenarios) > 0
    assert len(get_prompt_model.locations) > 0


def test_class_init_with_args(get_prompt_model_with_args):
    assert isinstance(get_prompt_model_with_args, PromptGenerator)
    assert isinstance(get_prompt_model_with_args.styles, list)
    assert isinstance(get_prompt_model_with_args.perspectives, list)
    assert isinstance(get_prompt_model_with_args.vibes, list)
    assert isinstance(get_prompt_model_with_args.boosters, list)
    assert isinstance(get_prompt_model_with_args.formats, list)
    assert isinstance(get_prompt_model_with_args.characters, list)
    assert isinstance(get_prompt_model_with_args.scenarios, list)
    assert isinstance(get_prompt_model_with_args.locations, list)
    assert len(get_prompt_model_with_args.styles) > 0
    assert len(get_prompt_model_with_args.perspectives) > 0
    assert len(get_prompt_model_with_args.vibes) > 0
    assert len(get_prompt_model_with_args.boosters) > 0
    assert len(get_prompt_model_with_args.formats) > 0
    assert len(get_prompt_model_with_args.characters) > 0
    assert len(get_prompt_model_with_args.scenarios) > 0
    assert len(get_prompt_model_with_args.locations) > 0
