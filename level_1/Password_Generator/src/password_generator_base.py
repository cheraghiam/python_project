from abc import ABC, abstractmethod


class PasswordGenerator(ABC):
    """Abstract base class for password generators.

    Args:
        ABC (type): Abstract base class.
    """
    @abstractmethod
    def generate(self) -> None:
        """Generate a password.
        """
        pass