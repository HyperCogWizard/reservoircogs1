# Formal Grammar RR - Relevance Realization P-Systems

## Overview

This document explores the intersection of formal grammar theory, Relevance Realization (RR), and P-Systems (membrane computing) within the context of reservoir computing. It provides a comprehensive framework for understanding how symbolic computation through membrane-based P-Systems can be enhanced with relevance-sensitive formal grammars.

## Table of Contents

1. [Formal Grammar Foundations](#formal-grammar-foundations)
2. [P-Systems Architecture](#p-systems-architecture)
3. [Relevance-Guided Grammar Rules](#relevance-guided-grammar-rules)
4. [Membrane-Based Computation](#membrane-based-computation)
5. [Integration with Reservoir Computing](#integration-with-reservoir-computing)
6. [Implementation Framework](#implementation-framework)
7. [Mathematical Formalization](#mathematical-formalization)
8. [Applications and Examples](#applications-and-examples)

## Formal Grammar Foundations

### Classical Formal Grammars

A formal grammar G is defined as a 4-tuple:
```
G = (N, T, P, S)
```

Where:
- `N`: Set of non-terminal symbols
- `T`: Set of terminal symbols (alphabet)
- `P`: Set of production rules
- `S`: Start symbol (S ∈ N)

### Relevance-Enhanced Grammars

We extend classical grammars with relevance functions:
```
G_RR = (N, T, P_RR, S, R, C)
```

Additional components:
- `R`: Relevance function R: (N ∪ T) × C → [0,1]
- `C`: Context space
- `P_RR`: Relevance-weighted production rules

### Production Rules with Relevance

Each production rule is enhanced with relevance conditions:
```
A →[r,c] α | β | γ
```

Where:
- `A`: Non-terminal symbol
- `α, β, γ`: Alternative productions
- `r`: Relevance threshold
- `c`: Context condition

The rule fires only if:
```
R(A, context) ≥ r AND context ∈ c
```

## P-Systems Architecture

### Basic P-System Structure

A P-System for relevance realization is defined as:
```
Π = (V, μ, w₁, w₂, ..., wₘ, R₁, R₂, ..., Rₘ, i₀, RR)
```

Extended components:
- `V`: Working alphabet (including relevance symbols)
- `μ`: Membrane structure with relevance channels
- `wᵢ`: Initial multiset with relevance annotations
- `Rᵢ`: Evolution rules with relevance conditions
- `i₀`: Output designation
- `RR`: Relevance realization engine

### Membrane Hierarchy for RR

The membrane structure reflects the triadic architecture:

```
Environment [₁
    Participatory [₂
        Short-term Memory [₃]₃
        Pattern Buffer [₄]₄
    ]₂
    Perspectival [₅
        Attention Filter [₆]₆
        Relevance Detector [₇]₇
    ]₅
    Propositional [₈
        Concept Storage [₉]₉
        Rule Base [₁₀]₁₀
    ]₈
]₁
```

### Relevance Symbols in Alphabet

The working alphabet includes relevance markers:
```
V = V_base ∪ V_relevance
V_relevance = {⊕ʳ, ⊖ʳ, ∼ʳ, ↕ʳ}
```

Where:
- `⊕ʳ`: High relevance marker
- `⊖ʳ`: Low relevance marker  
- `∼ʳ`: Neutral relevance marker
- `↕ʳ`: Relevance conflict marker

## Relevance-Guided Grammar Rules

### Context-Sensitive Productions

Productions adapt based on membrane context:

```
[A]ᵢ →[r≥θ] [α]ⱼ, if context(i) satisfies relevance_condition
```

Examples:

#### Memory Formation
```
[input·data]₂ →[r≥0.7] [short_term·memory]₃ ⊕ʳ
```

#### Attention Focusing
```
[pattern·candidate]₄ →[r≥0.8] [attended·pattern]₆ ⊕ʳ
[pattern·candidate]₄ →[r<0.3] [ignored·pattern]₄ ⊖ʳ
```

#### Concept Formation
```
[attended·pattern]₆ + [rule·template]₁₀ →[r≥0.9] [concept]₉ ⊕ʳ
```

### Dynamic Relevance Updates

Relevance values evolve based on success/failure:

```
R(symbol, context, t+1) = λ·R(symbol, context, t) + (1-λ)·feedback(t)
```

Where:
- `λ`: Decay parameter
- `feedback(t)`: Success/failure signal at time t

### Grammar Rule Evolution

Production rules can evolve based on usage and success:

```
P_new = P_old ∪ {discovered_rules} - {ineffective_rules}
```

Discovery criteria:
- High frequency co-occurrence
- Strong relevance correlation
- Successful outcome association

## Membrane-Based Computation

### Evolution Rules with Relevance

Each membrane type has specialized evolution rules:

#### Participatory Membrane (Short-term Memory)
```
Rules₃:
- a·⊕ʳ → a·a    (amplify relevant symbols)
- a·⊖ʳ → ε      (decay irrelevant symbols)
- a·b → c, if similarity(a,b) > δ ∧ relevance(c) > θ
```

#### Perspectival Membrane (Attention Filter)
```
Rules₆:
- pattern·⊕ʳ → attended_pattern·⊕ʳ
- pattern·⊖ʳ → ε
- attended_pattern → focused_pattern, if sustained_attention > τ
```

#### Propositional Membrane (Concept Storage)
```
Rules₉:
- concept₁·concept₂ → relation(concept₁, concept₂), if R(relation) > θ
- isolated_concept → ε, if age > max_age ∧ R(concept) < θ_min
```

### Inter-Membrane Communication

Membranes communicate through relevance-tagged messages:

```
send(message·⊕ʳ, from_membrane, to_membrane)
receive(message·⊕ʳ, membrane) → process(message, membrane)
```

Communication rules:
- Only relevance-tagged messages are transmitted
- Higher relevance = higher transmission priority
- Messages decay if not processed within time limit

### Computational Complexity

The computational complexity depends on:
- Number of membranes: O(m)
- Average objects per membrane: O(n)
- Evolution steps: O(t)
- Relevance calculations: O(r)

Total complexity: O(m·n·t·r)

## Integration with Reservoir Computing

### Reservoir as P-System

Map reservoir components to P-System elements:

```
Reservoir ↔ P-System Mapping:
- Neurons ↔ Membrane objects
- Connections ↔ Evolution rules
- Activation ↔ Object multiplicity
- Input ↔ Environmental input
- States ↔ Membrane configurations
```

### Grammar-Guided Reservoir Evolution

The reservoir's state evolution follows grammar rules:

```Python
def grammar_guided_evolution(reservoir_state, grammar, context):
    """Evolve reservoir according to relevance grammar."""
    
    # Parse current state as grammar symbols
    symbols = parse_state_as_symbols(reservoir_state)
    
    # Apply relevance-sensitive productions
    new_symbols = []
    for symbol in symbols:
        relevance = grammar.compute_relevance(symbol, context)
        
        if relevance >= grammar.threshold:
            # Apply high-relevance productions
            productions = grammar.get_productions(symbol, 'high_relevance')
        else:
            # Apply low-relevance productions
            productions = grammar.get_productions(symbol, 'low_relevance')
        
        # Select production based on context
        selected_production = select_production(productions, context)
        new_symbols.extend(apply_production(symbol, selected_production))
    
    # Convert symbols back to reservoir state
    return symbols_to_state(new_symbols)
```

### Membrane-Reservoir Hybrid

Combine membrane computing with reservoir dynamics:

```Python
class MembraneReservoir:
    def __init__(self, membrane_structure, grammar, reservoir_params):
        self.membranes = initialize_membranes(membrane_structure)
        self.grammar = grammar
        self.reservoir = Reservoir(**reservoir_params)
        self.relevance_engine = RelevanceEngine()
    
    def evolve_step(self, input_data, context):
        # Standard reservoir update
        reservoir_state = self.reservoir.update(input_data)
        
        # Parse reservoir state into symbols
        symbols = self.parse_state(reservoir_state)
        
        # Distribute symbols to appropriate membranes
        self.distribute_symbols(symbols)
        
        # Apply membrane evolution rules
        for membrane in self.membranes:
            membrane.evolve_with_grammar(self.grammar, context)
        
        # Collect membrane outputs
        membrane_outputs = self.collect_outputs()
        
        # Integrate with reservoir
        integrated_state = self.integrate(reservoir_state, membrane_outputs)
        
        return integrated_state
```

## Mathematical Formalization

### Formal Language Definition

The language generated by a relevance-realization P-System grammar:

```
L(G_RR) = {w ∈ T* | S ⇒*[R,C] w ∧ ∀i: R(wᵢ, cᵢ) ≥ θ}
```

Where:
- `⇒*[R,C]`: Derivation sequence under relevance conditions
- `wᵢ`: Substring at position i
- `cᵢ`: Context at position i
- `θ`: Global relevance threshold

### Relevance Function Properties

The relevance function must satisfy:

1. **Monotonicity**: R(w₁, c) ≤ R(w₁w₂, c) for relevant w₂
2. **Context Sensitivity**: R(w, c₁) ≠ R(w, c₂) if c₁ ≠ c₂
3. **Boundedness**: 0 ≤ R(w, c) ≤ 1
4. **Continuity**: Small context changes → small relevance changes

### P-System Semantics

The semantics of a relevance P-System:

```
⟦Π⟧ = {(w, R_sequence) | Π generates w with relevance sequence R_sequence}
```

Where:
- `w`: Generated string
- `R_sequence`: Sequence of relevance values during generation

### Computational Power

Relevance-enhanced P-Systems with membrane structure have computational power equivalent to:
- Context-sensitive grammars (Type 1) for basic operations
- Unrestricted grammars (Type 0) with relevance feedback loops
- Polynomial-time solutions for many NP problems through membrane parallelism

## Implementation Framework

### Core Classes

```Python
class RelevanceGrammar:
    """Grammar with relevance-weighted productions."""
    
    def __init__(self, terminals, non_terminals, start_symbol):
        self.terminals = terminals
        self.non_terminals = non_terminals
        self.start_symbol = start_symbol
        self.productions = {}
        self.relevance_function = None
    
    def add_production(self, lhs, rhs, relevance_condition):
        """Add a production rule with relevance condition."""
        self.productions[lhs] = self.productions.get(lhs, [])
        self.productions[lhs].append((rhs, relevance_condition))
    
    def set_relevance_function(self, func):
        """Set the relevance computation function."""
        self.relevance_function = func
    
    def apply_production(self, symbol, context):
        """Apply most relevant production for symbol in context."""
        if symbol not in self.productions:
            return [symbol]
        
        best_production = None
        best_relevance = -1
        
        for rhs, condition in self.productions[symbol]:
            relevance = self.relevance_function(symbol, context)
            if condition(relevance, context) and relevance > best_relevance:
                best_production = rhs
                best_relevance = relevance
        
        return best_production if best_production else [symbol]

class PSysMembrane:
    """Individual membrane in P-System."""
    
    def __init__(self, membrane_id, initial_objects):
        self.id = membrane_id
        self.objects = initial_objects.copy()
        self.evolution_rules = []
        self.child_membranes = []
        self.parent_membrane = None
    
    def add_evolution_rule(self, rule):
        """Add evolution rule to membrane."""
        self.evolution_rules.append(rule)
    
    def evolve_step(self, grammar, context):
        """Apply evolution rules for one step."""
        new_objects = []
        
        for obj in self.objects:
            # Apply grammar productions
            evolved = grammar.apply_production(obj, context)
            new_objects.extend(evolved)
        
        # Apply membrane-specific evolution rules
        for rule in self.evolution_rules:
            new_objects = rule.apply(new_objects, context)
        
        self.objects = new_objects

class RelevancePSystem:
    """Complete P-System with relevance realization."""
    
    def __init__(self, membrane_structure, grammar):
        self.membranes = self._build_membranes(membrane_structure)
        self.grammar = grammar
        self.environment = self.membranes[0]  # Root membrane
        self.relevance_engine = RelevanceEngine()
    
    def compute_configuration(self):
        """Compute current system configuration."""
        config = {}
        for membrane in self.membranes:
            config[membrane.id] = membrane.objects.copy()
        return config
    
    def evolve(self, steps, input_sequence, context_sequence):
        """Evolve P-System for specified steps."""
        configurations = [self.compute_configuration()]
        
        for step in range(steps):
            # Get current input and context
            current_input = input_sequence[step % len(input_sequence)]
            current_context = context_sequence[step % len(context_sequence)]
            
            # Inject input into environment
            self.environment.objects.extend(current_input)
            
            # Evolve all membranes
            for membrane in self.membranes:
                membrane.evolve_step(self.grammar, current_context)
            
            # Store configuration
            configurations.append(self.compute_configuration())
        
        return configurations
```

### Integration with ReservoirCogs

```Python
from reservoirpy.nodes import Reservoir, Ridge
from reservoircogs.psystems import RelevancePSystem
from reservoircogs.grammar import RelevanceGrammar

class PSysReservoirNode:
    """Reservoir node enhanced with P-System grammar."""
    
    def __init__(self, reservoir_size, grammar_config, psys_config):
        # Standard reservoir
        self.reservoir = Reservoir(
            units=reservoir_size,
            lr=0.3,
            sr=0.9
        )
        
        # P-System components
        self.grammar = RelevanceGrammar(**grammar_config)
        self.psystem = RelevancePSystem(**psys_config)
        
        # Integration layer
        self.state_parser = StateSymbolParser()
        self.symbol_integrator = SymbolStateIntegrator()
    
    def __call__(self, input_data, **kwargs):
        # Standard reservoir processing
        reservoir_state = self.reservoir(input_data)
        
        # Parse state into symbols
        symbols = self.state_parser.parse(reservoir_state)
        
        # Process through P-System
        context = self._extract_context(input_data, reservoir_state)
        psys_output = self.psystem.process_symbols(symbols, context)
        
        # Integrate back into reservoir state
        enhanced_state = self.symbol_integrator.integrate(
            reservoir_state, psys_output
        )
        
        return enhanced_state
```

## Applications and Examples

### Natural Language Processing

Using relevance-guided P-System grammars for syntax parsing:

```Python
# Define grammar for English syntax with relevance
syntax_grammar = RelevanceGrammar(
    terminals=['the', 'cat', 'sat', 'on', 'mat'],
    non_terminals=['S', 'NP', 'VP', 'PP'],
    start_symbol='S'
)

# Add relevance-sensitive productions
syntax_grammar.add_production(
    'S', ['NP', 'VP'], 
    lambda r, c: r > 0.8 and 'subject_verb' in c
)

syntax_grammar.add_production(
    'NP', ['the', 'cat'],
    lambda r, c: r > 0.7 and 'definite_article' in c
)

# Create P-System for parsing
parsing_membranes = {
    'input': ['the', 'cat', 'sat', 'on', 'the', 'mat'],
    'syntax': [],
    'semantics': [],
    'output': []
}

parser_psystem = RelevancePSystem(parsing_membranes, syntax_grammar)

# Parse with relevance guidance
parse_result = parser_psystem.evolve(
    steps=10,
    input_sequence=[['the', 'cat', 'sat', 'on', 'the', 'mat']],
    context_sequence=[{'task': 'parsing', 'language': 'english'}]
)
```

### Time Series Pattern Recognition

Applying to temporal pattern recognition in reservoir computing:

```Python
# Define temporal pattern grammar
temporal_grammar = RelevanceGrammar(
    terminals=['rising', 'falling', 'steady', 'peak', 'trough'],
    non_terminals=['Pattern', 'Trend', 'Event'],
    start_symbol='Pattern'
)

# Relevance based on recency and magnitude
def temporal_relevance(symbol, context):
    recency = context.get('recency', 0)
    magnitude = context.get('magnitude', 0)
    return 0.3 * recency + 0.7 * magnitude

temporal_grammar.set_relevance_function(temporal_relevance)

# Add temporal productions
temporal_grammar.add_production(
    'Pattern', ['Trend', 'Event'],
    lambda r, c: r > 0.6 and c.get('window_size', 0) > 5
)

# Integrate with reservoir for time series analysis
reservoir_psys = PSysReservoirNode(
    reservoir_size=100,
    grammar_config={'grammar': temporal_grammar},
    psys_config={'membranes': temporal_membranes}
)

# Process time series data
time_series = load_time_series_data()
enhanced_states = []

for t, data_point in enumerate(time_series):
    context = {
        'recency': 1.0 / (t + 1),
        'magnitude': abs(data_point),
        'window_size': min(t + 1, 10)
    }
    
    state = reservoir_psys(data_point, context=context)
    enhanced_states.append(state)
```

### Adaptive Learning

Using P-System evolution for adaptive learning:

```Python
class AdaptivePSysGrammar:
    """Grammar that evolves based on success/failure feedback."""
    
    def __init__(self, base_grammar):
        self.base_grammar = base_grammar
        self.production_scores = {}
        self.evolution_rate = 0.1
    
    def add_feedback(self, used_productions, success):
        """Update production scores based on feedback."""
        feedback_value = 1.0 if success else -0.5
        
        for production in used_productions:
            current_score = self.production_scores.get(production, 0.0)
            self.production_scores[production] = (
                current_score + self.evolution_rate * feedback_value
            )
    
    def evolve_grammar(self):
        """Evolve grammar based on accumulated scores."""
        # Remove low-scoring productions
        threshold = -2.0
        productions_to_remove = [
            prod for prod, score in self.production_scores.items()
            if score < threshold
        ]
        
        for prod in productions_to_remove:
            self.base_grammar.remove_production(prod)
        
        # Add high-scoring variations
        high_scoring = [
            prod for prod, score in self.production_scores.items()
            if score > 2.0
        ]
        
        for prod in high_scoring:
            variations = self.generate_variations(prod)
            for variation in variations:
                self.base_grammar.add_production(*variation)

# Example usage in online learning scenario
adaptive_grammar = AdaptivePSysGrammar(base_grammar)
online_psystem = RelevancePSystem(membranes, adaptive_grammar.base_grammar)

for episode in range(num_episodes):
    # Process episode
    configurations = online_psystem.evolve(
        steps=episode_length,
        input_sequence=episode_inputs,
        context_sequence=episode_contexts
    )
    
    # Evaluate performance
    success = evaluate_episode_performance(configurations, targets)
    
    # Provide feedback to grammar
    used_productions = extract_used_productions(configurations)
    adaptive_grammar.add_feedback(used_productions, success)
    
    # Evolve grammar every 10 episodes
    if episode % 10 == 0:
        adaptive_grammar.evolve_grammar()
```

---

This framework provides a comprehensive foundation for integrating formal grammar theory with P-Systems membrane computing and relevance realization principles. The resulting system enables adaptive, context-sensitive computation that can dynamically adjust its processing based on relevance feedback and evolutionary grammar adaptation.

The implementation examples demonstrate practical applications in natural language processing, time series analysis, and adaptive learning scenarios, showing how the theoretical framework translates into working computational systems within the ReservoirCogs ecosystem.