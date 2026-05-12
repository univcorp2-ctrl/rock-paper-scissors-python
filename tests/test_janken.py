import pytest

from janken import CHOICES, format_result, judge, normalize_choice


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("rock", "rock"),
        ("R", "rock"),
        ("グー", "rock"),
        ("paper", "paper"),
        ("P", "paper"),
        ("パー", "paper"),
        ("scissors", "scissors"),
        ("S", "scissors"),
        ("チョキ", "scissors"),
    ],
)
def test_normalize_choice_accepts_supported_inputs(raw, expected):
    assert normalize_choice(raw) == expected


def test_normalize_choice_rejects_invalid_input():
    assert normalize_choice("banana") is None


@pytest.mark.parametrize("choice", CHOICES)
def test_judge_draw(choice):
    assert judge(choice, choice) == "draw"


@pytest.mark.parametrize(
    ("player", "computer"),
    [
        ("rock", "scissors"),
        ("scissors", "paper"),
        ("paper", "rock"),
    ],
)
def test_judge_win(player, computer):
    assert judge(player, computer) == "win"


@pytest.mark.parametrize(
    ("player", "computer"),
    [
        ("rock", "paper"),
        ("paper", "scissors"),
        ("scissors", "rock"),
    ],
)
def test_judge_lose(player, computer):
    assert judge(player, computer) == "lose"


@pytest.mark.parametrize(
    ("player", "computer"),
    [
        ("lizard", "rock"),
        ("rock", "spock"),
    ],
)
def test_judge_raises_value_error_for_invalid_choices(player, computer):
    with pytest.raises(ValueError):
        judge(player, computer)


def test_format_result_contains_choices_and_outcome():
    message = format_result("rock", "scissors")
    assert "rock" in message
    assert "scissors" in message
    assert "You win!" in message
