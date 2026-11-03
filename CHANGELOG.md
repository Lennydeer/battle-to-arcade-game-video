# Change log

## 2026-11-03 — English edition

- Translated all documentation, templates, reference guides, and skill metadata into clear Intermediate-level English.
- Kept technical names and explained key terms in simple language.
- Kept the agreed production rules, file paths, hook IDs, and timeline checker behavior.
- Updated the installed skill, working copy, and downloadable package to match this edition.

## 2026-11-03 — Battle to Arcade Game Video

- Renamed the skill from `battle-to-fighting-video` to `battle-to-arcade-game-video`: folder, name field, display name, and example prompt.
- Added a README with installation and usage steps, a separate creative treatment, and a GitHub package.
- Made the product scope clear: the skill creates arcade fighting videos, not a playable game or a ready-made universal engine.
- The rename keeps the approved visual style and does not change earlier videos.

## 2026-11-03 — Rules updated from production feedback

- Compare size and body volume using the head, shoulders, torso, and limbs in every pose, including walking, grabbing, and the ending.
- Keep injuries on the correct side of the body until healing. Clothes do not repair themselves after healing.
- Avoid mirroring by default. Helpers and fighters change sides through clear movement.
- Show domains in the current side view at the same scale. Effect direction and cuts must match the action.
- Replaced the rule that every defeated fighter must lie down. Follow the actual outcome and agreed ending, including an explicitly chosen seated pose.
- Separate encounters can share a video when the user asks, with a clear cause-and-effect link.
- Record where music starts in the source and video. Sync SFX to frames. Keep checks after encoding separate from listening.
- Added `scale_locked`, `anatomy_locked`, and `audio_ready`. Updated `defeat_settled` and `before_export`.
- Expanded the script template. Moved choices for specific JJK battles into a separate guide.
- Kept Remotion for the final render, the 3–2–1 countdown, English HUD, technique names, three-second notices, and expressive smears.
