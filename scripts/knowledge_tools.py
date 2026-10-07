"""Validate regional knowledge and render review documents, using only stdlib.

This checks editorial integrity. It does not validate medical accuracy and does
not enable the module in the application.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / 'reasoning_assistent' / 'knowledge'


def validate(module: dict) -> list[str]:
    errors: list[str] = []
    def need(obj, fields, where):
        if not isinstance(obj, dict):
            errors.append(f'{where}: expected object')
            return False
        for field in fields:
            if field not in obj:
                errors.append(f'{where}: missing {field}')
        return True
    need(module, ['schema_version', 'id', 'version', 'status', 'activation',
                  'scope', 'ai_rules', 'evidence_contract', 'questions',
                  'conditions', 'sources', 'review'], 'module')
    activation = module.get('activation', {})
    if not isinstance(activation, dict):
        errors.append('activation: expected object')
        activation = {}
    # These data-only drafts must remain disabled. Enabling requires a separate
    # reviewed integration; flipping a JSON flag is not an approval mechanism.
    if activation.get('automatic_advice_enabled') is not False:
        errors.append('data-only module must have automatic_advice_enabled=false')
    if module.get('status') == 'draft_requires_clinical_review' and activation.get('clinically_reviewed') is not False:
        errors.append('draft must have clinically_reviewed=false')
    collections = {}
    for key in ['questions', 'conditions', 'sources', 'shared_profiles', 'mechanism_context']:
        items = module.get(key, [])
        if not isinstance(items, list):
            errors.append(f'{key}: expected list')
            items = []
        ids = []
        for item in items:
            if not isinstance(item, dict) or not isinstance(item.get('id'), str) or not item['id']:
                errors.append(f'{key}: missing/invalid id')
            else:
                ids.append(item['id'])
        if len(ids) != len(set(ids)):
            errors.append(f'{key}: duplicate id')
        collections[key] = set(ids)
    def refs(item, field, allowed, where):
        values = item.get(field, [])
        if not isinstance(values, list):
            errors.append(f'{where}.{field}: expected list')
            return
        for ref in values:
            if not isinstance(ref, str) or ref not in allowed:
                errors.append(f'{where}.{field}: unresolved reference {ref!r}')
    for condition in module.get('conditions', []):
        if not isinstance(condition, dict):
            continue
        where = f"condition {condition.get('id', '?')}"
        need(condition, ['id', 'name', 'category', 'diagnostic_clues', 'risk_factors',
                         'question_ids', 'physical_assessment', 'prognostic_factors',
                         'therapeutically_modifiable_factors', 'referral', 'limitations',
                         'source_ids', 'evidence_status', 'review_status'], where)
        for field in ['diagnostic_clues', 'risk_factors', 'physical_assessment',
                      'prognostic_factors', 'therapeutically_modifiable_factors', 'limitations']:
            value = condition.get(field)
            if not isinstance(value, list) or not value or not all(isinstance(x, str) and x.strip() for x in value):
                errors.append(f'{where}.{field}: expected nonempty text list')
        refs(condition, 'question_ids', collections['questions'], where)
        refs(condition, 'source_ids', collections['sources'], where)
        referral = condition.get('referral', {})
        if need(referral, ['priority', 'action', 'route'], where + '.referral'):
            if referral.get('priority') not in ['routine', 'conditional']:
                errors.append(f'{where}: invalid referral priority')
            if not referral.get('action'):
                errors.append(f'{where}: missing referral action')
        if not condition.get('source_ids'):
            errors.append(f'{where}: source reference required')
    for key in ['questions', 'shared_profiles', 'mechanism_context']:
        for item in module.get(key, []):
            if isinstance(item, dict):
                refs(item, 'source_ids', collections['sources'], f"{key} {item.get('id')}")
    for source in module.get('sources', []):
        if isinstance(source, dict):
            need(source, ['id', 'title', 'url', 'year', 'type', 'scope', 'checked_on', 'access'], 'source')
    return errors


def render(module: dict) -> str:
    lines = [f"# {module['title']}", '',
             f"Versie {module['version']} — {module['created_on']}. Status: **concept; klinische review vereist**.", '',
             'Deze leesversie wordt gegenereerd uit het JSON-bestand. Pas de JSON aan en genereer dit document opnieuw.', '',
             'De module is nog niet gekoppeld aan automatische adviezen. Zij ondersteunt beoordeling door een fysiotherapeut; geen autonome diagnose of triage.', '']
    def heading(title, values, level=2):
        lines.extend(['#' * level + ' ' + title, ''])
        lines.extend('- ' + str(x) for x in values)
        lines.append('')
    scope = module['scope']
    lines.extend(['## Toepassingsgebied', '', scope['population'], '', scope['coverage'], ''])
    heading('Buiten de huidige dekking', scope['exclusions'])
    heading('Open inhoudelijke punten', scope['known_gaps'])
    heading('Regels voor AI-gebruik', module['ai_rules'])
    lines.extend(['## Vastleggen van gespreksbewijs', '',
                  'Toestanden: ' + ', '.join(module['evidence_contract']['states']) + '.', '',
                  'Verplichte velden: ' + ', '.join(module['evidence_contract']['required_fields']) + '.', '',
                  'Tijdscontext: ' + ', '.join(module['evidence_contract']['time_context_values']) + '.', '',
                  'Verificatie: ' + ', '.join(module['evidence_contract']['verification_values']) + '.', ''])
    heading('Bewijsregels', module['evidence_contract']['rules'], 3)
    for profile in module['shared_profiles']:
        lines.extend(['## ' + profile['title'], '', profile['applies_to'], ''])
        heading('Prognostische context', profile['prognostic_factors'], 3)
        heading('Beïnvloedbare factoren', profile['therapeutically_modifiable_factors'], 3)
        heading('Beperkingen', profile['limitations'], 3)
        lines.extend(['Bronnen: ' + ', '.join(profile['source_ids']), ''])
    for profile in module['mechanism_context']:
        lines.extend(['## ' + profile['title'], ''])
        heading('Aanwijzingen', profile['clues'], 3)
        heading('Beoordeling', profile['assessment'], 3)
        heading('Beperkingen', profile['limitations'], 3)
        lines.extend(['Bronnen: ' + ', '.join(profile['source_ids']), ''])
    lines.extend(['## Vragenbank', '',
                  'De vragen zijn eigen formuleringen, geen gevalideerde schaal. Een vraag kan worden overgeslagen als het antwoord al expliciet en betrouwbaar bekend is. Context en klinische relevantie bepalen welke vragen nodig zijn.', ''])
    for question in module['questions']:
        lines.extend([f"### {question['id']}", '', question['text'], '',
                      f"Wanneer: {question['ask_when']}. Doel: {question['purpose']}. Prioriteit: {question['priority']}.", '',
                      question['follow_up'], '',
                      'Bronnen: ' + (', '.join(question['source_ids']) or 'eigen contextvraag; geen specifieke diagnostische claim'), ''])
    lookup = {q['id']: q['text'] for q in module['questions']}
    for i, condition in enumerate(module['conditions'], 1):
        lines.extend([f"## {i}. {condition['name']}", '',
                      f"ID: {condition['id']}; categorie: {condition['category']}; review: {condition['review_status']}.", ''])
        for title, key in [('Diagnostische aanwijzingen', 'diagnostic_clues'), ('Risicofactoren', 'risk_factors'),
                           ('Vervolgvragen', 'question_ids'), ('Lichamelijk onderzoek en beperkingen', 'physical_assessment'),
                           ('Prognostische factoren', 'prognostic_factors'), ('Therapeutisch beïnvloedbare factoren', 'therapeutically_modifiable_factors')]:
            values = condition[key]
            if key == 'question_ids':
                values = [f'{q}: {lookup[q]}' for q in values]
            heading(title, values, 3)
        lines.extend(['### Overleg / verwijzing', '', condition['referral']['action'], '',
                      condition['referral']['route'], '',
                      'Prioriteit `conditional` betekent dat de beschreven context de urgentie bepaalt; geen automatisch spoedlabel voor iedereen met deze aandoening.', ''] if condition['referral']['priority'] == 'conditional' else ['### Overleg / verwijzing', '', condition['referral']['action'], '', condition['referral']['route'], ''])
        heading('Interpretatiegrenzen', condition['limitations'], 3)
        lines.extend(['Bronnen: ' + ', '.join(condition['source_ids']), '', condition['evidence_status'], ''])
    lines.extend(['## Bronnenregister', '',
                  'Bronnen ondersteunen de genoemde kern. Vragen, selectie, uitleg en vertaling naar een lokaal zorgpad zijn eigen operationalisering. Niet ieder onderdeel van een aandoening heeft afzonderlijk gevalideerde evidence. Oudere of beperkte bronnen en hiaten zijn expliciet gemarkeerd.', ''])
    for source in module['sources']:
        lines.extend([f"### {source['id']}", '', f"[{source['title']}]({source['url']})", '',
                      f"Bronjaar/gebruikte versie: {source['year']}; type: {source['type']}; gecontroleerd: {source['checked_on']}.", '',
                      source['scope'], '', source['access'], ''])
    heading('Benodigde inhoudelijke review', module['review']['required_review'])
    lines.extend([module['review']['notes'], ''])
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--render', action='store_true', help='regenerate readable region documents')
    args = parser.parse_args()
    paths = sorted(path for path in (KNOWLEDGE / 'regions').glob('*.json') if path.name != 'index.json')
    if not paths:
        raise SystemExit('No region modules found')
    errors = []
    for path in paths:
        module = json.loads(path.read_text(encoding='utf-8'))
        found = validate(module)
        errors.extend(f'{path.name}: {error}' for error in found)
        if not found and args.render:
            output = ROOT / 'docs' / 'knowledge' / (path.stem + '.md')
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(render(module), encoding='utf-8')
        print(f"{path.name}: {len(module['conditions'])} conditions, {len(module['questions'])} questions; {len(found)} errors")
    if errors:
        raise SystemExit('\n'.join(errors))


if __name__ == '__main__':
    main()
