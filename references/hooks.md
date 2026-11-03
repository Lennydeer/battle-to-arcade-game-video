# Hooks

The agent performs these checks at the matching stage. They do not install background tasks, shell hooks, or automatic Codex handlers. Use `scripts/check_timeline.py` for data checks under the format below. Visual checks remain separate.

## Production hooks

| Hook / when | Check and output | If there is a problem |
|---|---|---|
| `story_ready` — before planning the action | Confirm participants, limits, and sources. Each step has an action, response, and result. The outcome and states match the source. Save the script and open gaps. | Correct the order. Do not show unverified details as checked facts. Ask only about a critical open choice. |
| `assets_ready` — before generating or adding poses | Set each fighter's reference, colors, clothing cut, face, proportions, scale, sides, and contact points. After generation, check transparency, edges, nearby cells in the sprite sheet, and ALL poses, including non-attack poses. | Fix or regenerate the affected asset. Random resizing cannot fix different anatomy. |
| `motion_ready` — before expanding the test | Check preparation, contact, reaction, and return for both fighters. Speed is clear; the smear does not hide contact; feet meet the floor; new drawings keep the design. Review at normal speed and frame by frame. | Fix drawings, paths, timing, or phases. Do not automatically increase the frame rate. |
| `scene_exit` — at every transition | The outgoing state matches the next event's incoming state: pose, support, ability to act, resources, injuries, clothing, power-ups, sides, props, and damage to the arena. Notices have their own time intervals. | Fix state resets or sudden recovery before the full build. |
| `scale_locked` — after adding each sheet and before export | Compare ALL used poses of both fighters with their references: head, shoulders, torso, limbs, and support. Check walking, grabbing, and the ending separately. Save a contact sheet at one scale and transition frames in the QA report. | Fix the model or scale. Do not fit it to the full image rectangle when an arm or leg is raised. |
| `anatomy_locked` — after injury, transformation, or healing | Keep the body's left and right sides correct, whatever its screen position. The same hand stays missing in every pose until explicit healing. Clothing does not repair itself after healing. Helpers do not change sides without moving. | Correct every affected pose, not only the reported frame. |
| `defeat_settled` — after the outcome and at the ending | The actual result, agreed final pose, support, and ability to act match. A lying or seated character does not stand up without recovery. HP does not determine death. Check both fighters, all later poses, and the last frame. | Fix conflicts with the script. A seated ending explicitly chosen by the user is not an error by itself. |
| `audio_ready` — before export with sound | Confirm the exact file, start positions in the source and video, trim, fades, and SFX at contact frames. Check the mix and export for clipping, then listen if possible. | Do not change the chosen track or start position. Record technical checks and actual listening separately. |
| `before_export` — before rendering | Check 3–2–1, English HUD, technique-only captions, 3-second notices, agreed sound, and contact/FX/HP/SFX timing. Check each new pose type, extreme positions, location changes, start, and ending. Complete `scale_locked`, `anatomy_locked`, `defeat_settled`, and, when sound is used, `audio_ready`. The final render uses Remotion and the composition check has no errors. | Fix confirmed errors. Review warnings by meaning; do not ignore them as a group. |
| `after_export` — before delivery | Check actual size, fps, duration, codecs, full decoding, audio, playback, sample frames, readability, and sync. Save a QA report listing completed and missing checks. | Do not claim the file is verified. Fix the problem or state the specific limit. |
| `feedback_received` — after a comment | Separate general rules from local changes. Update design guidelines and feedback. Check similar moments for BOTH fighters, then build a new version within the authorized scope. | Remove conflicts from active rules. Keep the history and earlier release. |

## Viewer hooks

Do not add text clickbait, a flash-forward, an invented hit, or a new order of story events. Keep the countdown and chronology.

- **Opening:** show clear stances, distance, and the first real threat just after the countdown. Do not spend time explaining the backstory.
- **A question through action:** show preparation for a dangerous technique and the opponent's possible response. The viewer should understand what the fighters are trying to do without extra text.
- **Change of advantage:** highlight a real counter with a change in distance, pose, pace, or arena conditions. Do not promise a turn that does not happen.
- **Cause → result:** show clear contact, reaction, sound, and state change. Do not cover the key moment with a smear.
- **Rising intensity:** a new technique, power-up, or domain changes visible behavior, not just the caption.
- **Ending:** show the actual outcome and character states. The final pose matches the agreed result. Do not invent a death, victory card, or extra ending.

## Timeline data check

This data format is optional for a project. If used, run the check at `scene_exit` and `before_export`:

`python3 <skill>/scripts/check_timeline.py <project>/timeline-review.json`

JSON fields:

- `fps`, `duration_frames`, `intro_frames` (3×fps), and `language` (`en`).
- `initial`: an object `{fighter_id: {hp, energy, costume, ...}}`. Initial resource numbers must be at least zero; extra fields are flexible.
- `events`: ordered `{id, frame, before, after, technique?, caption?}` objects. `before` and `after` are full state snapshots for all participants, not only changed values. An event's `after` must match the next event's `before`. An empty `caption` is allowed; a nonempty caption must equal `technique`. All actions start after the intro.
- `notifications`: `{event_id, start, end}`, using frame numbers for the full video. `start` equals the event frame; `end = start + 3×fps`. If the interval goes beyond the end of the video, the script reports an error. Extend the final hold or adjust timing; do not hide the problem.

Example state: `{"yuji":{"hp":740,"energy":82,"costume":"intact","injury":"left-arm"}}`.

The script cannot check story accuracy, gaze direction, anatomy, image content, natural movement, or audio quality. `defeat_settled` is a separate visual check, not automatic pose recognition. A successful exit code does not replace visual review.
