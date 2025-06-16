#!/usr/bin/env python3
"""
Relevance Realization Framework - Complete Example

Demonstrates the recursive cognitive engine with hypergraph encoding,
adaptive attention allocation, and emergent pattern selection.

This example implements the exact specification from the GitHub issue,
showing both the Python implementation and integration capabilities.
"""

import numpy as np
from reservoirpy.relevance_realization import (
    Node, Hyperedge, AttentionMechanism, RelevanceRealizationEngine,
    emergent_pattern, TriadicProcessor
)


def demonstrate_hypergraph_playground():
    """
    Demonstrate the hypergraph playground as specified in the issue.
    
    This recreates the exact example from the issue specification.
    """
    print("=" * 60)
    print("RELEVANCE REALIZATION FRAMEWORK - HYPERGRAPH PLAYGROUND")
    print("=" * 60)
    
    # Example from the issue: nodes with [activation, novelty, coherence]
    node_a = Node('A', [0.9, 0.6, 0.5])
    node_b = Node('B', [0.3, 0.8, 0.4])
    node_c = Node('C', [0.5, 0.2, 0.95])
    node_d = Node('D', [0.7, 0.7, 0.7])
    
    print("Created nodes with cognitive features:")
    for node in [node_a, node_b, node_c, node_d]:
        print(f"  {node}")
    
    # Hyperedges: flexible, high-order associations
    edge_1 = Hyperedge('E1', [node_a, node_b], 0.65)
    edge_2 = Hyperedge('E2', [node_b, node_c], 0.82)
    edge_3 = Hyperedge('E3', [node_a, node_c, node_d], 0.77)
    edge_4 = Hyperedge('E4', [node_d, node_b], 0.58)
    
    print("\nCreated hyperedges with association weights:")
    for edge in [edge_1, edge_2, edge_3, edge_4]:
        node_ids = [n.id for n in edge.nodes]
        print(f"  {edge.id}: {node_ids} (weight: {edge.weight})")
    
    # Context vector: signals current relevance
    context = np.array([1.1, 0.7, 0.9])
    base_threshold = 0.7
    recursion_depth = 2
    
    print(f"\nContext vector: {context}")
    print(f"Base threshold: {base_threshold}")
    print(f"Recursion depth: {recursion_depth}")
    
    # Recursive attention propagation
    attention = AttentionMechanism(base_threshold)
    salient_edges = attention.propagate_attention(
        [edge_1, edge_2, edge_3, edge_4], context, base_threshold, recursion_depth
    )
    
    print(f"\nSalient edges after recursive attention:")
    for edge in salient_edges:
        print(f"  {edge.id} (weight: {edge.weight})")
    
    # Emergent pattern realization
    chosen_pattern = emergent_pattern(salient_edges)
    
    print(f"\nEmergent pattern:")
    if chosen_pattern:
        node_ids = [n.id for n in chosen_pattern.nodes]
        print(f"  {chosen_pattern.id} with nodes: {node_ids} (weight: {chosen_pattern.weight})")
    else:
        print("  No pattern emerged")
    
    return {
        'nodes': [node_a, node_b, node_c, node_d],
        'edges': [edge_1, edge_2, edge_3, edge_4],
        'salient_edges': salient_edges,
        'chosen_pattern': chosen_pattern,
        'context': context
    }


