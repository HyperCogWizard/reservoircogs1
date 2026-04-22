"""
Test suite for the Relevance Realization Framework.

Tests hypergraph structures, attention mechanisms, pattern selection,
and recursive cognitive processing.
"""

import pytest
import numpy as np
from reservoirpy.relevance_realization import (
    Node, Hyperedge, AttentionMechanism, salience_score,
    RelevanceRealizationEngine, emergent_pattern, select_pattern,
    TriadicProcessor
)


class TestHypergraph:
    """Test hypergraph node and edge structures."""
    
    def test_node_creation(self):
        """Test node creation and properties."""
        node = Node('test_node', [0.5, 0.8, 0.3])
        assert node.id == 'test_node'
        assert np.allclose(node.features, [0.5, 0.8, 0.3])
    
    def test_node_equality(self):
        """Test node equality comparison."""
        node1 = Node('A', [1.0, 0.5])
        node2 = Node('A', [1.0, 0.5])
        node3 = Node('B', [1.0, 0.5])
        
        assert node1 == node2
        assert node1 != node3
    
    def test_hyperedge_creation(self):
        """Test hyperedge creation and properties."""
        node_a = Node('A', [0.5, 0.3])
        node_b = Node('B', [0.8, 0.2])
        edge = Hyperedge('E1', [node_a, node_b], 0.75)
        
        assert edge.id == 'E1'
        assert len(edge.nodes) == 2
        assert edge.weight == 0.75
    
    def test_hyperedge_combined_features(self):
        """Test hyperedge feature combination."""
        node_a = Node('A', [1.0, 2.0])
        node_b = Node('B', [3.0, 4.0])
        edge = Hyperedge('E1', [node_a, node_b], 0.5)
        
        combined = edge.get_combined_features()
        expected = np.array([4.0, 6.0])  # Sum of features
        assert np.allclose(combined, expected)


class TestAttentionMechanism:
    """Test attention and salience scoring."""
    
    def test_salience_score_basic(self):
        """Test basic salience scoring."""
        features = np.array([1.0, 2.0, 3.0])
        context = np.array([0.5, 1.0, 1.5])
        
        score = salience_score(features, context)
        expected = 1.0*0.5 + 2.0*1.0 + 3.0*1.5  # 7.0
        assert abs(score - expected) < 1e-9
    
    def test_salience_score_dimension_mismatch(self):
        """Test salience scoring with dimension mismatch."""
        features = np.array([1.0, 2.0])
        context = np.array([0.5, 1.0, 1.5])
        
        score = salience_score(features, context)
        expected = 1.0*0.5 + 2.0*1.0  # 2.5 (uses minimum dimension)
        assert abs(score - expected) < 1e-9
    
    def test_attention_mechanism_filtering(self):
        """Test attention mechanism edge filtering."""
        # Create test nodes and edges
        node_a = Node('A', [1.0, 1.0, 1.0])
        node_b = Node('B', [0.1, 0.1, 0.1])
        edge_high = Hyperedge('E1', [node_a], 0.8)
        edge_low = Hyperedge('E2', [node_b], 0.2)
        
        attention = AttentionMechanism(threshold=0.5)
        context = np.array([1.0, 1.0, 1.0])
        
        filtered = attention.update_attention([edge_high, edge_low], context, 2.0)
        
        # Only high-salience edge should pass
        assert len(filtered) == 1
        assert filtered[0].id == 'E1'
    
    def test_recursive_attention_propagation(self):
        """Test recursive attention propagation."""
        node_a = Node('A', [1.0, 1.0, 1.0])
        node_b = Node('B', [0.8, 0.8, 0.8])
        edge1 = Hyperedge('E1', [node_a], 0.9)
        edge2 = Hyperedge('E2', [node_b], 0.7)
        
        attention = AttentionMechanism()
        context = np.array([1.0, 1.0, 1.0])
        
        result = attention.propagate_attention([edge1, edge2], context, 2.0, depth=2)
        
        # Should have some filtering effect
        assert len(result) <= 2
        assert len(attention.attention_history) > 0


