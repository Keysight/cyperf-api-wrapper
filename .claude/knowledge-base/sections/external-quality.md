<!-- generated: knowledge-base v3.5.0 | section:external-quality -->
## External Quality Summary

EQ evaluation not yet performed. Run `/knowledge-base:discover-all` for full evaluation.

### Surface changes observed since last KB refresh (pre-EQ, from git history 2026-07-14 → 2026-07-29)
- **Breaking**: `SessionsApi.start_session_prepare_test` (plus its `_with_http_info`/`_without_preload_content` variants) and the `PrepareTestOperation`/`PreparedTestOptions` models it used were removed entirely (PR #81, Jul 27 2026 regen).
- **Breaking**: `UtilsApi.get_eula`/`post_eula` gained a new required positional `id` parameter; the resource path changed from the hardcoded `/eula/v1/eula/CyPerf` to `/eula/v1/eula/{id}` (PR #81). The wrapper's own `wait_for_controller_up()` was not updated to match, so this is also an internal reliability bug — see `sections/technical-debt.md` (TD-1).
- **Non-breaking / additive**: `DataMigrationApi.start_controller_migration_import` gained an optional `file` upload parameter (multipart form); `ApplicationResourcesApi.delete_resources_capture` now documents `401`/`403`/`404` `ErrorResponse` returns in addition to `500`; several `ApplicationResourcesApi` docstrings had the word "CyPerf" genericized (e.g. "Get a particular CyPerf application" → "Get a particular application") — cosmetic only.
- **Behavioral change (hand-written helper API, not generated)**: `utils.TestRunner.set_prisma_airs_params`/`set_model_armor_params` both gained an optional `hostname=` keyword argument and now raise `ValueError` when no matching guardrail strike or application is found at all (previously only printed and returned) — PR #80, Jul 29 2026, ISGAPPSEC2-38154.