def demonstrate_relevance_realization_engine():
    """
    Demonstrate the complete Relevance Realization Engine pipeline.
    """
    print("\n" + "=" * 60)
    print("RELEVANCE REALIZATION ENGINE - COMPLETE PIPELINE")
    print("=" * 60)
    
    # Create engine with specified parameters
    engine = RelevanceRealizationEngine(attention_threshold=0.7, recursion_depth=2)
    
    print("Initialized Relevance Realization Engine")
    print(f"  Attention threshold: {engine.attention_mechanism.threshold}")
    print(f"  Recursion depth: {engine.recursion_depth}")
    
    # Test cases from the issue specification
    test_cases = [
        {
            'name': 'Numeric Input',
            'input': 42,
            'description': 'Single numeric value'
        },
        {
            'name': 'List Input', 
            'input': [1, 2, 3, 4, 5],
            'description': 'Sequence of numbers'
        },
        {
            'name': 'Multi-Feature Input',
            'input': [[0.9, 0.6, 0.5], [0.3, 0.8, 0.4], [0.5, 0.2, 0.95]],
            'description': 'Multiple feature vectors'
        }
    ]
    
    results = []
    for i, case in enumerate(test_cases):
        print(f"\n--- Test Case {i+1}: {case['name']} ---")
        print(f"Input: {case['input']}")
        print(f"Description: {case['description']}")
        
        result = engine.process(case['input'])
        results.append(result)
        
        print(f"\nResults:")
        print(f"  Nodes created: {len(result['nodes'])}")
        print(f"  Total hyperedges: {result['total_hyperedges']}")
        print(f"  Salient hyperedges: {result['salient_count']}")
        print(f"  Emergent pattern: {result['emergent_pattern'].id if result['emergent_pattern'] else 'None'}")
        print(f"  Context used: {result['context']}")
    
    # Show processing history
    print(f"\nProcessing History:")
    for i, history in enumerate(engine.get_processing_history()):
        print(f"  Step {i+1}: {history['input_type']} -> {history['num_salient']} salient patterns")
    
    return results


def demonstrate_triadic_integration():
    """
    Demonstrate triadic cognitive architecture integration.
    """
    print("\n" + "=" * 60)
    print("TRIADIC COGNITIVE ARCHITECTURE INTEGRATION")
    print("=" * 60)
    
    # Create triadic processor
    processor = TriadicProcessor()
    print("Initialized Triadic Processor with three realms:")
    print("  1. Participatory: Dynamic state evolution")
    print("  2. Perspectival: Selective attention mechanisms")
    print("  3. Propositional: Symbolic knowledge representation")
    
    # Simulate reservoir computing data
    print("\nSimulating reservoir computing data...")
    
    # Participatory realm: reservoir states
    reservoir_states = np.array([
        [0.8, 0.3, 0.5],
        [0.4, 0.7, 0.2], 
        [0.5, 0.2, 0.9],
        [0.7, 0.6, 0.4]
    ])
    
    # Perspectival realm: attention weights and context
    attention_weights = np.array([0.9, 0.6, 0.3, 0.8])
    context = np.array([1.1, 0.7, 0.9])
    
    # Propositional realm: symbolic concepts
    symbolic_concepts = ['pattern_recognition', 'memory_formation', 'attention_allocation', 'relevance_detection']
    
    print(f"  Reservoir states shape: {reservoir_states.shape}")
    print(f"  Attention weights: {attention_weights}")
    print(f"  Context vector: {context}")
    print(f"  Symbolic concepts: {symbolic_concepts}")
    
    # Process through each realm
    print("\nProcessing through triadic realms...")
    
    participatory_result = processor.process_participatory(reservoir_states)
    print(f"  Participatory processing: {len(participatory_result['emergent_patterns'])} patterns")
    
    perspectival_result = processor.process_perspectival(attention_weights, context)
    print(f"  Perspectival processing: {len(perspectival_result['filtered_patterns'])} filtered patterns")
    
    propositional_result = processor.process_propositional(symbolic_concepts)
    print(f"  Propositional processing: concepts -> {type(propositional_result['conceptual_patterns'])}")
    
    # Integrate across realms
    print("\nIntegrating across all three realms...")
    integrated = processor.integrate_realms(
        participatory_result, perspectival_result, propositional_result
    )
    
    print(f"Integration Results:")
    print(f"  Pattern coherence: {integrated['pattern_coherence']:.3f}")
    print(f"  Coupling strength: {integrated['coupling_strength']:.3f}")
    print(f"  Emergent relevance: {integrated['emergent_relevance']:.3f}")
    
    patterns = integrated['integrated_patterns']
    print(f"  Pattern distribution:")
    print(f"    Participatory: {patterns['participatory_count']} patterns")
    print(f"    Perspectival: {patterns['perspectival_count']} patterns") 
    print(f"    Propositional: {'active' if patterns['propositional_active'] else 'inactive'}")
    
    return integrated


