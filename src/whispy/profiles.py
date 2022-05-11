"""Functions to extract 1-d profiles from astronomical images

Author: Will Henney, IRyA-UNAM, 2022
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Union

import numpy as np
from astropy.coordinates import Angle
from astropy.coordinates import SkyCoord
from astropy.io import fits  # type: ignore
from astropy.wcs import WCS
from mpdaf.obj import Image

HDU = Union[fits.PrimaryHDU, fits.CompImageHDU, fits.ImageHDU]


def get_skycoords_array(hdu: HDU) -> SkyCoord:
    """Get the sky cordinates array for a FITS image HDU

    Returns an astropy.coordinates.SkyCoord array that matches the
    hdu.data array"""
    ny, nx = hdu.data.shape
    xpix, ypix = np.meshgrid(np.arange(nx), np.arange(ny))
    coords = WCS(hdu.header).pixel_to_world(xpix, ypix)
    return coords


@dataclass
class RadialProfile:
    image: Image
    origin: SkyCoord
    pa_axis: Angle
