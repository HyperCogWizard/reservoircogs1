"""
Recursive Relevance Realization Engine - Core cognitive processing system.

Implements the main recursive cognitive engine that orchestrates hypergraph 
encoding, adaptive attention allocation, and emergent pattern selection.
"""

from typing import List, Optional, Dict, Any
import numpy as np
from .hypergraph import Node, Hyperedge
from .attention import AttentionMechanism, salience_score
from .pattern_selection import emergent_pattern, select_pattern, rank_patterns


class RelevanceRealizationEngine:
    """
    Main engine for recursive relevance realization processing.
    
    Embodies the cognitive flowchart: Input → Feature Extraction → 
    Hypergraph Construction → Salience Mapping → Recursive Attention → 
    Emergent Pattern Selection → Adaptive Output.
    """
    
    def __init__(self, attention_threshold: float = 0.7, recursion_depth: int = 2):
        """
        Initialize the relevance realization engine.
        
        Args:
            attention_threshold: Base threshold for attention filtering
            recursion_depth: Number of recursive attention iterations
        """
        self.attention_mechanism = AttentionMechanism(attention_threshold)
        self.recursion_depth = recursion_depth
        self.processing_history = []
    
    def extract_features(self, input_signal: Any) -> List[float]:
        """
        Extract features from raw input signal.
        
        Converts input into feature vectors suitable for hypergraph encoding.
        Basic implementation - can be extended for specific modalities.
        
        Args:
            input_signal: Raw input data
        
        Returns:
            Feature vector as list of floats
        """
        # Simple feature extraction - normalize numeric inputs
        if isinstance(input_signal, (int, float)):
            return [float(input_signal), 0.5, 0.5]  # [value, novelty, coherence]
        elif isinstance(input_signal, (list, tuple, np.ndarray)):
            arr = np.array(input_signal, dtype=np.float64)
            # Extract basic statistical features
            if len(arr) > 0:
                return [float(arr.mean()), float(arr.std()), float(len(arr))]
            else:
                return [0.0, 0.0, 0.0]
        else:
            # Default features for unknown types
            return [0.5, 0.5, 0.5]
    
    def construct_hypergraph(self, features_list: List[List[float]]) -> tuple[List[Node], List[Hyperedge]]:
        """
        Construct hypergraph from extracted features.
        
        Creates nodes and hyperedges representing the cognitive space
        for relevance realization processing.
        
        Args:
            features_list: List of feature vectors
        
        Returns:
            Tuple of (nodes, hyperedges)
        """
        # Create nodes from features
        nodes = []
        for i, features in enumerate(features_list):
            node = Node(f'N{i}', features)
            nodes.append(node)
        
        # Create hyperedges connecting nodes
        hyperedges = []
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                # Weight based on feature similarity
                weight = self._compute_edge_weight(nodes[i], nodes[j])
                edge = Hyperedge(f'E{i}_{j}', [nodes[i], nodes[j]], weight)
                hyperedges.append(edge)
        
        # Add higher-order hyperedges for groups of 3+ nodes
        if len(nodes) >= 3:
            for i in range(len(nodes) - 2):
                # Create 3-node hyperedge
                group_nodes = nodes[i:i+3]
                weight = np.mean([node.features.mean() for node in group_nodes])
                edge = Hyperedge(f'E3_{i}', group_nodes, weight)
                hyperedges.append(edge)
        
        return nodes, hyperedges
    
    def _compute_edge_weight(self, node1: Node, node2: Node) -> float:
        """Compute weight between two nodes based on feature similarity."""
        # Use negative distance as weight (closer nodes have higher weight)
        distance = np.linalg.norm(node1.features - node2.features)
        return max(0.1, 1.0 - distance / 10.0)  # Normalize and ensure positive
    
    def process(self, input_signal: Any, context: Optional[np.ndarray] = None) -> Dict[str, Any]:
        """
        Main processing pipeline for relevance realization.
        
        Implements the complete cognitive flowchart from input to adaptive output.
        
        Args:
            input_signal: Raw input to process
            context: Optional context vector for attention guidance
        
        Returns:
            Dictionary with processing results and emergent patterns
        """
        # Step 1: Feature Extraction
        if isinstance(input_signal, list) and all(isinstance(x, list) for x in input_signal):
            # Multiple feature vectors provided
            features_list = input_signal
        else:
            # Single input - extract features
            features = self.extract_features(input_signal)
            features_list = [features]
        
        # Step 2: Hypergraph Construction
        nodes, hyperedges = self.construct_hypergraph(features_list)
        
        # Step 3: Salience Mapping
        if context is None:
            # Default context based on average features
            if nodes:
                context = np.mean([node.features for node in nodes], axis=0)
            else:
                context = np.array([1.0, 0.5, 0.8])  # Default context
        
        # Step 4: Recursive Attention Allocation
        salient_edges = self.attention_mechanism.propagate_attention(
            hyperedges, context, self.attention_mechanism.threshold, self.recursion_depth
        )
        
        # Step 5: Emergent Pattern Selection
        chosen_pattern = emergent_pattern(salient_edges)
        ranked_patterns = rank_patterns(salient_edges)
        
        # Step 6: Adaptive Output
        result = {
            'input_features': features_list,
            'nodes': nodes,
            'total_hyperedges': len(hyperedges),
            'salient_hyperedges': salient_edges,
            'salient_count': len(salient_edges),
            'emergent_pattern': chosen_pattern,
            'ranked_patterns': ranked_patterns[:5],  # Top 5 patterns
            'context': context,
            'attention_state': self.attention_mechanism.get_attention_state()
        }
        
        # Record processing history
        self.processing_history.append({
            'timestamp': len(self.processing_history),
            'input_type': type(input_signal).__name__,
            'num_features': len(features_list),
            'num_nodes': len(nodes),
            'num_edges': len(hyperedges),
            'num_salient': len(salient_edges),
            'emergent_pattern_id': chosen_pattern.id if chosen_pattern else None
        })
        
        return result
    
    def get_processing_history(self) -> List[Dict[str, Any]]:
        """Get the complete processing history for analysis."""
        return self.processing_history
    
    def reset(self):
        """Reset the engine state."""
        self.attention_mechanism.attention_history.clear()
        self.processing_history.clear()