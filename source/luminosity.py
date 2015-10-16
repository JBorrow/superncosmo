"""##########################################################################
#                                                                           # 
#   Author: Josh Borrow                                                     #
#   Affiliation: Durham University                                          #
#   Creation Date: 2015-10-16                                               #
#   Project: SuperNCosmo, 3rd Year                                          #
#   File Description: Script for calculating effective luminosity of t1asne #
#                     for the superncosmo project                           #
#                                                                           #
##########################################################################"""

import numpy as np
import gfunc as gf
from scipy.optimize import curve_fit


def mag_peak_fit(z, lpeak):
    """Wrapper for get_mag_peak that's compatible with curve_fit"""
    return gf.get_mag_lpeak(lpeak, z)


def find_lpeak():
    """Finds peak luminosity using the data and functions specified in gfunc."""
    z, mag, mag_err = gf.get_data()
    print z, mag, mag_err

    popt, pcov = curve_fit(mag_peak_fit, z, mag, sigma=mag_err,
                                 absolute_sigma=True)

    return popt, pcov

if __name__=="__main__":
    print find_lpeak()
