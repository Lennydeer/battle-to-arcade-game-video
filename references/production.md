# Production and storage

## Materials

Compare the reference with the full pose sheet first. Use the available image generation tool and its current instructions to create or edit raster images. Do not replace a character drawing with a simple shape made in code. Check transparency in the alpha channel, not by the appearance of a black or checkerboard background. A prompt alone does not prove that the designs match.

Keep the arena, fighters, techniques, shadows, and HUD on separate layers. PNG/RGBA files, drawing sequences, and layered or rigged source files are the masters; the MP4 is only the output. Save exact prompts, references, sources, and asset versions. Do not depend only on files in a generator's cache. If the tool has limits, do not promise identical anatomy across separate generations.

## Final render: Remotion

Render the final video with Remotion. Other tools can prepare images, poses between key drawings, smears, effects, and the script. Keep the approved drawn animation. Do not use Hyperframes for the final export.

Build the timeline in a React/JSX composition with local images, CSS/SVG, and audio tracks. Calculate states and timing from the frame number so each render gives the same result. Do not use real-time timers or random values without a fixed seed. Render review frames from the same composition. Record the composition ID, versions, dependency lockfile, and settings. Before using an API, check the installed version and current official documentation.

When moving an older project, keep its editing, drawings, states, paths, smears, and audio. Compare sample frames and transitions with the approved version. Importing a finished MP4 is not the same as moving editable animation. Keep old Hyperframes source files as history, not as a required part of the new render.

Give the real command and paths for the current project. Do not copy absolute paths from another computer. If Node or the package manager is missing from PATH, first check the installed runtime. External media tools may prepare or inspect files, but must not secretly replace the final renderer. Find the specific cause of an error; do not silently change engines.

## Review and delivery

Save `source/`, assets, the lockfile, render settings, script, active design guidelines, feedback, review frames, and the QA (quality review) report next to the versioned MP4. Do not overwrite older versions. Do not use a copy of node_modules as a source archive; provide steps to install the same dependencies.

Check the actual resolution, frame rate, duration, decoding, audio track, and playback from start to finish. Keep visual review, text readability, choreography, and listening checks separate. Audio peak and RMS (average level) measurements do not prove that the mix sounds balanced. Record exactly what was checked and any limits. A decoder reporting no errors is not creative approval.

Show the MP4 using its absolute local path. Briefly state the changes and any important limits. Avoid technical detail unless asked. The video file must exist; a command finishing does not by itself prove that the output is correct.

## Audio

Keep the original music, separate music and SFX tracks, and the final mix. Record the exact file, `source_start`, `video_start`, trim, speed, and fades. “From 00:31” means the chosen part starts 31 seconds into the source track, not after 31 seconds of silence in the video. Fit the track to the edit; do not stretch the fight to fit the music. Do not add a loop or change speed without making that choice clear.

Sync SFX with contacts, steps, healing, transformations, and techniques. Save a cue list (a list of sound events) with the frame, type, level, and source. Use effects so the music and key hits remain clear. Check for clipping in the encoded MP4, not only in the WAV. For an audio-only change, compare frames with the approved video: the visuals must stay the same. Muted browser playback is not a listening review.

## Continuity review

Create a contact sheet showing every used pose at the same physical scale, including walking, picking up an object, and the ending. Compare body landmarks and volume, not only the image height. Check frames before, during, and after each change of model, injury, healing, camera, and object grab. Cropping and transparent margins must not change scale or support. A timeline data check cannot detect a wrong drawing.
