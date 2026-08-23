# Aegis Architecture

## 1. System Overview

Aegis is an autonomous business operations and decision engine.

The system receives information from multiple business systems,
normalizes the information, detects meaningful events, investigates
those events using specialized AI agents, evaluates possible actions,
and either executes safe actions or requests human approval.

## 2. Major Components

### Sources

External systems providing information.

Examples:

- Email
- CRM
- Sales database
- Support tickets
- Spreadsheets
- GitHub
- Business APIs

### Ingestion Layer

Responsible for collecting and normalizing incoming information.

### Event Engine

Determines whether incoming information represents a meaningful
business event.

### Intelligence Layer

Contains specialized agents responsible for investigation and analysis.

Initial agents:

- Sales Analyst
- Support Analyst
- Finance Analyst
- Business Researcher
- Decision Planner
- Critic

### Decision Layer

Evaluates proposed actions.

Actions are classified into:

- Informational
- Low-risk autonomous
- Human approval required
- Prohibited

### Execution Layer

Executes approved actions through connected tools and APIs.

### Memory Layer

Stores:

- Events
- Decisions
- Actions
- Results
- Agent reasoning summaries
- Feedback
- Business state

### Evaluation Layer

Measures:

- Accuracy
- Decision quality
- Action success
- False positives
- False negatives
- Human overrides

## 3. Feedback Loop

Every executed action should eventually produce an outcome.

```text
Event
 ↓
Investigation
 ↓
Decision
 ↓
Action
 ↓
Outcome
 ↓
Evaluation
 ↓
Memory
 ↓
Future decisions

# Aegis Event Architecture

## Purpose

The Aegis Event is the canonical representation of something that
happens inside or around a business system and may require monitoring,
investigation, decision making, or action.

## Event Flow

```text
External System
      ↓
Source Adapter
      ↓
Event Normalization
      ↓
Aegis Event
      ↓
Event Router
      ↓
Investigation

# Aegis Investigation Architecture

## Purpose

An investigation is a structured process used by Aegis to determine
the likely causes of an important business event.

## Investigation Lifecycle

```text
Event
 ↓
Investigation Created
 ↓
Evidence Collection
 ↓
Evidence Analysis
 ↓
Hypothesis Generation
 ↓
Hypothesis Verification
 ↓
Conclusion
 ↓
Confidence
 ↓
Decision


the number of AI agents has been increased,
1. sales analyst
2. critic 
2. re analyst

AUTHORITATIVE AEGIS CONTEXT:

{{ JSON.stringify($json.aegis_context) }}

REANALYSIS INSTRUCTION:

{{ $json.reanalysis_instruction }}

Revise the previous analysis using the critic's feedback while preserving all authoritative evidence and deterministic calculations.


the agenst have been under preforming