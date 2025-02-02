"""
Test for file IO
"""
import pytest
import numpy as np

brbd_to_test = []

import biorbd

brbd_to_test.append(biorbd)


@pytest.mark.parametrize("brbd", brbd_to_test)
@pytest.mark.parametrize("method", ["only_lm", "lm", "trf"])
def test_solve(brbd, method):
    biorbd_model = brbd.Model("../../models/pyomecaman.bioMod")

    qinit = np.array([0.1, 0.1, -0.3, 0.35, 1.15, -0.35, 1.15, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])

    markers = np.ndarray((3, biorbd_model.nbMarkers(), 1))
    markers[:, :, 0] = np.array([mark.to_array() for mark in biorbd_model.markers(qinit)]).T

    ik = biorbd.InverseKinematics(biorbd_model, markers)
    ik_q = ik.solve(method=method)

    if method == "only_lm":
        np.testing.assert_almost_equal(
            np.squeeze(ik_q.T),
            qinit,
        )
    elif method == "trf" or method == "lm":
        np.testing.assert_almost_equal(np.squeeze(np.round(ik_q, 1).T), qinit, decimal=1)
