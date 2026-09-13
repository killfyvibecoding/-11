# Flowith reference profile: 04bb8569

Source: [Flowith shared canvas](https://flowith.io/view/04bb8569-9b45-4eec-a76e-fcf304c7213a)

`template_id`: `flowith:04bb8569-9b45-4eec-a76e-fcf304c7213a`

The shared canvas exposes seven primary image-generation prompt modules, followed by a separate 4:5 before/after workflow poster. The module order is:

1. hero product poster
2. lifestyle or usage scene
3. four-scene lifestyle collage
4. material or surface macro detail
5. selling-point demonstration
6. colors, size, and styling information graphic
7. care, usage, or trust closeout

## Reusable visual DNA

- 9:16 vertical canvas for the primary modules; generous negative space
- warm ivory, cream, oat, and soft beige palette with clean low-texture gradients
- soft natural or studio daylight, low contrast, no hard shadow, calm premium mood
- restrained bilingual typography, usually a large serif title plus smaller sans-serif support copy
- small brand mark in the upper-left when an authorized logo exists
- pill-shaped CTA in the lower-right when a CTA is actually needed
- glassmorphism information card only when it improves hierarchy; keep it quiet and sparse
- one communication job per image, with a visible product identity lock and a short negative prompt

## Prompt schema to preserve

Use the canvas's field order as a template, then replace its product-specific content:

```text
project_settings
brand_module
scene_style or canvas_style
model or model_consistency (only when a person is needed)
product identity and consistency rule
scene_goal or product_detail (for a selling-point module)
typography_layout / layout
negative_prompt
final_prompt_cn or prompt_payload
```

For a product such as the user's suction phone stand, map the sequence as follows:

| Flowith module | Phone-stand adaptation | Fact gate |
|---|---|---|
| Hero | Clean product hero on a warm neutral studio set | Preserve the photographed black body, round base, hinge, and visible red accent; do not invent unseen sides |
| Lifestyle | Stand supporting a phone on a smooth, flat surface | “Smooth, flat surface” and “phone support” come from the user; any specific surface or environment remains a scene choice, not a performance claim |
| Four-scene collage | Desk, glass/mirror, tile, and another visibly smooth plane, each showing the same SKU | Show context only; do not imply tested load, durability, or universal adhesion |
| Macro detail | Suction base, hinge, release/lock detail, and surface contact | Only describe details visible in the supplied photos; unseen mechanism remains `pending` |
| Selling point | Phone-support posture, placement, and viewing context | “Stable”, angle range, load capacity, magnetic force, or one-hand operation require user evidence |
| Information graphic | Compatible-surface guidance and use flow | Do not invent dimensions, materials, compatibility lists, or numerical specifications |
| Trust closeout | Cleaning, placement, and usage reminders | Use only user-supplied instructions; otherwise leave copy `pending` |

The 4:5 before/after poster can be used as a separate promotional asset about the generation workflow. It must not be treated as a product detail page and must not copy Flowith's name, interface, logo, or claims into a product listing unless the user owns and authorizes those assets.

## Identity and copy rules

The source canvas contains apparel-specific examples, a third-party brand name, model details, and unverified fabric or care claims. Treat those as `rejected-reference`. Carry over their layout logic and visual DNA only. Replace every product, brand, model, claim, and CTA with the user's sourced content or an original editable overlay. Preserve the standard asset-set default and record this source URL and mapping in the manifest before rendering.
