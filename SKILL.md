---
name: battle-to-arcade-game-video
description: "Research fictional battles and create animated 2D fighting videos with clear techniques, consistent characters, HP and resources, strong motion smears, and sound. Use for a new battle video or changes to an existing one. A simple lore question does not require video production."
---

# Battle to Arcade Game Video

Create a clear battle sequence in the style of a 2D fighting game. The viewer should see the action, the response, and the result. The approved style reference is Yuji–Choso Hyperframes v02. Use its presentation rules, not its specific techniques, numbers, or costumes.

## Getting started

- Read the current script, character references, design guidelines, feedback, and latest approved version. The user's latest correction replaces an older rule that conflicts with it. Keep one clear set of active rules.
- Continue from the requested stage. A text change does not mean a new render. Do not repeat an approved test. Approval of a video does not confirm that every detail matches the original story.
- **Use Remotion for the final render, not Hyperframes.** Keep the approved approach to artwork, poses, smears, and the script. Earlier Hyperframes versions are visual references, not a required engine. This style does not require the lore-to-video-remotion skill.
- Use AskQuestions or an available interactive choice tool only for creative decisions that are still open: the battle and its limits, a major new concept, or sound. Explain the context, recommend an option, and explain its effect. Do not ask again about agreed choices or routine technical decisions.
- Keep project files and media outside the skill folder. Do not change global settings or other skills for a new project.

## Script and accuracy

Complete the [battle template](references/battle-template.md) before planning the action. For JJK, read the [agreed scope](references/jjk.md).

- Start with an actual action from the fight. Avoid long backstory, flashbacks, and an unnecessary ending after the fight. Name the participants and the start and end of each battle. A connected fight can stay one story when the participants change. Keep separate meetings and rematches clear in the chronology. Combine them in one video only when the user asks; keep the cause-and-effect link and leave out unrelated parallel fights.
- Write each step as **who → exact technique or movement → response → hit, block, or miss → result → new state**. Name summoned creatures, weapons, and limits. “Overpowers the opponent” is not a script.
- Keep sources, exact chapters and pages when available, explanations, and unverified details in Markdown. Separate facts from the original work, additions in an adaptation, interpretation, and choices made for the video. Do not present a secondary summary as a page-by-page check.
- Do not invent successful attacks, deaths, techniques, or advantages to make the fight more exciting. Mark added linking movements and shorter timing as choices made for the video.

## Visual rules

- Use 1920×1080, 16:9, 30 fps. Keep the side-view arena, fighters, effects, and HUD (the game-style information display) on separate layers. Use fast, continuous action. Aim for 60–90 seconds for a battle of similar complexity. Split a complex fight into parts instead of losing key events. A short test is usually 7–13 seconds; do not stretch a simple exchange.
- Begin with a still scene and **3 → 2 → 1**, one second per number. Then remove the countdown. Do not show an exchange number or a timer for the video length.
- All on-screen text is **in English**. Show the name, numerical HP, and resource at the top; for JJK, use CURSED ENERGY. Below each fighter's resource bar, show their injury and received damage notices for **exactly 3 seconds** each. The text disappears; the injury and HP loss remain.
- The bottom panel shows **only the name of the technique in use**. Do not label ordinary punches, running, or moving closer. Do not add location names, sources, internal IDs, an explanation of the HP model, or final explanation cards unless requested.
- The numbers are a game model explained in the documentation, not an official measure of power. Resources change because of events. Zero HP does not automatically mean death. Add another meter only when a mechanic needs it. Keep an ability's story timer separate from screen time.

## Characters, arena, and animation

