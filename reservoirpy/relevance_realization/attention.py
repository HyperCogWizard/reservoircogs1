"""
Attention mechanisms and salience scoring for the Relevance Realization Framework.

Implements adaptive attention allocation and contextual salience computation.
"""

from typing import List, Optional
import numpy as np
from .hypergraph import Hyperedge


def salience_score(features: np.ndarray, context: np.ndarray) -> float:
    """
    Compute the salience score between features and context.
    
    Uses dot product to measure contextual relevance, representing
    how well features align with current context.
    
    Args:
        features: Feature vector from nodes/edges
        context: Current context vector
    
    Returns:
        Salience score (higher = more relevant)
    """
    # Ensure both arrays are float64 for numerical stability
    features = np.asarray(features, dtype=np.float64)
    context = np.asarray(context, dtype=np.float64)
    
    # Handle dimension mismatch by using minimum dimension
    min_dim = min(len(features), len(context))
    if min_dim == 0:
        return 0.0
    
    return float(np.dot(features[:min_dim], context[:min_dim]))


class AttentionMechanism:
    """
    Implements adaptive attention allocation over hypergraph structures.
    
    Provides context-sensitive filtering and recursive attention propagation
    for emergent pattern detection.
    """
    
    def __init__(self, threshold: float = 0.5):
        """
        Initialize attention mechanism.
        
        Args:
            threshold: Base threshold for attention filtering
        """
        self.threshold = threshold
        self.attention_history = []
    
    def update_attention(self, edges: List[Hyperedge], context: np.ndarray, 
                        threshold: Optional[float] = None) -> List[Hyperedge]:
        """
        Filter hyperedges based on attention/salience above threshold.
        
        Args:
            edges: List of hyperedges to filter
            context: Current context vector
            threshold: Attention threshold (uses default if None)
        
        Returns:
            List of salient hyperedges above threshold
        """
        if threshold is None:
            threshold = self.threshold
        
        salient_edges = []
        for edge in edges:
            combined_features = edge.get_combined_features()
            if len(combined_features) > 0:
                score = salience_score(combined_features, context)
                if score > threshold:
                    salient_edges.append(edge)
        
        return salient_edges
    
    def propagate_attention(self, edges: List[Hyperedge], context: np.ndarray, 
                          threshold: float, depth: int = 2) -> List[Hyperedge]:
        """
        Recursively propagate attention with increasing threshold.
        
        Implements recursive attention allocation that adapts to changing
        contexts, enabling emergent self-organizing relevance.
        
        Args:
            edges: Initial set of hyperedges
            context: Context vector for attention
            threshold: Starting threshold
            depth: Number of recursive iterations
        
        Returns:
            Final set of salient hyperedges after recursive propagation
        """
        if depth == 0 or not edges:
            return edges
        
        # Filter edges based on current threshold
        salient_edges = self.update_attention(edges, context, threshold)
        
        # Record attention state
        self.attention_history.append({
            'depth': depth,
            'threshold': threshold,
            'num_edges': len(salient_edges)
        })
        
        # Recursive call with increased threshold
        return self.propagate_attention(
            salient_edges, 
            context, 
            threshold + 0.05,  # Gradually increase selectivity
            depth - 1
        )
    
    def get_attention_state(self) -> dict:
        """
        Get current attention state for monitoring and debugging.
        
        Returns:
            Dictionary with attention mechanism state information
        """
        return {
            'threshold': self.threshold,
            'history_length': len(self.attention_history),
            'last_history': self.attention_history[-1] if self.attention_history else None
        }