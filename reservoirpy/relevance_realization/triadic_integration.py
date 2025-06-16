"""
Triadic integration for the Relevance Realization Framework.

Implements integration with the existing triadic architecture (Participatory,
Perspectival, Propositional) for cognitive synergy.
"""

from typing import Any, Dict, Optional, List
import numpy as np
from .recursive_engine import RelevanceRealizationEngine
from .hypergraph import Node, Hyperedge


class TriadicProcessor:
    """
    Integrates relevance realization with triadic cognitive architecture.
    
    Bridges the hypergraph-based relevance engine with the three realms:
    - Participatory: Dynamic state evolution
    - Perspectival: Selective attention mechanisms  
    - Propositional: Symbolic knowledge representation
    """
    
    def __init__(self, atomspace: Optional[Any] = None):
        """
        Initialize triadic processor.
        
        Args:
            atomspace: Optional AtomSpace for symbolic processing
        """
        self.atomspace = atomspace
        self.relevance_engine = RelevanceRealizationEngine()
        self.triadic_state = {
            'participatory': None,
            'perspectival': None, 
            'propositional': None
        }
    
    def process_participatory(self, reservoir_states: np.ndarray) -> Dict[str, Any]:
        """
        Process participatory realm through relevance realization.
        
        Args:
            reservoir_states: Dynamic reservoir state evolution
            
        Returns:
            Processed participatory information
        """
        # Convert reservoir states to hypergraph representation
        features_list = []
        for i, state in enumerate(reservoir_states):
            if isinstance(state, np.ndarray):
                # Extract features from state vector
                features = [float(state.mean()), float(state.std()), float(state.max())]
            else:
                features = [float(state), 0.5, 0.5]
            features_list.append(features)
        
        # Process through relevance engine
        result = self.relevance_engine.process(features_list)
        
        self.triadic_state['participatory'] = {
            'raw_states': reservoir_states,
            'relevance_result': result,
            'emergent_patterns': result.get('ranked_patterns', [])
        }
        
        return self.triadic_state['participatory']
    
    def process_perspectival(self, attention_weights: np.ndarray, context: np.ndarray) -> Dict[str, Any]:
        """
        Process perspectival realm through selective attention.
        
        Args:
            attention_weights: Current attention allocation
            context: Perspectival context vector
            
        Returns:
            Processed perspectival information
        """
        # Create hypergraph nodes from attention patterns
        attention_features = []
        for i, weight in enumerate(attention_weights):
            # Features: [attention_strength, selectivity, coherence]
            features = [float(weight), float(weight > 0.5), float(weight * context[i % len(context)])]
            attention_features.append(features)
        
        # Process with relevance engine using context
        result = self.relevance_engine.process(attention_features, context)
        
        self.triadic_state['perspectival'] = {
            'attention_weights': attention_weights,
            'context': context,
            'relevance_result': result,
            'filtered_patterns': result.get('salient_hyperedges', [])
        }
        
        return self.triadic_state['perspectival']
    
    def process_propositional(self, symbolic_concepts: List[str]) -> Dict[str, Any]:
        """
        Process propositional realm through symbolic knowledge.
        
        Args:
            symbolic_concepts: List of symbolic concept identifiers
            
        Returns:
            Processed propositional information
        """
        # Convert symbolic concepts to feature representation
        concept_features = []
        for i, concept in enumerate(symbolic_concepts):
            # Simple encoding: concept length, hash, position
            features = [
                float(len(concept)) / 20.0,  # Normalized length
                float(hash(concept) % 100) / 100.0,  # Normalized hash
                float(i) / len(symbolic_concepts)  # Position
            ]
            concept_features.append(features)
        
        # Process through relevance engine
        result = self.relevance_engine.process(concept_features)
        
        # Integrate with AtomSpace if available
        symbolic_integration = None
        if self.atomspace is not None:
            symbolic_integration = self._integrate_with_atomspace(result, symbolic_concepts)
        
        self.triadic_state['propositional'] = {
            'concepts': symbolic_concepts,
            'relevance_result': result,
            'symbolic_integration': symbolic_integration,
            'conceptual_patterns': result.get('emergent_pattern')
        }
        
        return self.triadic_state['propositional']
    
    def _integrate_with_atomspace(self, relevance_result: Dict[str, Any], 
                                 concepts: List[str]) -> Dict[str, Any]:
        """
        Integrate relevance results with AtomSpace symbolic reasoning.
        
        Args:
            relevance_result: Results from relevance engine
            concepts: Original symbolic concepts
            
        Returns:
            Integration results
        """
        # Placeholder for AtomSpace integration
        # In full implementation, this would create atoms and links
        return {
            'integrated_concepts': len(concepts),
            'emergent_atoms': relevance_result.get('salient_count', 0),
            'symbolic_coherence': 0.8  # Placeholder coherence measure
        }
    
    def integrate_realms(self, participatory_result: Dict[str, Any],
                        perspectival_result: Dict[str, Any],
                        propositional_result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Integrate results from all three realms into unified output.
        
        Args:
            participatory_result: Results from participatory processing
            perspectival_result: Results from perspectival processing  
            propositional_result: Results from propositional processing
            
        Returns:
            Integrated triadic output
        """
        # Extract emergent patterns from each realm
        participatory_patterns = participatory_result.get('emergent_patterns', [])
        perspectival_patterns = perspectival_result.get('filtered_patterns', [])
        propositional_pattern = propositional_result.get('conceptual_patterns')
        
        # Compute integration measures
        pattern_coherence = self._compute_pattern_coherence(
            participatory_patterns, perspectival_patterns, propositional_pattern
        )
        
        cross_realm_coupling = self._compute_coupling_strength(
            participatory_result, perspectival_result, propositional_result
        )
        
        # Create integrated output
        integrated_output = {
            'triadic_state': self.triadic_state.copy(),
            'pattern_coherence': pattern_coherence,
            'coupling_strength': cross_realm_coupling,
            'emergent_relevance': self._compute_emergent_relevance(),
            'integrated_patterns': {
                'participatory_count': len(participatory_patterns),
                'perspectival_count': len(perspectival_patterns),
                'propositional_active': propositional_pattern is not None
            }
        }
        
        return integrated_output
    
    def _compute_pattern_coherence(self, participatory_patterns: List[Any],
                                 perspectival_patterns: List[Any],
                                 propositional_pattern: Any) -> float:
        """Compute coherence across triadic patterns."""
        # Simple coherence based on pattern counts and alignment
        total_patterns = len(participatory_patterns) + len(perspectival_patterns)
        if propositional_pattern is not None:
            total_patterns += 1
        
        if total_patterns == 0:
            return 0.0
        
        # Coherence increases with balanced patterns across realms
        balance_factor = 1.0 - abs(len(participatory_patterns) - len(perspectival_patterns)) / max(1, total_patterns)
        return min(1.0, balance_factor * 0.8 + 0.2)
    
    def _compute_coupling_strength(self, *realm_results) -> float:
        """Compute coupling strength between realms."""
        # Measure how well the realms are coupled based on result similarity
        coupling_scores = []
        
        for i, result1 in enumerate(realm_results):
            for j, result2 in enumerate(realm_results[i+1:], i+1):
                # Simple coupling based on salient count similarity
                count1 = result1.get('relevance_result', {}).get('salient_count', 0)
                count2 = result2.get('relevance_result', {}).get('salient_count', 0)
                
                if count1 + count2 > 0:
                    similarity = 1.0 - abs(count1 - count2) / (count1 + count2)
                    coupling_scores.append(similarity)
        
        return np.mean(coupling_scores) if coupling_scores else 0.0
    
    def _compute_emergent_relevance(self) -> float:
        """Compute overall emergent relevance from triadic integration."""
        # Combine relevance measures from all realms
        relevance_scores = []
        
        for realm_name, realm_state in self.triadic_state.items():
            if realm_state and 'relevance_result' in realm_state:
                salient_count = realm_state['relevance_result'].get('salient_count', 0)
                total_count = realm_state['relevance_result'].get('total_hyperedges', 1)
                realm_relevance = salient_count / max(1, total_count)
                relevance_scores.append(realm_relevance)
        
        return np.mean(relevance_scores) if relevance_scores else 0.0
    
    def reset(self):
        """Reset triadic processor state."""
        self.relevance_engine.reset()
        self.triadic_state = {
            'participatory': None,
            'perspectival': None,
            'propositional': None
        }