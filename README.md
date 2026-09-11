# AdaCipher

Research code for studying cipher-based jailbreaks of LLMs and for **AdaCipher** — an
automated, black-box pipeline that adaptively discovers new
transformations for jailbreaking a given target model (with or without external
input and output guardrails).

The pipeline searches for a cipher over a fixed number of trials: a *Strategy Model*
proposes a transformation, a *Code Model* implements it as a Python class, the
implementation is verified for correctness, and then used to attack
the target model. Feedback from a *Process Judge* and a *Benign Evaluation*
step is aggregated and fed back into the next trial. 

## Repository layout

All code lives under `autojailbreak/`.

| Path | Contents |
|---|---|
| `main_launch.py` | Entry point — runs an experiment from a YAML config |
| `configs/` | Config parsing (`config_reader.py`) and experiment-config objects (`exp_config.py`) |
| `config_files/` | All experiment configs, see table below |
| `ciphers/` | Built-in static ciphers (Caesar, ROT13, Base64, QWERTY, word reversal, identity/no-op) and the base `Cipher` interface |
| `attacker/`, `strategist/`, `summariser/`, `denoiser/` | AdaCipher pipeline components — cipher-search / code-generation prompts, feedback summarisation, response denoising |
| `target/` | Target-model wrapper (plain model, or model + input/output guardrails) |
| `guardrail/` | Guardrail wrappers (e.g. Llama Guard) |
| `judges/` | Harm judge (HarmBench-style), process judge, benign judge |
| `models/` | Model backends (OpenRouter API models, local models, request/response logger) |
| `static_attacks/` | Natural-language jailbreaks combined with ciphers (Persona, DeepInception/roleplay) |
| `custom_datasets/` | Dataset loaders (HarmBench split, AlpacaEval) |
| `prompts/` | All prompt templates and few-shot examples used by the pipeline components |
| `experiments/` | `Trainer` (AdaCipher search loop), `Tester` (static/held-out evaluation), `BenignTester`, experiment logger |
| `utils/` | Plotting/aggregation scripts, cipher-family diversity analysis, train/val/test misalignment analysis, best-cipher selection |
| `logs_final*/`, `figures/` | Experiment outputs (raw logs, per-trial configs, generated plots) |

## Setup

```bash
conda env create -f environment.yml
conda activate llm
export OPENROUTER_KEY=<your-openrouter-api-key>
```

Reproducing API-based experiments requires access to the corresponding models through OpenRouter and may incur API costs.

Model calls go through the [OpenRouter](https://openrouter.ai) API (`model_type: openrouter`
in configs); a local guardrail/model backend is also supported (`local_llamaguard`, etc.,
run on-device rather than via the API).

## Running an experiment

```bash
cd autojailbreak
python main_launch.py --config config_files/<some_config>.yaml
```

A config's `GeneralFields` block defines the experiment; an optional `Substitutions`
block sweeps one or more fields (e.g. `target_model_name`) across several runs, so a
single YAML file can launch the same experiment for every target model.

`exp_type` in the config selects the run mode in `main_launch.py`:
- `static` — evaluate one fixed cipher on the test set (no search)
- `static_benign` — same, but scored by the benign judge (capability probes)
- `dynamic` — the full AdaCipher search loop (train → validation → test)
- `basic` / `categories` — other train-and-test variants of the search

## Config catalog — what to run for which experiment

| Experiment (thesis section) | Configs |
|---|---|
| Static-cipher ASR / benign-capability probes (PP/CP/PC/CC settings, §3.1, §5.1) | `config_files/static_*.yaml` (no guardrails) and `config_files/benign/*.yaml` (per-cipher, per-setting benign quality) |
| AdaCipher adaptive search (§3.2, §5.2), one file per target model, `_guards` suffix = with input+output guardrails | `config_files/dynamic_*.yaml` |
| Combinations with natural-language jailbreaks — Persona / DeepInception(roleplay), with/without guardrails, ID vs. discovered cipher (§3.3, §5.3) | `config_files/attack_combinations/static_{persona,roleplay}_*.yaml` |
| Cross-model cipher transferability (§6.3) | `config_files/transferability/static_{model}_others.yaml` |

Guardrail on/off is controlled per-config via `use_input_guard` / `use_output_guard`
and `guard_type` in `GeneralFields`; most experiment types are provided as matched
`_no_guards` / `_with_guards` config pairs.

## Outputs and analysis

Each run writes to `log_path` (e.g. `logs_final/`, `logs_final_benign/`,
`logs_final_transferability/`), organised by experiment name, target model, and run
number — including per-trial cipher code, request/response logs, and a
`trial_summary.txt`. Aggregated plots are written to `figures/`.

Post-hoc analysis (plots, cipher-family diversity classification, train/val/test
category-distribution checks, best-cipher selection) lives in `utils/`, including a
few Jupyter notebooks (`plot_asr_over_trials.ipynb`, `recompute_reject_stats.ipynb`,
`experiments/experiment_summary.ipynb`).
