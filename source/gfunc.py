"""##########################################################################
#                                                                           # 
#   Author: Josh Borrow                                                     #
#   Affiliation: Durham University                                          #
#   Creation Date: 2015-10-16                                               #
#   Project: SuperNCosmo, 3rd Year                                          #
#   File Description: Contains global variables (e.g. H0) and functions     #
#                     (e.g. conversion from magnitude to flux) for the      #
#                     superNcosmo project as part of third year physics.    #
#                                                                           #
##########################################################################"""

import numpy as np
import scipy.integrate as si


################## Set global variables here ################################


H0 = 75. * (1/3.086E19)  # in km/s/mpc convert to s^-1
c = 299792458.  # in m/s
pi = np.pi
m0_init=-15
low_z_data = "../data/low_z_data.csv"


################# Set global functions here ################################


def get_mag_from_flux(flux, m0=m0_init):
    """m0 in units of...""" # FIX ME
    return m0 - 2.5*np.log10(flux)


def GR_factor_R0(z, c=c, H0=H0):
    """Gets the factor R_0 * S(eta) from general relativity (see 10.14 in pdf
    booklet). For low redshifts, this is approximately cz/H0."""
    return c*z/H0


def get_flux_lpeak(lpeak, z, pi=pi, c=c, H0=H0, R0SN=GR_factor_R0):
    """Gets the peak flux of a t1a sne with luminosity Lpeak (10.14)"""
    return (lpeak)/(4*pi*(R0SN(z,c,H0)**2)*((1+z)**2))


def get_mag_lpeak(lpeak, z, m0=m0_init, pi=pi, c=c, H0=H0, R0SN=GR_factor_R0):
    """Wrapper for get_mag_from_flux and get_flux_lpeak to return magnitude
    instead of flux"""
    return get_mag_from_flux(get_flux_lpeak(lpeak, z, pi, c, H0,
                             GR_factor_R0), m0)


def get_data(fname=low_z_data):
    """Use data in columns of name, redshift, mag, mag_error with comma
    as the delimiter"""
    raw = np.loadtxt(fname, delimiter=" ", usecols=(1,2,3))
    return raw[:,0], raw[:,1], raw[:,2]


def get_h_flat(z, omega_lambda, H0=H0):
    """Gets H in a flat universe as a function of z only"""
    return H0*np.sqrt((1-omega_lambda)*(1+z)**3 + omega_lambda)


def GR_factor_integral(z, omega_lambda, c=c, H0=H0, get_h_flat=get_h_flat):
    """Gets the factor R0 eta based on the model in get_h_flat by integration"""
    initial_result = c*si.quad(get_h_flat, a=0, b=z, args=(omega_lambda, H0))
    return initial_result[0]
