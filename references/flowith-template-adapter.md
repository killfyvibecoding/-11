# Flowith template adapter

Use this reference when a user provides a Flowith share page as a template for product visuals. The Flowith page is a source of visual and prompt structure; the user's product photos, verified facts, and explicit copy remain the source of truth.

## What to extract

Capture only content that is visibly available from the shared page:

- `template_id`, source URL, access state, and extraction timestamp
- page or node order and the communication job of each module
- palette, background, material, light direction, lens or camera feel, framing, whitespace, typography mood, and information density
- prompt blocks, exact copy fields, safe zones, negative constraints, output ratios, and any platform notes

Keep this extraction separate from the product identity card. A template may describe a phone, color, brand, package, claim, review, or specification that belongs to its original project; those details are `rejected-reference` unless the user independently supplies and authorizes them.

## Access and fallback

1. Open the supplied share URL and inspect the visible canvas or exported prompt blocks.
2. If the page is an app shell, login gate, empty state, or inaccessible dynamic canvas, set `access_state: inaccessible`, preserve the URL, and list the smallest missing input: pasted/exported prompt text or screenshots of the needed nodes.
3. Do not infer hidden node text or silently substitute a remembered Flowith template.
4. If only part of the canvas is visible, extract only that part and mark the missing modules `pending`.

## Mapping to this skill

For a standard asset set, apply the extracted visual DNA to each selected slot while retaining the same identity lock and fact gate. For a detail-page mode, map one visible Flowith module to one page with one primary communication job. Compose each final prompt in this order:

```text
product identity lock
allowed facts and copy provenance
Flowith-derived visual DNA and module logic
slot/page camera, scene, layout, and safe zones
exact copy or editable-overlay notes
negative constraints
ratio and platform requirements
```

Record the following in the manifest before rendering:

```json
{
  "template_id": "flowith:<share-id>",
  "template_source_url": "<url>",
  "template_access_state": "extracted|partial|inaccessible",
  "template_summary": "<visual DNA and module mapping>",
  "template_copy_provenance": "rejected-reference|original-overlay|user|visible-label"
}
```

The Flowith page itself is never passed as a target-product image input. Do not copy its logo, packaging, claims, testimonials, or wording; use an owned logo and sourced facts or an original editable overlay instead.
