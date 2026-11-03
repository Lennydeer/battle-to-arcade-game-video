# Creative treatment: Battle to Arcade Game Video

## Concept

Show how a battle happened through the visual language of a 2D arcade fighting game. Every action should be clear from the image: who attacked, which technique they used, how the opponent responded, and what changed after contact. The real course of the battle creates the drama. The game-style display helps the viewer follow its results.

This is a linear animated video. The viewer watches a planned sequence and does not control the characters. The arcade fighting style shapes the presentation, while the original work provides the logic of the fight.

## Story and accuracy

Start with an actual battle action after a short countdown. Do not spend a long opening section on backstory. Build the script as a chain: action → response → hit, block, or miss → result → new state. Show a specific action instead of simply saying that one character is stronger.

Name techniques, summoned creatures, and weapons clearly. Carry their results into later events. Defeat, death, unconsciousness, and a temporary inability to act are different states. Zero HP does not prove death by itself.

Keep source links, chapters, pages, and review status in the working script. Mark facts from the original work, additions in an adaptation, interpretation, and shortened action made for the video separately. Approval of the video does not mean that every story detail has been checked.

## Frame and space

The standard frame is 16:9, 1920×1080, at 30 frames per second. Fighters face each other in a side-view arena and stand on a clear surface. Build the background, characters, shadows, effects, and interface as separate layers.

Characters change position through visible movement. Do not mirror an image as a quick way to get another pose: this can switch an injury to the wrong side, change clothing, or move a helper. Use a suitable pose for the new direction.

By default, Domain Expansion changes the surroundings within the current frame. Keep character scale and the floor line stable. Use a separate wide shot only when agreed. The start of an attack, its path, and its mark on the target must match.

Props belong to the arena. A door has a specific opening, debris has a source, and an object is picked up in a visible place. Damage to the surroundings does not disappear without a reason.

## Characters and continuity

The first approved drawing of each fighter becomes the model reference. Keep the same face, hair, colors, clothing cut, shoes, head, shoulders, torso, and limb lengths in every pose. Check both fighters, including walking, reactions, falls, object grabs, and the final held pose.

Measure character size using body landmarks, not the outer rectangle of the image. A raised leg makes that rectangle larger, but must not make the head or torso smaller. Removing transparent margins must not change physical scale or contact with the ground.

Record injuries relative to the body: the left hand remains the left hand whatever the screen position. Store the body state, clothing, power-ups, and weapons separately. Healing can restore the body without repairing a sleeve. A change of control over a body does not count as healing by itself.

The final pose follows the actual outcome and the user's explicit choice. After a fall, show contact with the floor and a stable position. A defeated character who is lying or sitting does not return to a stance without a recovery event. A winner does not crouch to pick up an object when the agreed action is a standing grab.

## Animation

Each exchange has preparation, acceleration, contact, reaction, and return. Smoothness comes from connected phases, movement paths, and rhythm. A large number of drawings is not required. A limited set of poses with strong drawn transitions is acceptable.

Smears are brief stretched drawings, arcs, and trails during the fastest part of a movement. They connect clear poses and show speed and force. The contact and reaction must remain readable. A long fade between two silhouettes does not replace a movement phase.

Keep a supporting foot planted on the floor. Travel uses leg and arm movement. A jump, knockback, or levitation needs a clear reason. Levitation does not require a flip. Rotating a whole flat standing image does not replace body animation.

## Interface

| Element | Rule |
|---|---|
| Opening | Still fighters; 3 → 2 → 1, one second each; then remove the countdown |
| Top panels | Names, numerical HP, and a resource; for JJK, use CURSED ENERGY |
| Below the resource | That fighter's injury or received damage notice, for exactly three seconds |
| Bottom panel | Only the English name of the technique in use; empty during ordinary movements |
| Lasting states | Removing a notice does not undo the injury, damage, or resource loss |
| Numbers | Explain the invented model in the documentation, without an on-screen production note |

All screen text is in English. Do not add location names, exchange numbers, source links, or final explanation cards unless requested. HP and energy change because of events. Keep the story duration of an ability separate from the length of the edit.

## Pace and viewer attention

For a battle of similar complexity, aim for 60–90 seconds. A simple exchange fits a short test of about 7–13 seconds. Split a complex battle into parts when needed. Events determine the length, not the music track.

Viewer hooks keep the story order: a clear threat after the countdown; technique preparation and a possible response; a real counter; a change of advantage; a visible new ability effect; and a clear outcome. Do not add invented attacks, flash-forwards, or text clickbait.

## Sound

Choose the sound mode and music for each battle. Record the exact music file, the start of the selected part in the source, and its entry point in the video. “From 00:31” means playback from that position in the source track, not a 31-second pause.

Fit music to the edit with trimming and agreed transitions. Do not silently add loops or change speed. Place SFX (sound effects) at contact, step, transformation, healing, and technique frames. Keep the source audio, separate tracks, and a list of sound events.

Check for clipping and check the audio after encoding. Technical level measurements do not replace listening. If only the sound changes, review frames must match the approved visual version.

## Production and review

| Stage | Output | Main hooks |
|---|---|---|
| Research | Sources, limits, event sequence, and states | story_ready |
| Visual preparation | Image folders, references, arena, and pose sheets | assets_ready, scale_locked |
| Animation test | Clear action and reaction from both fighters | motion_ready |
| Full fight | Consistent poses, injuries, clothing, and surroundings | scene_exit, anatomy_locked, defeat_settled |
| Audio | Chosen music section and synchronized effects | audio_ready |
| Export and review | MP4, source files, review frames, and a report | before_export, after_export |
| Changes | Updated rules and a new output version | feedback_received |

Hooks are tasks for the agent at the right stage. They do not install background handlers. The timeline checker checks data; it does not recognize images or judge creative quality.

Remotion renders the final video. React/JSX defines the composition and timing. CSS/SVG creates the interface and effects. Transparent images and pose sequences represent the characters. Other tools can prepare drawings and audio. The finished MP4 does not replace the editable project.

## Completion criteria

The viewer understands the attack order, defense, and outcome through the action. Character models stay consistent between poses. Injuries and clothes continue across all transitions. Techniques have visible effects. Contact and interface changes happen together. Final states match the story. The video opens and plays from start to finish. Record completed technical, visual, and sound checks separately.

The release package contains the MP4, script, editable project, assets, dependency versions, render settings, current rules, and feedback log. Keep earlier versions. Specific JJK choices are listed in a [separate guide](../references/jjk.md); they do not automatically become rules for other works.