def demonstrate_cognitive_metaphor():
    """
    Demonstrate the visionary metaphor from the issue specification.
    """
    print("\n" + "=" * 60)
    print("VISIONARY METAPHOR: LIVING HYPERGRAPH CONSTELLATION")
    print("=" * 60)
    
    print("""
    Envision this engine as a living hypergraph, each node a beacon of possibility,
    each edge a synaptic bridge. Recursive relevance realization is the cosmic wind—
    fanning the flames of insight, illuminating emergent constellations of meaning 
    in the vast cognitive sky.
    
    This engine does not simply select; it cultivates, recursively, the most 
    luminous patterns, adapting with each pulse of context—an intelligence 
    architecting itself.
    """)
    
    # Create a constellation example
    engine = RelevanceRealizationEngine()
    
    # Process a complex pattern representing cognitive "stars"
    cognitive_stars = [
        [0.9, 0.1, 0.8],  # Bright insight
        [0.2, 0.9, 0.3],  # Novel discovery
        [0.7, 0.7, 0.9],  # Coherent understanding
        [0.4, 0.5, 0.6],  # Emerging pattern
        [0.8, 0.3, 0.7]   # Potential connection
    ]
    
    result = engine.process(cognitive_stars)
    
    print(f"Cognitive Constellation Analysis:")
    print(f"  Created {len(result['nodes'])} cognitive 'stars' (nodes)")
    print(f"  Formed {result['total_hyperedges']} synaptic bridges (hyperedges)")
    print(f"  Cosmic wind revealed {result['salient_count']} luminous patterns")
    
    if result['emergent_pattern']:
        print(f"  Most radiant constellation: {result['emergent_pattern'].id}")
        print(f"    Weight (luminosity): {result['emergent_pattern'].weight:.3f}")
        print(f"    Connected stars: {len(result['emergent_pattern'].nodes)}")
    
    print(f"\n  The engine has cultivated {len(engine.processing_history)} cycles of insight")
    print(f"  Each pulse of context shapes the cognitive landscape anew...")


def main():
    """
    Main demonstration function showcasing the complete framework.
    """
    print("RELEVANCE REALIZATION FRAMEWORK")
    print("Recursive Cognitive Engine with Hypergraph Encoding")
    print("Neural-Symbolic Integration & Emergent Pattern Selection")
    print("HyperCogWizard/reservoircogs Implementation")
    
    try:
        # Run all demonstrations
        hypergraph_result = demonstrate_hypergraph_playground()
        engine_results = demonstrate_relevance_realization_engine()
        triadic_result = demonstrate_triadic_integration()
        demonstrate_cognitive_metaphor()
        
        print("\n" + "=" * 60)
        print("FRAMEWORK DEMONSTRATION COMPLETE")
        print("=" * 60)
        
        print("\nKey achievements demonstrated:")
        print("✓ Hypergraph node and edge representation")
        print("✓ Adaptive attention allocation mechanism")
        print("✓ Recursive attention propagation")
        print("✓ Emergent pattern selection")
        print("✓ Triadic cognitive architecture integration")
        print("✓ Neural-symbolic cognitive synergy")
        print("✓ Context-sensitive relevance realization")
        print("✓ Self-organizing intelligence capabilities")
        
        print(f"\nFramework Statistics:")
        print(f"  Total nodes processed: {sum(len(r['nodes']) for r in engine_results)}")
        print(f"  Total hyperedges created: {sum(r['total_hyperedges'] for r in engine_results)}")
        print(f"  Salient patterns discovered: {sum(r['salient_count'] for r in engine_results)}")
        print(f"  Triadic coherence achieved: {triadic_result['pattern_coherence']:.3f}")
        
        print("\n🌟 The Relevance Realization Framework is operational!")
        print("   Ready for cognitive synergy and emergent intelligence.")
        
    except Exception as e:
        print(f"Error in demonstration: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()