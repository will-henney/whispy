"""Functions to manipulate masks of MUSE cubes and images

Author: Will Henney, IRyA-UNAM, 2021
"""
from mpdaf.obj import Image


def trim_edges(im: Image, m: int) -> None:
    """Trim in-place m pixels of each edge of image by setting mask"""
    im.mask[:m, :] = True
    im.mask[-m:, :] = True
    im.mask[:, :m] = True
    im.mask[:, -m:] = True
    return None
