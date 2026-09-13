# QA and recovery contract

## Manifest fields

Keep one manifest for the job. If the filesystem is available, save it as `ecommerce-visual-manifest.json`; otherwise show the same fields in the response.

```json
{
  "job_id": "sku-slug-YYYYMMDD-HHMM",
  "identity_source": ["/absolute/product-front.jpg"],
  "fact_sources": {"color": "visible", "net_weight": "pending"},
  "platform_rule_status": "verified | platform_rule_pending",
  "assets": [
    {
      "asset_id": "sku-slug-white-bg-v001",
      "slot": "white-bg",
      "status": "planned",
      "references": ["product-front.jpg"],
      "copy_provenance": {"kind": "none", "refs": [], "overlay": null, "note": null},
      "platform": "pending",
      "platform_rule_status": "platform_rule_pending",
      "ratio": "pending",
      "version": 1,
      "retry_count": 0,
      "output": null,
      "failure": null
    }
  ]
}
```

Use stable IDs across retries. A retry updates the same asset record and increments `retry_count`; it does not create a duplicate slot. Completed outputs are immutable unless the user explicitly asks for a new version.

## Status rules

- `planned`: internal pre-render manifest state; never present it as a completed deliverable.
- `publishable`: identity, facts, text, platform constraints, and visual QA pass.
- `needs_review`: a human must check text, a generated scene, or a borderline visual detail; this includes a text check that fails when an output still exists.
- `concept`: a creative or inferred view that is not evidence of an unseen product surface or claim.
- `pending`: a required input, platform rule, or renderer is missing.
- `failed`: the slot exhausted its retry allowance or the provider returned a non-retryable error.

When more than one condition applies, use this precedence: `pending` for missing prerequisites, `concept` for explicitly unverified hidden or effect content, `needs_review` for a human-checkable output, `failed` for no usable output after retries, and `publishable` only when every gate passes. `planned` is only an internal pre-render state.

Every `copy_provenance` object uses `kind`, `refs`, `overlay`, and optional `note`. `kind` may be `user`, `visible-label`, `original-overlay`, `assistant-simulation`, `rejected-reference`, or `none`. `original-overlay` may contain only original, non-factual framing copy; factual copy must point to a user or readable-label reference. `assistant-simulation` is allowed only when the user requests a concept mockup and must carry the visible label `示例参数 / 待核实`; it can never pass the `publishable` gate. A rejected third-party logo or copy request must retain its reference and reason in `note`.

## QA checklist

Check each asset against the same identity card:

- silhouette, proportions, color, material/texture, logo/label, packaging text, and distinctive details;
- no added parts, altered interfaces, invented contents, hidden surfaces, or misleading use actions;
- every headline, label, parameter, ingredient, warning, and claim has a source; simulated values are visibly labeled `示例参数 / 待核实`;
- third-party reference logo, packaging, claims, reviews, and wording are absent; any refusal and original replacement copy are recorded in `copy_provenance`; an unconfirmed user-provided logo is not used;
- Chinese text is exact, legible, and not distorted; long text is editable when possible;
- product is the visual subject and is not obscured by a person, prop, or decoration;
- ratio, dimensions, format, file size, background, and text policy match the current platform requirement.

## Recovery rules

1. On timeout or a transient 5xx: query the existing asset ID/result first, then retry once with the same idempotency key.
2. On a visual mismatch: keep the failed image, record the mismatch, tighten the identity block, and rerender only that slot.
3. On a text or fact mismatch: do not rerender the whole image set; correct the copy/overlay or mark the slot `needs_review`.
4. On a missing provider key or unavailable renderer: stop rendering, report the exact missing prerequisite, and preserve the plan and manifest.
5. If the user explicitly requests a full new run, preserve the old manifest and outputs, create a new job/version, and give the new run explicit versioned IDs such as `sku-white-bg-v002`; retries within that run keep the new ID. Keep slot-level retry limits and never overwrite the previous version.
6. At delivery, list successful, review, concept, pending, and failed assets separately. Never hide partial completion.
