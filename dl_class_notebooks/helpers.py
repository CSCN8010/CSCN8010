import sys
import torch

def print_pytorch_version() -> None:
    """
    Prints the pyTorch version.
    Parameters
    ----------
    None
    Returns
    -------
    None
    """
    print(f'pyTorch version: {torch.__version__}')

def print_python_version() -> None:
    """
    Prints the Python version.
    Parameters
    ----------
    None
    Returns
    -------
    None
    """
    print(f'Python version: {sys.version}')

def print_tensor_info(tensor: torch.Tensor, fields: list[str]=None) -> None:
    """
    Prints information about a tensor.
    Parameters
    ----------
    tensor : torch.Tensor
        The tensor to print information about.
    fields : list[str], optional
        A list of fields to print. If None, all supported fields are printed.
        Valid fields are: 'Tensor', 'Type', 'dtype', 'Dimension', 'Shape'
    Returns
    -------
    None
    """
    # A dictionary of the supported fields by this function, and their corresponding generating function.
    supported_fields = {
        'Tensor':    tensor,
        'Type':      type(tensor), 
        'dtype':     tensor.dtype, 
        'Dimension': tensor.dim(), 
        'Shape':     tuple(tensor.shape)
        }
    # type check the input
    if type(tensor) is not torch.Tensor:
        raise TypeError(f"The input must be a <class 'torch.Tensor'>. Instead it is a {type(tensor)}")
    if fields is not None:
        for field in fields:
            if field not in supported_fields.keys():
                raise ValueError(f"Field {field} is not a valid field. Valid fields are: {supported_fields.keys()}")
    # set fields to all fields if None
    if fields is None:
        fields = list(supported_fields.keys())
    # print the fields
    for field in fields:
        if field == 'Tensor':
            print(f'{supported_fields[field]}')
        else:
            print(f'{field:<12} {supported_fields[field]}')  # all other fields are printed on a single line, and '<12' keeps the alignment
    return
