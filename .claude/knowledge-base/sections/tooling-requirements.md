<!-- generated: knowledge-base v3.5.0 | section:tooling-requirements -->
## Tooling Requirements

### Understand Skills (always generated)
- `explain` — navigate the generated-vs-hand-written split; explain what a given `*Api` operation or model actually does against the CyPerf controller.
- `document` — keep `README.md`/`docs/*.md` in sync is generator-owned; human-facing docs work should target `samples/*.py` and this KB instead.

### Operate Skills (always generated)
- `review` — code review, scoped to the small hand-written surface (`utils.py`, `dynamic_model_meta.py`, `samples/`, CI/build files); generated files should be excluded from review by default.
- `exec-plan` — flag the test-framework gap (scenario-zero) on first use per the Testing table above.
- No `deploy` skill — this project has no deployment target beyond a PyPI publish, already automated by Jenkins.

### Improve Skills (gap-driven)
Requires IQ/EQ evaluation to identify gaps.
