__author__ = 'FeNikS'

import noc.sa.profiles
from noc.sa.protocols.sae_pb2 import HTTP


class Profile(noc.sa.profiles.Profile):
    name = "Harmonic.DiviComElectra"
    supported_schemes = [HTTP]
