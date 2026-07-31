<!-- generated: knowledge-base v3.5.0 | section:technical-debt -->
## Technical Debt Registry

Full registry requires IQ evaluation. One item below was surfaced during an incremental git-history review (not from a formal IQ pass) and is tracked here because it is a confirmed, evidenced bug.

| ID | Title | Severity | Evidence | Status |
|----|-------|----------|----------|--------|
| TD-1 | `wait_for_controller_up()` EULA-accept path breaks after the PR #81 `UtilsApi` regen | Blocking (confirmed library bug) | `cyperf/api_client.py` lines ~166/172 call `eula_checker.get_eula()` / `eula_checker.post_eula(EulaSummary(accepted=True))` with no `id` argument; PR #81 (Jul 27 2026 "Regenerate Cyperf Python Wrapper") changed `UtilsApi.get_eula`/`post_eula` to require a positional `id` (path changed from the hardcoded `/eula/v1/eula/CyPerf` to `/eula/v1/eula/{id}`) | Open — introduced 2026-07-27, not yet fixed as of 2026-07-31 |

Open question for a human: what `id` should the wrapper now pass here (a literal `"CyPerf"`? one obtained from `list_eulas`?) — not inferable from the diff alone, so no fix was guessed.
