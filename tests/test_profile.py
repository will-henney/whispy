import astropy.units as u
import numpy as np
import pytest
from astropy.coordinates import SkyCoord
from astropy.io import fits
from astropy.wcs import WCS

from whispy import profiles


@pytest.fixture()
def hdu():
    """A simple example HDU"""
    nx, ny = 5, 5
    w = WCS(naxis=2)
    w.wcs.crpix = [1.0, 1.0]
    w.wcs.crval = [90.0, 45.0]
    w.wcs.cdelt = np.array([-1.0, 1.0]) / 3600
    w.wcs.ctype = ["RA---TAN", "DEC--TAN"]

    yield fits.PrimaryHDU(header=w.to_header(), data=np.ones((ny, nx)))


def test_skycoords_separation(hdu):
    """Check that separation of diagonal opposite corners is correct"""
    # Size of image in arcsec
    width = (hdu.header["NAXIS1"] - 1) * hdu.header["CDELT1"] * 3600
    height = (hdu.header["NAXIS2"] - 1) * hdu.header["CDELT2"] * 3600
    # Calculate by hand the separation between diagonal opposite corner pixels
    expected_separation = np.hypot(width, height) * u.arcsec
    c = profiles.get_skycoords_array(hdu)
    assert np.isclose(
        c[0, 0].separation(c[-1, -1]),
        expected_separation,
    )
