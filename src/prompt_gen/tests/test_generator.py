from prompt_gen import PromptGenerator
import pytest


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


def test_loading_class_with_args(get_prompt_model_with_args):
    assert isinstance(
        get_prompt_model_with_args.generate_random_prompts(), list)
    assert isinstance(
        get_prompt_model_with_args.generate_random_prompts()[0], str)


@pytest.mark.parametrize('args', [
    {'styles': ['style1', 'style2']},
    {'perspectives': ['perspective1', 'perspective2']},
    {'vibes': ['vibe1', 'vibe2']},
    {'boosters': ['booster1', 'booster2']},
    None
])
def test_single_prompt(get_prompt_model, args):
    assert isinstance(get_prompt_model.generate_single_prompt(args), str)


def test_multiple_prompts_with_no_args(get_prompt_model):
    assert isinstance(get_prompt_model.generate_random_prompts(), list)
    assert isinstance(get_prompt_model.generate_random_prompts()[0], str)


def test_multiple_prompts_with_args(get_prompt_model):
    assert isinstance(get_prompt_model.generate_random_prompts(
        styles=['style1', 'style2'],
        perspectives=['perspective1', 'perspective2'],
        vibes=['vibe1', 'vibe2'],
        boosters=['booster1', 'booster2'],
        formats=['format1', 'format2'],
        characters=['character1', 'character2'],
        scenarios=['scenario1', 'scenario2'],
        locations=['location1', 'location2']), list)
    assert isinstance(get_prompt_model.generate_random_prompts(
        styles=['style1', 'style2'],
        perspectives=['perspective1', 'perspective2'],
        vibes=['vibe1', 'vibe2'],
        boosters=['booster1', 'booster2'],
        formats=['format1', 'format2'],
        characters=['character1', 'character2'],
        scenarios=['scenario1', 'scenario2'],
        locations=['location1', 'location2'])[0], str)
