import numpy as np


def sat_zen_angle(xlat, xlon, satlat=0, satlon=-75.0):

    """
    Calculate the satellite-zenith or satellite-viewing angle
    of given geographical coordinates given the position of a geostationary satellite.
    
    Args:
      xlat: Numpy array (or list) of latitude coordinates.
      xlon: Numpy array (or list) of longitude coordinates.
      satlat: Satellite latitude, default 0.
      satlon: Satellite longitude, default -75.0.

    Returns:
      Numpy array of satellite zenith angles.

    """

    DTOR = np.pi / 180.0

    if isinstance(xlat, list):
        xlat = np.array(xlat)
    if isinstance(xlon, list):
        xlon = np.array(xlon)

    lon = (xlon - satlon) * DTOR
    lat = (xlat - satlat) * DTOR

    beta = np.arccos(np.cos(lat) * np.cos(lon))
    sin_beta = np.sin(beta)

    zenith = np.arcsin(
        42164.0 * sin_beta / np.sqrt(1.808e09 - 5.3725e08 * np.cos(beta))
    )

    zenith = zenith / DTOR

    return zenith
