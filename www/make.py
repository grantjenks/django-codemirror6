#!/usr/bin/env python3
"""Make JS bundles for Code Mirror

Bundle like: codemirror-<language>-<variants>.js
Example: codemirror-sql-yjs.js

"""

import argparse
import collections
import functools
import subprocess
import sys
import tqdm

shell = functools.partial(subprocess.run, shell=True)
Import = collections.namedtuple('Import', 'name path star splat')

template = """{import_text}

window.CM6 = {{
{cm6_text}
}}
"""

base = [
    Import('CodeMirror', 'codemirror', True, True),
    Import('CodeMirrorAutocomplete', '@codemirror/autocomplete', True, True),
    Import('CodeMirrorCommands', '@codemirror/commands', True, True),
    Import(
        'CodeMirrorIndentationMarkers',
        '@replit/codemirror-indentation-markers',
        True,
        True,
    ),
    Import('CodeMirrorLanguage', '@codemirror/language', True, True),
    Import('CodeMirrorLint', '@codemirror/lint', True, True),
    Import('CodeMirrorSearch', '@codemirror/search', True, True),
    Import('CodeMirrorState', '@codemirror/state', True, True),
    Import('CodeMirrorView', '@codemirror/view', True, True),
]

languages = {
    'cpp': [Import('CodeMirrorLangCpp', '@codemirror/lang-cpp', True, True)],
    'css': [Import('CodeMirrorLangCss', '@codemirror/lang-css', True, True)],
    'html': [Import('CodeMirrorLangHtml', '@codemirror/lang-html', True, True)],
    'java': [Import('CodeMirrorLangJava', '@codemirror/lang-java', True, True)],
    'javascript': [
        Import('CodeMirrorLangJavascript', '@codemirror/lang-javascript', True, True)
    ],
    'json': [Import('CodeMirrorLangJson', '@codemirror/lang-json', True, True)],
    'markdown': [
        Import('CodeMirrorLangMarkdown', '@codemirror/lang-markdown', True, True)
    ],
    'php': [Import('CodeMirrorLangPhp', '@codemirror/lang-php', True, True)],
    'python': [
        Import('CodeMirrorLangPython', '@codemirror/lang-python', True, True)
    ],
    'rust': [Import('CodeMirrorLangRust', '@codemirror/lang-rust', True, True)],
    'sql': [Import('CodeMirrorLangSql', '@codemirror/lang-sql', True, True)],
    'xml': [Import('CodeMirrorLangXml', '@codemirror/lang-xml', True, True)],
    # 'yaml': [
    #     Import('StreamLanguage', '@codemirror/language', False, False),
    #     Import('yaml', '@codemirror/legacy-modes/mode/yaml', False, False),
    # ],
}

variants = {
    'yjs': [
        Import('Y', 'yjs', True, False),
        Import('WebrtcProvider', 'y-webrtc', False, False),
        Import('yCollab', 'y-codemirror.next', False, False),
    ],
}


def clean():
    shell('rm -f package-lock.json *.js')
    shell('rm -rf node_modules dist')


def setup():
    shell('npm install')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--clean', action='store_true')
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('--input', action='store_true')
    parser.add_argument('--setup', action='store_true')
    parser.add_argument('--language')
    parser.add_argument('--variant')
    args = parser.parse_args()

    if args.clean:
        clean()
        exit()

    if args.setup:
        setup()
        exit()

    rollup_args = '-p @rollup/plugin-node-resolve -p @rollup/plugin-commonjs'

    if args.debug:
        suffix = '.js'
    else:
        suffix = '.min.js'
        rollup_args += ' -p rollup-plugin-terser'

    name_parts = ['cm6']
    import_lines = []
    cm6_lines = []

    def add(name, path, star, splat):
        if star:
            import_line = f'import * as {name} from "{path}"'
        else:
            import_line = f'import {{ {name} }} from "{path}"'
        import_lines.append(import_line)
        if splat:
            cm6_line = f'    ...{name}'
        else:
            cm6_line = f'    {name}'
        cm6_lines.append(cm6_line)

    for name, path, star, splat in base:
        add(name, path, star, splat)

    if args.language == 'all':
        name_parts.append('all')
        for language, imports in languages.items():
            for name, path, star, splat in imports:
                add(name, path, star, splat)
    elif args.language in languages:
        name_parts.append(args.language)
        imports = languages[args.language]
        for name, path, star, splat in imports:
            add(name, path, star, splat)
    else:
        assert args.language is None

    if args.variant in variants:
        name_parts.append(args.variant)
        imports = variants[args.variant]
        for name, path, star, splat in imports:
            add(name, path, star, splat)
    else:
        assert args.variant is None

    import_text = '\n'.join(import_lines)
    cm6_text = ',\n'.join(cm6_lines)
    text = template.format(import_text=import_text, cm6_text=cm6_text)

    with open('input.js', 'w') as writer:
        writer.write(text)

    output = f'{"-".join(name_parts)}{suffix}'
    rollup = 'node_modules/.bin/rollup'
    shell(f'{rollup} input.js -f iife -o {output} {rollup_args}')

    if not args.input:
        shell('rm input.js')


if __name__ == '__main__':
    if sys.argv[1:] == ['all']:
        print('Generating all variants ...')
        clean()
        setup()
        builds = [
            ['./make.py'],
            ['./make.py', '--language', 'all'],
            *[['./make.py', '--language', language] for language in languages]
        ]
        others = [build + ['--variant', 'yjs'] for build in builds]
        commands = [*builds, *others]
        for command in tqdm.tqdm(commands):
            sys.argv = command
            main()
    else:
        main()
