"""
Pattern selection algorithms for emergent pattern realization.

Implements emergent pattern selection that mirrors cognitive insight
and relevance realization processes.
"""

from typing import List, Optional, Any
from .hypergraph import Hyperedge


def emergent_pattern(edges: List[Hyperedge]) -> Optional[Hyperedge]:
    """
    Select the most emergent pattern from a set of hyperedges.
    
    Chooses the hyperedge with highest weight, representing the most
    salient pattern that has emerged from the recursive attention process.
    
    Args:
        edges: List of hyperedges to select from
    
    Returns:
        Hyperedge with highest weight, or None if no edges
    """
    if not edges:
        return None
    
    return max(edges, key=lambda edge: edge.weight)


def select_pattern(edges: List[Hyperedge], selection_strategy: str = 'max_weight') -> Optional[Hyperedge]:
    """
    Select pattern using specified strategy.
    
    Provides multiple strategies for pattern selection to enable
    different types of emergent behavior.
    
    Args:
        edges: List of hyperedges to select from
        selection_strategy: Strategy to use ('max_weight', 'max_nodes', 'min_weight')
    
    Returns:
        Selected hyperedge based on strategy, or None if no edges
    """
    if not edges:
        return None
    
    if selection_strategy == 'max_weight':
        return max(edges, key=lambda edge: edge.weight)
    elif selection_strategy == 'min_weight':
        return min(edges, key=lambda edge: edge.weight)
    elif selection_strategy == 'max_nodes':
        return max(edges, key=lambda edge: len(edge.nodes))
    elif selection_strategy == 'random':
        import random
        return random.choice(edges)
    else:
        # Default to max_weight
        return max(edges, key=lambda edge: edge.weight)


def rank_patterns(edges: List[Hyperedge], context: Optional[Any] = None) -> List[Hyperedge]:
    """
    Rank all patterns by emergent potential.
    
    Returns patterns sorted by their potential for emergence,
    enabling selection of multiple relevant patterns.
    
    Args:
        edges: List of hyperedges to rank
        context: Optional context for ranking (not used in basic implementation)
    
    Returns:
        List of hyperedges sorted by descending weight
    """
    return sorted(edges, key=lambda edge: edge.weight, reverse=True)


def pattern_coherence(edge: Hyperedge) -> float:
    """
    Compute coherence measure for a pattern.
    
    Measures how coherent the features are within a pattern,
    based on the variance of combined features.
    
    Args:
        edge: Hyperedge representing the pattern
    
    Returns:
        Coherence score (lower variance = higher coherence)
    """
    combined_features = edge.get_combined_features()
    if len(combined_features) == 0:
        return 0.0
    
    # Use negative variance as coherence (higher coherence = lower variance)
    return -float(combined_features.var())


def pattern_diversity(edges: List[Hyperedge]) -> float:
    """
    Compute diversity measure across multiple patterns.
    
    Measures how diverse the set of patterns is, encouraging
    exploration of different emergent possibilities.
    
    Args:
        edges: List of hyperedges representing patterns
    
    Returns:
        Diversity score (higher = more diverse patterns)
    """
    if len(edges) < 2:
        return 0.0
    
    # Simple diversity based on weight variance
    weights = [edge.weight for edge in edges]
    return float(sum(weights)) / len(weights) if weights else 0.0