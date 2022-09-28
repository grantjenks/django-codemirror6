SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

ifeq ($(origin .RECIPEPREFIX), undefined)
  $(error Make does not support .RECIPEPREFIX. Use GNU Make 4+, AKA gmake.)
endif
.RECIPEPREFIX = >

ROLLUP_ARGS = -p @rollup/plugin-node-resolve -p @rollup/plugin-commonjs

build: ROLLUP_ARGS += -p rollup-plugin-terser
build: cm6.min.js
.PHONY: build

debug: cm6.min.js
.PHONY: debug

# codemirror.min.js: package-lock.json codemirror.js
# > echo $(ROLLUP_ARGS)
# > node_modules/.bin/rollup codemirror.js -f iife -o codemirror.min.js \
# >    $(ROLLUP_ARGS)

# codemirror-sql.min.js: package-lock.json codemirror-sql.js
# > node_modules/.bin/rollup codemirror-sql.js -f iife -o codemirror-sql.min.js \
# >    $(ROLLUP_ARGS)

# y-codemirror.min.js: package-lock.json y-codemirror.js
# > node_modules/.bin/rollup y-codemirror.js -f iife -o y-codemirror.min.js \
# >    $(ROLLUP_ARGS)

# codemirror-all.js: codemirror.js codemirror-sql.js y-codemirror.js
# > cat codemirror.js codemirror-sql.js y-codemirror.js > codemirror-all.js

# codemirror-all.min.js: codemirror-all.js
# > node_modules/.bin/rollup codemirror-all.js -f iife -o codemirror-all.min.js \
# >    $(ROLLUP_ARGS)

cm6.min.js: package-lock.json cm6.js
> echo $(ROLLUP_ARGS)
> node_modules/.bin/rollup cm6.js -f iife -o cm6.min.js \
>    $(ROLLUP_ARGS)

package-lock.json: package.json
> npm install

clean:
> rm -f *.min.js
> rm -f codemirror-all.js
> rm -f package-lock.json
> rm -rf node_modules
.PHONY: clean
