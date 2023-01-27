"""Module providing wrapper for terraform."""
from .terraform import (
    IsFlagged,
    IsNotFlagged,
    Terraform,
    TerraformCommandError,
    VariableFiles,
)
from .tfstate import Tfstate
