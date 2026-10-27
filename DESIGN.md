# Profile maintenance

The visual identity uses ink, cyan, violet, and a small copper accent. All artwork is local, hand-authored SVG: no remote badges, tracking pixels, font requests, scripts, or statistics services. No scheduled workflow is needed.

## Assets

- `hero-dark.svg` and `hero-light.svg`: desktop, 960 × 380.
- `hero-mobile-dark.svg` and `hero-mobile-light.svg`: mobile, 480 × 420.
- `signal.svg`: decorative separator.

The README uses GitHub-supported `<picture>` sources for light/dark and narrow layouts. The fallback is the light desktop image. Core content is ordinary Markdown so it remains selectable, accessible, and readable without images. SVG has a complete static composition when animation is unavailable. CSS animation stops for `prefers-reduced-motion: reduce`; there are no flashing effects or continuously moving text.

Keep SVGs free of JavaScript, external references, embedded HTML, and raster images. Preserve viewBox scaling and the README's descriptive hero alt text. Source order matters: narrow dark, narrow light, desktop dark, fallback light.

## Content

Profile information was checked against the supplied CV, the public LinkedIn profile, and the linked public repositories. The CV itself, its telephone number, email, and local file path are intentionally not committed. Private repositories are not featured. Graduation dates were omitted because the CV and indexed LinkedIn education dates differ. Training-path completion is not presented as exam certification. Mobile repositories are described as development/learning work without claims of commercial adoption or exclusive original authorship.

Review employment dates when roles change. Confirm new achievements before adding them. Update project descriptions from the actual source rather than repository names alone. Avoid automatic statistics that can misrepresent private contributions or depend on unreliable external renderers.