class TestPatternSelection:
    """Test pattern selection algorithms."""
    
    def test_emergent_pattern_selection(self):
        """Test emergent pattern selection."""
        node_a = Node('A', [1.0])
        node_b = Node('B', [1.0])
        edge1 = Hyperedge('E1', [node_a], 0.3)
        edge2 = Hyperedge('E2', [node_b], 0.8)
        edge3 = Hyperedge('E3', [node_a, node_b], 0.5)
        
        pattern = emergent_pattern([edge1, edge2, edge3])
        assert pattern.id == 'E2'  # Highest weight
    
    def test_emergent_pattern_empty_list(self):
        """Test emergent pattern with empty edge list."""
        pattern = emergent_pattern([])
        assert pattern is None
    
    def test_select_pattern_strategies(self):
        """Test different pattern selection strategies."""
        node_a = Node('A', [1.0])
        node_b = Node('B', [1.0])
        node_c = Node('C', [1.0])
        
        edge1 = Hyperedge('E1', [node_a], 0.3)
        edge2 = Hyperedge('E2', [node_b], 0.8)
        edge3 = Hyperedge('E3', [node_a, node_b, node_c], 0.5)  # 3 nodes
        
        edges = [edge1, edge2, edge3]
        
        # Test max_weight strategy
        max_weight = select_pattern(edges, 'max_weight')
        assert max_weight.id == 'E2'
        
        # Test min_weight strategy
        min_weight = select_pattern(edges, 'min_weight')
        assert min_weight.id == 'E1'
        
        # Test max_nodes strategy
        max_nodes = select_pattern(edges, 'max_nodes')
        assert max_nodes.id == 'E3'


class TestRelevanceRealizationEngine:
    """Test the main relevance realization engine."""
    
    def test_engine_initialization(self):
        """Test engine initialization."""
        engine = RelevanceRealizationEngine()
        assert engine.attention_mechanism is not None
        assert engine.recursion_depth == 2
        assert len(engine.processing_history) == 0
    
    def test_feature_extraction_numeric(self):
        """Test feature extraction from numeric input."""
        engine = RelevanceRealizationEngine()
        features = engine.extract_features(42.5)
        
        assert len(features) == 3
        assert features[0] == 42.5
        assert features[1] == 0.5  # Default novelty
        assert features[2] == 0.5  # Default coherence
    
    def test_feature_extraction_list(self):
        """Test feature extraction from list input."""
        engine = RelevanceRealizationEngine()
        features = engine.extract_features([1, 2, 3, 4, 5])
        
        assert len(features) == 3
        assert features[0] == 3.0  # Mean
        assert features[1] > 0     # Std dev
        assert features[2] == 5.0  # Length
    
    def test_hypergraph_construction(self):
        """Test hypergraph construction from features."""
        engine = RelevanceRealizationEngine()
        features_list = [[1.0, 0.5, 0.3], [0.8, 0.7, 0.2]]
        
        nodes, edges = engine.construct_hypergraph(features_list)
        
        assert len(nodes) == 2
        assert len(edges) >= 1  # At least pairwise edge
        assert all(isinstance(node, Node) for node in nodes)
        assert all(isinstance(edge, Hyperedge) for edge in edges)
    
    def test_full_processing_pipeline(self):
        """Test complete processing pipeline."""
        engine = RelevanceRealizationEngine()
        result = engine.process([1, 2, 3])
        
        # Check result structure
        required_keys = [
            'input_features', 'nodes', 'total_hyperedges', 
            'salient_hyperedges', 'emergent_pattern', 'context'
        ]
        for key in required_keys:
            assert key in result
        
        # Check processing history
        assert len(engine.processing_history) == 1
        assert 'num_features' in engine.processing_history[0]
    
    def test_processing_multiple_inputs(self):
        """Test processing with multiple feature vectors."""
        engine = RelevanceRealizationEngine()
        features_list = [[0.8, 0.3, 0.5], [0.4, 0.7, 0.2], [0.5, 0.2, 0.9]]
        
        result = engine.process(features_list)
        
        assert result['input_features'] == features_list
        assert len(result['nodes']) == 3
        assert result['total_hyperedges'] > 0


