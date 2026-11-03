#!/usr/bin/env python3
"""Read-only timeline checks; visual/canon/audio QA remains manual."""
import argparse
import json
import math
import sys


def validate(data):
    errors = []
    def require(ok, message):
        if not ok:
            errors.append(message)
    def integer(x):
        return isinstance(x, int) and not isinstance(x, bool)
    def state_ok(state, label, ids=None):
        if not isinstance(state, dict) or not state:
            errors.append(f'{label}: expected nonempty fighter state object')
            return False
        if ids is not None:
            require(set(state) == ids, f'{label}: fighter IDs changed')
        for fighter, values in state.items():
            if not isinstance(values, dict):
                errors.append(f'{label}.{fighter}: expected object')
                continue
            for key in ('hp', 'energy'):
                value = values.get(key)
                require(isinstance(value, (int, float)) and not isinstance(value, bool)
                        and math.isfinite(value) and value >= 0,
                        f'{label}.{fighter}.{key}: expected finite number >= 0')
            require(isinstance(values.get('costume'), str) and bool(values['costume']),
                    f'{label}.{fighter}: costume state required')
        return True
    if not isinstance(data, dict):
        return ['root: expected object']
    fps, duration, intro = (data.get(k) for k in ('fps', 'duration_frames', 'intro_frames'))
    require(integer(fps) and fps > 0, 'fps: positive integer required')
    require(integer(duration) and duration > 0, 'duration_frames: positive integer required')
    if not integer(fps) or fps <= 0 or not integer(duration) or duration <= 0:
        return errors
    require(integer(intro) and intro == 3 * fps, 'intro_frames: expected 3 seconds')
    require(duration > 3 * fps, 'duration_frames: no action after intro')
    require(data.get('language') == 'en', 'language: screen language must be en')
    previous = data.get('initial')
    initial_valid = state_ok(previous, 'initial')
    ids = set(previous) if initial_valid else None
    events = data.get('events')
    if not isinstance(events, list) or not events:
        return errors + ['events: nonempty list required']
    event_frames = {}
    last_frame = -1
    for i, event in enumerate(events):
        label = f'events[{i}]'
        if not isinstance(event, dict):
            errors.append(f'{label}: expected object')
            continue
        event_id, frame = event.get('id'), event.get('frame')
        valid_id = isinstance(event_id, str) and bool(event_id)
        require(valid_id, f'{label}: nonempty id required')
        if valid_id:
            require(event_id not in event_frames, f'{label}: duplicate id {event_id}')
            event_frames[event_id] = frame
        require(integer(frame) and 3 * fps <= frame < duration, f'{label}: frame outside action')
        if integer(frame):
            require(frame >= last_frame, f'{label}: event order goes backwards')
            last_frame = frame
        before, after = event.get('before'), event.get('after')
        state_ok(before, label + '.before', ids)
        state_ok(after, label + '.after', ids)
        require(before == previous, f'{label}: before does not match previous after')
        previous = after
        caption = event.get('caption', '')
        require(isinstance(caption, str), f'{label}: caption must be string')
        require(not caption or caption == event.get('technique'),
                f'{label}: caption must be technique name or empty')
    notifications = data.get('notifications')
    if not isinstance(notifications, list):
        return errors + ['notifications: list required (may be empty)']
    for i, notice in enumerate(notifications):
        label = f'notifications[{i}]'
        if not isinstance(notice, dict):
            errors.append(f'{label}: expected object')
            continue
        start, end, event_id = (notice.get(k) for k in ('start', 'end', 'event_id'))
        valid_id = isinstance(event_id, str) and event_id in event_frames
        require(valid_id, f'{label}: unknown event_id')
        require(integer(start) and integer(end), f'{label}: integer start/end required')
        if integer(start) and integer(end):
            require(end - start == 3 * fps, f'{label}: notification must last 3 seconds')
            require(0 <= start < end <= duration, f'{label}: clipped by video boundary')
            if valid_id:
                require(start == event_frames[event_id], f'{label}: start differs from event frame')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest')
    args = parser.parse_args()
    try:
        with open(args.manifest, encoding='utf-8') as source:
            errors = validate(json.load(source))
    except (OSError, ValueError) as exc:
        errors = [str(exc)]
    print(json.dumps({'ok': not errors, 'errors': errors}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
