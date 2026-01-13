# Agentic Health Analytics (Local LLM Demo)

This repository is a **learning-focused, end-to-end demo** of building an AI agent pipeline using a **local, open-source large language model (LLM)**.

The project simulates how patient health data could be ingested, analysed over time, and summarised by an LLM-powered agent — **without using any paid APIs**.

---

## What this project demonstrates

- Running a **local LLM** using Ollama (no API keys required)
- Generating **synthetic patient health time-series data**
- Processing patient data through a **Python-based agent pipeline**
- Producing **structured, machine-readable summaries** (JSON / CSV)
- Designing systems that are **evaluation- and product-ready**, not just chatbots

This project intentionally focuses on **system design and reasoning**, not model fine-tuning.

---

## High-level workflow

1. **Synthetic data generation**
   - Create a CSV of patient health metrics (e.g. weight, blood pressure, activity)
   - Multiple time points per patient (weekly check-ins)

2. **Agent-style analysis**
   - Group patient records over time
   - Compute numerical trends (deltas, averages, extremes)
   - Pass structured summaries to a local LLM

3. **LLM output**
   - Risk level (low / medium / high)
   - Key findings grounded in numbers
   - Safe, non-diagnostic next-step suggestions
   - Clinician review flag (boolean)

4. **Outputs**
   - One JSON record per patient
   - CSV summary for inspection and downstream analysis

---

## Tech stack

- **Python 3.12**
- **Ollama** (local LLM runtime)
- **Llama 3.2 (3B)** open-weight model
- pandas / numpy (data handling)
- requests (LLM communication)

The LLM interface is intentionally abstracted so it can be swapped for hosted models later.

---

## Repository structure

