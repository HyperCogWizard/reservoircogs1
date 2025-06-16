"""
Relevance Realization Framework for ReservoirCogs

This module implements a recursive cognitive engine with hypergraph encoding,
adaptive attention allocation, and emergent pattern selection.
"""

from .hypergraph import Node, Hyperedge
from .attention import AttentionMechanism, salience_score
from .recursive_engine import RelevanceRealizationEngine
from .pattern_selection import emergent_pattern, select_pattern
from .triadic_integration import TriadicProcessor

__all__ = [
    'Node',
    'Hyperedge', 
    'AttentionMechanism',
    'salience_score',
    'RelevanceRealizationEngine',
    'emergent_pattern',
    'select_pattern',
    'TriadicProcessor'
]