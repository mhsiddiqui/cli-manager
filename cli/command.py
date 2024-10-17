from typing import List, Any

class BaseCommand:
    """Base class for defining custom commands."""

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def get_arguments(self) -> List[dict]:
        """Override to define arguments."""
        return []

    def run(self, *args, **kwargs) -> Any:
        """Override to implement the logic."""
        raise NotImplementedError("Subclasses must implement the run() method.")