- **The first approved frames define each character's model.** Keep the same face, hair, proportions, limb lengths, head size, colors, outlines, clothing cut, shoes, and shadows in every pose. This applies to both fighters, including reactions and falls.
- Check body size against the first approved drawing: head size, shoulder and torso width, and limb lengths. Matching the image height alone does not prove that proportions match. Check walking, picking up an object, and holding the final pose as carefully as attacks.
- Do not set scale from the full image rectangle. A raised leg changes that rectangle, not the body size. Compare body landmarks. Store physical scale and contact points separately from image cropping.
- In a fighting stance, the face, gaze, and torso point toward the opponent. Check every pose and change of side. Do not mirror sprites or the scene by default; use poses drawn for the correct direction. Keep fighters, helpers, injuries, and props on the correct sides. Show movement when someone changes sides. A fall or an intentional turn is not a wrong fighting stance.
- Plant supporting feet on the floor, with shadows below them. Avoid accidental floating, rocking the whole image, or sliding a fixed stance across the ground. Use a leg and arm cycle for travel. Leaving the ground must follow an action such as a jump, throw, knockback, or an established levitation ability.
- For both fighters, build **preparation → acceleration → contact → reaction → return**. A smaller set of good drawings is acceptable. Smooth movement comes from connected phases, paths, and rhythm, not just frame count. Do not hide a poor transition with a long fade between silhouettes.
- Use strong **smears** for fast transitions: brief stretched drawings, arcs, or motion trails between clear poses. Set their length to fit the movement. Do not keep them through the whole strike, hide the target or contact, or change the character's normal face and costume. Effects and a brief pause on impact support body animation; they do not replace it.
- Clothing either stays intact throughout the fight, or every shown tear remains afterward. Injuries, power-ups, marks, weapons, water, and debris remain after a pose or camera change. Recovery needs a separate, justified event.
- **The ending follows the result and the agreed final pose.** If a character falls, show the loss of support, contact with the surface, and a stable final pose. A lying character does not return to a stance without recovery. An explicitly chosen seated ending is valid. A winner does not crouch or fall without a reason. Defeat, unconsciousness, and death are different states; confirm death from the source, not from zero HP. See [JJK](references/jjk.md) for local choices.
- **Pose, support, action, and HUD must show the same state.** Carry both fighters' body position, floor contact, ability to act, injuries, and clothing into the next frame. For a lying character, place support and shadow under the body. Do not hang a horizontal drawing from the old foot anchor. Check later pose changes and the final hold, not only the impact frame.
- Separate levitation from a flip. Leaving the floor does not require rotation. In the agreed Gojo scene, he floats upright facing Toji. Do not rotate a flat standing image just to add movement. If the action needs a flip, draw clear poses between its start and end. After moving a character, align the technique's starting point with the hand or weapon and check its path to the target.
- For a domain, keep the side-view camera, fighter scale, and floor line by default. Change the surroundings and effects around them. Use a separate wide shot only when agreed. The technique's starting point, direction, and result must match. Do not replace a vertical cut with a horizontal one.
- A technique must be **visible**, not just named. Props belong to the arena: a door is attached to a stall before it breaks; afterward, the opening, door panel, or debris remains.

## Production process and hooks

[Hooks](references/hooks.md) are required agent checkpoints and methods for keeping viewers interested. They are not automatically installed system handlers.

1. Sources → step-by-step script → states before and after each event. Complete `story_ready`.
2. Build the moodboard as **images and folders**. Separate characters, arenas, techniques, and a sample frame. Keep source material separate from generated artwork. Set the references and complete `assets_ready`.
3. For a new approach, build a short test with an action and a reaction from both fighters. Complete `motion_ready`. Apply the findings to the full pose set, not only the reported frame.
4. After approval or a request for the full video, apply the approach to the whole fight. Fit music to the video length. Keep impact sound, effects, and HP changes in sync. Ask about the track or silent mode only if no choice exists. Do not replace agreed sound.
5. Follow the [production rules](references/production.md), `before_export`, and `after_export`. Fix found problems, save a new version, and show a playable MP4.
6. On feedback, complete `feedback_received`: update the active rules first, then do the authorized work. Keep earlier videos and source files. Do not call pose-based animation a full rig (a joint-based animation system), or call technical audio analysis a listening review.
