"""
Hypergraph structures for the Relevance Realization Framework.

Implements nodes and hyperedges as the foundation for distributed cognition
and neural-symbolic integration.
"""

from typing import List, Any, Optional
import numpy as np


class Node:
    """
    Represents a node in the hypergraph structure.
    
    Each node encodes features like activation, novelty, and coherence,
    which are core to distributed cognition.
    """
    
    def __init__(self, id_: str, features: List[float]):
        """
        Initialize a hypergraph node.
        
        Args:
            id_: Unique identifier for the node
            features: Feature vector [activation, novelty, coherence, ...]
        """
        self.id = id_
        self.features = np.array(features, dtype=np.float64)
    
    def __repr__(self):
        return f"Node(id='{self.id}', features={self.features.tolist()})"
    
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.id == other.id and np.allclose(self.features, other.features)


class Hyperedge:
    """
    Represents a hyperedge in the hypergraph structure.
    
    Hyperedges bind nodes and enable high-order associative inferences
    with flexible, non-binary associations.
    """
    
    def __init__(self, id_: str, nodes: List[Node], weight: float):
        """
        Initialize a hyperedge.
        
        Args:
            id_: Unique identifier for the hyperedge
            nodes: List of nodes connected by this hyperedge
            weight: Strength/weight of the association
        """
        self.id = id_
        self.nodes = nodes
        self.weight = float(weight)
    
    def __repr__(self):
        node_ids = [node.id for node in self.nodes]
        return f"Hyperedge(id='{self.id}', nodes={node_ids}, weight={self.weight})"
    
    def __eq__(self, other):
        if not isinstance(other, Hyperedge):
            return False
        return (self.id == other.id and 
                self.nodes == other.nodes and 
                abs(self.weight - other.weight) < 1e-9)
    
    def get_combined_features(self) -> np.ndarray:
        """
        Get the combined features of all nodes in this hyperedge.
        
        Returns:
            Sum of feature vectors from all connected nodes
        """
        if not self.nodes:
            return np.array([])
        
        return np.sum([node.features for node in self.nodes], axis=0)