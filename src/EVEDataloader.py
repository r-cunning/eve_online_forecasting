import pandas as pd
import numpy as np
import torch
from torch_geometric_temporal.signal import StaticGraphTemporalSignal
import json 

class EVEDataloader(object):
    """A dataset of commodity prices on several EVE Online's main regional market hubs. Each vertex represents a market hub (trading exchange). 
    The edges between them represent transport routes. Underlying graph is static. Vertex features are the lagged daily prices of the commodities.
    Adapted from the Pytorch Geometric Temporal library.
    """

    # def __init__(self):
    def __init__(self, file):

        self._read_json(file)

    def _read_json(self, file):
        # Open and read the JSON file
        with open(file, 'r') as file:
            self._dataset = json.load(file)

    def _get_edges(self):
        self._edges = np.array(self._dataset["edges"]).T

    def _get_edge_weights(self):
        self._edge_weights = np.ones(self._edges.shape[1])

    def _get_targets_and_features(self):
        stacked_target = np.array(self._dataset["FX"])
        self.features = [
            stacked_target[i : i + self.lags, :].T
            for i in range(stacked_target.shape[0] - self.lags)
        ]
        self.targets = [
            stacked_target[i + self.lags, :].T
            for i in range(stacked_target.shape[0] - self.lags)
        ]

    def get_dataset(self, lags: int = 4) -> StaticGraphTemporalSignal:
        """Returning the EVE Dataset data iterator.

        Args types:
            * **lags** *(int)* - The number of time lags (days).
        Return types:
            * **dataset** *(StaticGraphTemporalSignal)* - The EVE Online graph dataset.
        """
        self.lags = lags
        self._get_edges()
        self._get_edge_weights()
        self._get_targets_and_features()
        dataset = StaticGraphTemporalSignal(
            self._edges, self._edge_weights, self.features, self.targets
        )
        return dataset
