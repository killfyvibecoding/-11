# Standard asset set

Use this as a slot menu, not a mandatory fixed count. Select the smallest set that satisfies the user's platform and purpose.

| Slot | Purpose | Typical source | Release rule |
|---|---|---|---|
| `white-bg` | Main listing image | Front product photo | No text or decorative props; follow the platform's current main-image rule |
| `hero-45` | Secondary hero / 45-degree view | Front or verified multi-view | Do not rotate into an unknown surface |
| `key-features` | 2–4 verified selling points | Front plus fact card | Use real product details; icons must not replace evidence |
| `selling-point` | One benefit explained clearly | Product detail photo plus verified claim | One primary claim only |
| `material-detail` | Texture, finish, construction, or ingredient view | Detail/back photo or visible trait | Do not infer material composition or percentages |
| `lifestyle` | Product in a believable use scene | Product photo plus approved scene | The product remains the sharpest subject and the action must be plausible |
| `model-or-usage` | Wear/use demonstration | Product photo plus model or usage brief | Conditional for apparel, accessories, beauty, tools, and appliances |
| `multi-scene` | Several approved contexts in one asset | Same identity lock and approved scenes | Keep the product large enough to inspect |
| `three-angle` | Front/side/back or multi-view sheet | Verified multi-view photos | If inferred from one view, label `concept` and do not use for technical proof |
| `package-spec` | Packaging, contents, or parameters | Package/label/spec source | Every field needs a `user` or readable-label source |
| `detail-page` | Reference-driven page module | Product identity plus style reference | Generate per module; use the reference to match visual language only |

## Default standard sequence

For “完整套图” without a platform-specific count, propose:

1. `white-bg`
2. `hero-45`
3. `key-features`
4. `material-detail`
5. `lifestyle`
6. `model-or-usage` when relevant
7. `multi-scene`
8. `package-spec` when verified information exists
9. `three-angle` as publishable only when the angles are evidenced

For a reference-driven detail page, count visible screens/modules in the user's reference and use that count. Preserve a hero opening and a verified information/package closeout when the page has enough modules. Use the target platform's current official dimensions and image policies; if they are unavailable or uncertain, record `platform_rule_pending` instead of guessing.

## Prompt block template

```text
PRODUCT IDENTITY LOCK: [stable description from the identity card]
ALLOWED FACTS AND COPY SOURCE: [user / visible facts only; pending fields omitted]
VISUAL DNA: [reference-derived color, light, composition, type mood; no target-product details]
SLOT: [purpose, camera, scene, layout, product scale, safe text area]
EXACT COPY: [only if sourced; otherwise leave a clean text area]
NEGATIVE: do not change SKU, color, silhouette, proportions, structure, logo, label, or verified text; no invented parts, claims, specs, certificates, watermark, or competitor comparison
OUTPUT: [platform, ratio, format, required background, file-size constraints]
```