class TestTriadicIntegration:
    """Test triadic architecture integration."""
    
    def test_triadic_processor_initialization(self):
        """Test triadic processor initialization."""
        processor = TriadicProcessor()
        assert processor.relevance_engine is not None
        assert 'participatory' in processor.triadic_state
        assert 'perspectival' in processor.triadic_state
        assert 'propositional' in processor.triadic_state
    
    def test_participatory_processing(self):
        """Test participatory realm processing."""
        processor = TriadicProcessor()
        reservoir_states = np.array([[0.5, 0.8], [0.3, 0.7], [0.9, 0.2]])
        
        result = processor.process_participatory(reservoir_states)
        
        assert 'raw_states' in result
        assert 'relevance_result' in result
        assert 'emergent_patterns' in result
        assert np.array_equal(result['raw_states'], reservoir_states)
    
    def test_perspectival_processing(self):
        """Test perspectival realm processing."""
        processor = TriadicProcessor()
        attention_weights = np.array([0.8, 0.3, 0.6])
        context = np.array([1.0, 0.5, 0.7])
        
        result = processor.process_perspectival(attention_weights, context)
        
        assert 'attention_weights' in result
        assert 'context' in result
        assert 'relevance_result' in result
        assert np.array_equal(result['attention_weights'], attention_weights)
    
    def test_propositional_processing(self):
        """Test propositional realm processing."""
        processor = TriadicProcessor()
        concepts = ['concept1', 'concept2', 'pattern']
        
        result = processor.process_propositional(concepts)
        
        assert 'concepts' in result
        assert 'relevance_result' in result
        assert 'conceptual_patterns' in result
        assert result['concepts'] == concepts
    
    def test_realm_integration(self):
        """Test integration across all three realms."""
        processor = TriadicProcessor()
        
        # Process each realm
        participatory_result = processor.process_participatory(np.array([[0.5, 0.8]]))
        perspectival_result = processor.process_perspectival(np.array([0.7]), np.array([1.0]))
        propositional_result = processor.process_propositional(['test'])
        
        # Integrate results
        integrated = processor.integrate_realms(
            participatory_result, perspectival_result, propositional_result
        )
        
        assert 'triadic_state' in integrated
        assert 'pattern_coherence' in integrated
        assert 'coupling_strength' in integrated
        assert 'emergent_relevance' in integrated
        
        # Check coherence and coupling are valid probabilities
        assert 0.0 <= integrated['pattern_coherence'] <= 1.0
        assert 0.0 <= integrated['coupling_strength'] <= 1.0
        assert 0.0 <= integrated['emergent_relevance'] <= 1.0


class TestRelevanceRealizationFramework:
    """Integration tests for the complete framework."""
    
    def test_framework_structure_exists(self):
        """Test that framework structure exists properly."""
        from reservoirpy.relevance_realization import (
            Node, Hyperedge, AttentionMechanism, RelevanceRealizationEngine
        )
        
        # Framework components should be importable
        assert Node is not None
        assert Hyperedge is not None
        assert AttentionMechanism is not None
        assert RelevanceRealizationEngine is not None
    
    def test_end_to_end_processing(self):
        """Test end-to-end relevance realization processing."""
        # Create engine
        engine = RelevanceRealizationEngine(attention_threshold=0.6, recursion_depth=3)
        
        # Process various input types
        inputs = [
            42,  # Numeric
            [1, 2, 3, 4],  # List
            [[0.8, 0.3, 0.5], [0.4, 0.7, 0.2]]  # Feature vectors
        ]
        
        results = []
        for input_data in inputs:
            result = engine.process(input_data)
            results.append(result)
            
            # Verify basic result structure
            assert 'emergent_pattern' in result
            assert 'salient_count' in result
            assert result['salient_count'] >= 0
        
        # Verify processing history
        assert len(engine.processing_history) == len(inputs)
    
    def test_triadic_cognitive_pipeline(self):
        """Test complete triadic cognitive processing pipeline."""
        processor = TriadicProcessor()
        
        # Simulate reservoir computing data
        reservoir_states = np.random.randn(10, 5)
        attention_weights = np.random.rand(5)
        context = np.array([1.0, 0.8, 0.6, 0.4, 0.2])
        concepts = ['memory', 'attention', 'pattern', 'relevance']
        
        # Process through all realms
        participatory = processor.process_participatory(reservoir_states)
        perspectival = processor.process_perspectival(attention_weights, context)
        propositional = processor.process_propositional(concepts)
        
        # Integrate
        integrated = processor.integrate_realms(participatory, perspectival, propositional)
        
        # Verify integration produces meaningful results
        assert integrated['emergent_relevance'] >= 0.0
        assert 'integrated_patterns' in integrated
        
        patterns = integrated['integrated_patterns']
        assert 'participatory_count' in patterns
        assert 'perspectival_count' in patterns
        assert 'propositional_active' in patterns


if __name__ == '__main__':
    # Run basic demonstration if called directly
    print("Testing Relevance Realization Framework...")
    
    # Create example system
    engine = RelevanceRealizationEngine()
    
    # Test with sample data
    result = engine.process([[0.9, 0.6, 0.5], [0.3, 0.8, 0.4], [0.5, 0.2, 0.95]])
    
    print(f"Processed {len(result['input_features'])} feature vectors")
    print(f"Created {len(result['nodes'])} nodes")
    print(f"Generated {result['total_hyperedges']} total hyperedges")
    print(f"Found {result['salient_count']} salient patterns")
    
    if result['emergent_pattern']:
        print(f"Emergent pattern: {result['emergent_pattern'].id}")
    else:
        print("No emergent pattern found")
    
    print("Framework test completed successfully!")