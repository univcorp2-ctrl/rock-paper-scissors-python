"""A simple command-line Rock Paper Scissors game."""

from __future__ import annotations

import random
from typing import Optional

CHOICES = ("rock", "paper", "scissors")

ALIASES = {
    "rock": "rock",
    "r": "rock",
    "gu": "rock",
    "goo": "rock",
    "グー": "rock",
    "ぐー": "rock",
    "paper": "paper",
    "p": "paper",
    "pa": "paper",
    "paa": "paper",
    "パー": "paper",
    "ぱー": "paper",
    "scissors": "scissors",
    "scissor": "scissors",
    "s": "scissors",
    "choki": "scissors",
    "チョキ": "scissors",
    "ちょき": "scissors",
}

QUIT_WORDS = {"q", "quit", "exit", "終了", "やめる"}


def normalize_choice(value: str) -> Optional[str]:
    """Normalize user input into one of rock, paper, or scissors."""
    return ALIASES.get(value.strip().lower())


def judge(player: str, computer: str) -> str:
    """Return the result from the player's point of view.

    Args:
        player: One of ``rock``, ``paper``, or ``scissors``.
        computer: One of ``rock``, ``paper``, or ``scissors``.

    Returns:
        ``draw``, ``win``, or ``lose``.

    Raises:
        ValueError: If either choice is invalid.
    """
    if player not in CHOICES:
        raise ValueError(f"Invalid player choice: {player}")
    if computer not in CHOICES:
        raise ValueError(f"Invalid computer choice: {computer}")

    if player == computer:
        return "draw"

    winning_pairs = {
        ("rock", "scissors"),
        ("scissors", "paper"),
        ("paper", "rock"),
    }
    return "win" if (player, computer) in winning_pairs else "lose"


def format_result(player: str, computer: str) -> str:
    """Create a user-friendly result message."""
    result = judge(player, computer)
    if result == "draw":
        return f"You chose {player}. Computer chose {computer}. It's a draw!"
    if result == "win":
        return f"You chose {player}. Computer chose {computer}. You win!"
    return f"You chose {player}. Computer chose {computer}. You lose!"


def get_computer_choice() -> str:
    """Return a random computer choice."""
    return random.choice(CHOICES)


def main() -> None:
    """Run the interactive command-line game."""
    print("Rock Paper Scissors / ジャンケン")
    print("Type rock, paper, scissors or グー, パー, チョキ. Type q to quit.")

    while True:
        raw_choice = input("Your choice: ").strip()
        if raw_choice.lower() in QUIT_WORDS:
            print("Thanks for playing!")
            break

        player_choice = normalize_choice(raw_choice)
        if player_choice is None:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(format_result(player_choice, computer_choice))


if __name__ == "__main__":
    main()
