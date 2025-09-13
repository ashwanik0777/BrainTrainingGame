"""Simple stats persistence and helper for CLI app."""
import json
import os
from datetime import datetime

class Stats:
    def __init__(self, path='data/scores.json'):
        self.path = path
        self._data = {}
        self._load()

    def _load(self):
        if os.path.exists(self.path):
            try:
                with open(self.path, 'r') as f:
                    self._data = json.load(f)
            except Exception:
                self._data = {}
        else:
            self._data = {}

    def _save(self):
        dname = os.path.dirname(self.path)
        if dname and not os.path.exists(dname):
            os.makedirs(dname, exist_ok=True)
        with open(self.path, 'w') as f:
            json.dump(self._data, f, indent=2)

    def update(self, game_key, result):
        """Update stored stats with a single session `result` dict."""
        now = datetime.utcnow().isoformat() + 'Z'
        g = self._data.setdefault(game_key, {})
        g['games_played'] = g.get('games_played', 0) + 1
        g['last_played'] = now

        if isinstance(result, dict):
            if 'score' in result:
                prev_high = g.get('high_score', 0)
                g['high_score'] = max(prev_high, result['score'])
                hist = g.setdefault('last_scores', [])
                hist.insert(0, {'score': result.get('score'), 'when': now})
                g['last_scores'] = hist[:5]
            if 'levels_reached' in result:
                prev_levels = g.get('max_levels', 0)
                g['max_levels'] = max(prev_levels, result['levels_reached'])

            if 'avg_reaction' in result:
                prev_best = g.get('best_reaction')
                if result.get('best_reaction') is not None:
                    if prev_best is None or result['best_reaction'] < prev_best:
                        g['best_reaction'] = result['best_reaction']
                g['last_avg_reaction'] = result.get('avg_reaction')

        self._data[game_key] = g
        self._save()

    def reset(self):
        self._data = {}
        self._save()

    def __str__(self):
        lines = ['Stats Summary\n' + '-'*40]
        if not self._data:
            return '\n'.join(lines + ['No stats yet — play some games!'])
        for k, v in self._data.items():
            lines.append(f"Game: {k}")
            for kk, vv in v.items():
                lines.append(f"  {kk}: {vv}")
            lines.append('-'*40)
        return '\n'.join(lines)