#!/usr/bin/env python3
"""Catch presentation exports entering navigation or overwriting the notes app."""
from html.parser import HTMLParser
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_site'


class MainNavigation(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_nav = False
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'nav' and attrs.get('id') == 'nav':
            self.in_nav = True
        elif tag == 'a' and self.in_nav:
            self.links.append(attrs.get('href', ''))

    def handle_endtag(self, tag):
        if tag == 'nav':
            self.in_nav = False


def deck_data(text):
    return json.JSONDecoder().raw_decode(text.split('const DATA=', 1)[1])[0]


def main():
    for route in ['index.html', 'blog.html', 'presentations/index.html',
                  'blog/who-decides-when-ai-is-trustworthy/index.html',
                  'presentations/ucl-ai-trust/index.html']:
        parser = MainNavigation()
        parser.feed((SITE / route).read_text())
        leaks = [url for url in parser.links if url.startswith('/presentations/') and url != '/presentations/']
        if leaks:
            raise SystemExit(f'Presentation resource leaked into main navigation in {route}: {leaks}')
    public = SITE / 'presentations/ucl-ai-trust'
    slides = (public / 'slides.html').read_text()
    notes = (public / 'notes.html').read_text()
    for name, text in [('slides', slides), ('notes', notes)]:
        if 'const DATA=' not in text or '<div id="header">' in text or text.startswith('---'):
            raise SystemExit(f'The standalone {name} app was overwritten or wrapped as a site page')
    slide_data, note_data = deck_data(slides), deck_data(notes)
    if [x['key'] for x in slide_data] != [x['key'] for x in note_data]:
        raise SystemExit('Audience and presenter decks have different slide orders')
    for name in ['sources.html', 'notes-text.html']:
        if not (public / name).exists():
            raise SystemExit(f'Missing explicitly routed presentation resource: {name}')
    timeline = json.loads((ROOT / '_data/ai_trust_story.json').read_text())
    keys = {x['key'] for x in slide_data}
    article = (SITE / 'blog/who-decides-when-ai-is-trustworthy/index.html').read_text()
    for event in timeline:
        if event['slide'] not in keys or f'id="{event["id"]}"' not in article:
            raise SystemExit(f'Broken article timeline entry: {event["id"]}')
    print('Presentation publishing audit passed: navigation, app routes, notes order and timeline targets.')


if __name__ == '__main__':
    main()
