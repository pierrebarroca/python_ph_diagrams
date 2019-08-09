# -*- coding: utf-8 -*-

"""Main module."""

import CoolProp.CoolProp as CP
import numpy as np
class PlotProps:

    def __init__(self, CP_BACKEND, FLUID):
        self.abst = CP.AbstractState(CP_BACKEND, FLUID)
        self.__get_PropLimits()

    def __get_PropLimits(self):
        self.Tmin = self.abst.keyed_output(CP.iT_triple)
        self.Tcritical = self.abst.keyed_output(CP.iT_critical)
        self.abst.update(CP.QT_INPUTS, 0, self.Tmin)
        self.Hmin = self.abst.keyed_output(CP.iHmass)
        self.Pmin = self.abst.keyed_output(CP.iP)
        self.abst.update(CP.QT_INPUTS, 0, self.Tcritical)
        self.Hcritical = self.abst.keyed_output(CP.iHmass)
        self.Pcritical = self.abst.keyed_output(CP.iP)
        self.abst.update(CP.QT_INPUTS, 1, self.Tmin)
        self.Hmax = self.abst.keyed_output(CP.iHmass)

    def get_SubCooledSatLine(self, N=10):
        H = np.array([])
        P = np.linspace(self.Pmin, self.Pcritical-1, N)
        for iP in P:
            self.abst.update(CP.PQ_INPUTS, iP, 0)
            H = np.append(H, self.abst.keyed_output(CP.iHmass))
        return H, P

    def get_SuperHeatedSatLine(self, N=10):
        H = np.array([])
        P = np.linspace(self.Pcritical-1, self.Pmin, N)
        for iP in P:
            self.abst.update(CP.PQ_INPUTS, iP, 1)
            H = np.append(H, self.abst.keyed_output(CP.iHmass))
        return H, P

    def get_SatLine(self, N=10):
        H0, P0 = self.get_SubCooledSatLine(N=N)
        H1, P1 = self.get_SuperHeatedSatLine(N=N)
        H = np.append(H0, H1)
        P = np.append(P0, P1)
        return H, P

    def get_SatQLine(self, Q, N=10):
        H = np.array([])
        P = np.linspace(self.Pmin, self.Pcritical-1, N)
        for iP in P:
            self.abst.update(CP.PQ_INPUTS, iP, Q)
            H = np.append(H, self.abst.keyed_output(CP.iHmass))
        return H, P

    def get_SatTLine(self, T, N=10):
        self.abst.update(CP.QT_INPUTS, 0, T)
        H0 = self.abst.keyed_output(CP.iHmass)
        P0 = self.abst.keyed_output(CP.iP)
        self.abst.update(CP.QT_INPUTS, 1, T)
        H1 = self.abst.keyed_output(CP.iHmass)
        P1 = self.abst.keyed_output(CP.iP)
        H = np.linspace(H0, H1, N)
        P = np.linspace(P0, P1, N)
        return H, P

    def get_SuperHeatedTLine(self, T, Hmax, N=10):
        self.abst.update(CP.QT_INPUTS, 0, T)
        H0 = self.abst.keyed_output(CP.iHmass)
        P0 = self.abst.keyed_output(CP.iP)
        self.abst.update(CP.QT_INPUTS, 1, T)
        H1 = self.abst.keyed_output(CP.iHmass)
        P1 = self.abst.keyed_output(CP.iP)
        H = np.linspace(H0, H1, N)
        P = np.linspace(P0, P1, N)
        return H, P
