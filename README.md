# Battle to Arcade Game Video

A Codex skill that turns a fictional battle into an animated video in the style of a 2D arcade fighting game. The viewer sees each technique, the opponent's response, and the result through character movement, effects, and a game-style display.

**The output is a video, not a playable game.** Remotion renders the final video. This package contains instructions, a script template, and a timeline checker. It does not include a ready-made animation engine or character assets.

[Creative treatment](docs/EXPLICATION.md) · [Agent instructions](SKILL.md) · [Battle template](references/battle-template.md) · [Hooks](references/hooks.md) · [Change log](CHANGELOG.md)

## What you get

- A step-by-step script with sources, character states, and clear notes on adaptation.
- Approved character models, pose sheets, and separate layers for the arena, effects, and interface.
- An editable Remotion project, a playable MP4, and source materials.
- A review report covering state continuity, scale, anatomy, motion, text, sound, and export.

The standard format is 1920×1080 at 30 fps, with a side-view arena and a short 3–2–1 countdown. Screen text is in English. Working notes can use the project's chosen language. Technique names appear at the bottom. HP and resources appear at the top. Injury and damage notices appear below the resource bar for three seconds. HP and energy are an invented model explained in the documentation.

## Installation

Copy this folder into the Codex skills directory under the name `battle-to-arcade-game-video`. For a standard installation:

```sh
git clone https://github.com/Lennydeer/battle-to-arcade-game-video.git "$HOME/.codex/skills/battle-to-arcade-game-video"
```

If that folder already exists, back up your version first. The command above is for a new installation. If you use a custom `CODEX_HOME`, use its `skills` directory. After installation, start a new chat or refresh the available skills in your environment.

## Usage

```text
Use $battle-to-arcade-game-video. Prepare the battle [participants]
from [source, chapter, or episode]. Start and end: [limits].
Begin with the script and a short test. No sound for now.
```

To update an existing project:

```text
Use $battle-to-arcade-game-video. In the project at [path], fix the
character's size during walking and the final grab. Use the first
approved stance as the reference. Check all poses for both fighters
and render a new version.
```

Keep choices that have already been agreed. A request to edit only the script does not start a render. Ask about major new creative choices through interactive options, with context and the effect of each option.

## Process

1. Define the participants, start and end, and source. Write the actions, responses, and state changes.
2. Collect visual references as images and folders. Approve the characters and arena.
3. Test a short exchange: preparation → acceleration → contact → reaction → return.
4. Apply the approach to the full fight, keeping body size, anatomy, clothes, and attack results consistent.
5. Add the chosen music and SFX, then render and review the output.

Each stage has [production hooks](references/hooks.md): checks the agent performs at the right moment. They are not automatically installed system handlers. Viewer hooks keep attention through real threats, counters, and changes of advantage without changing the order of events.

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | Agent rules and workflow |
| `agents/openai.yaml` | Display name and example skill prompt |
| `references/battle-template.md` | Script template and states before and after actions |
| `references/hooks.md` | Production and viewer hooks; JSON format |
| `references/production.md` | Assets, Remotion, audio, review, and delivery |
| `references/jjk.md` | Local JJK series choices, not a universal source of story facts |
| `scripts/check_timeline.py` | Checks state snapshots and notice timing |
| `docs/EXPLICATION.md` | Creative treatment: concept, visual style, and production plan |

## Tools and dependencies

Use Remotion, React/JSX, CSS/SVG, local PNG/RGBA files, pose sequences, and an available image generation or editing tool. Music and SFX are separate tracks. FFmpeg and FFprobe help prepare and check media. Rendering needs compatible Node.js and Remotion dependencies, plus a browser. Record their versions in each project; this skill package does not include them. Image generation depends on the tools available in the user's environment.

`check_timeline.py` uses only the Python 3 standard library:

```sh
python3 scripts/check_timeline.py /path/to/project/timeline-review.json
```

See [hooks](references/hooks.md) for the data format. The checker does not recognize images, verify story facts, or judge animation and sound quality.

## Materials and scope

This repository contains text instructions and a checking script. It does not include frames from original works, music, character images, or finished videos. Check the rights and terms for production materials in each project. Keep original story facts, adaptation additions, and staging choices clearly separate.

## Summary

Create clear 2D battle videos with source-based choreography, consistent characters, lasting injuries and costume damage, expressive motion smears, English technique captions, HP and resource bars, and synchronized audio. The package guides production and review; it is not a game or a complete animation engine.
