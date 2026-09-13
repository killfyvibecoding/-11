# Reference detail-page mode

Use this mode only when the user provides a product identity source, the product facts/copy that may be published, and a complete detail-page or style reference. A missing reference does not block the standard asset set; it makes the detail-page branch `pending` with the smallest missing input listed.

## Plan before rendering

1. Count visible screens or semantic modules in the reference. The priority is the user's explicit count, then visible reference count, then a clearly stated 8–12 page proposal. Record the count basis.
2. Reverse-engineer visual DNA only: palette, background material, light direction, composition, whitespace, typography mood, information density, and module rhythm. Keep the user's product identity and facts in a separate card.
3. Produce pages 1 through N. Each page has one communication job, page purpose, sourced copy, layout, product/reference roles, page-specific prompt, copy-overlay notes, and release status. Keep a hero opening and a verified information/package closeout when the count allows it.
4. Extract each page prompt before rendering. Every extracted prompt contains the page prompt, unified style prompt, unified negative prompt, exact copy source, output ratio, and final input combination.
5. Render one page per call using the extracted prompt plus the product identity source. Use the reference for analysis and style extraction, not as a target-product image input in the final call. Keep the default vertical ratio only when the target platform's current rule supports it; otherwise record the required ratio or `platform_rule_pending`.

## Page plan fields

```text
page_id / page_name:
primary_job:
visual_content:
layout_and_safe_zones:
exact_copy:
copy_provenance:
product_reference_role:
style_reference_role:
page_prompt:
overlay_notes:
status:
```

## Local preset compatibility

If the user's existing `ecommerce-detail-page-workflow` preset is available, preserve its explicit page order, ratios, exact-copy requirements, and information-page closeout when the user asks for that preset. In a standalone import where its reference assets are unavailable, ask for a new reference or use the visible reference count; never recreate missing template details from memory and never mark the resulting pages `publishable` without a platform and copy check.
