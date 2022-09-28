import * as CodeMirror from "codemirror"
import * as CodeMirrorAutocomplete from "@codemirror/autocomplete"
import * as CodeMirrorCommands from "@codemirror/commands"
import * as CodeMirrorIndentationMarkers from '@replit/codemirror-indentation-markers'
import * as CodeMirrorLanguage from "@codemirror/language"
import * as CodeMirrorLint from "@codemirror/lint"
import * as CodeMirrorSearch from "@codemirror/search"
import * as CodeMirrorState from '@codemirror/state';
import * as CodeMirrorView from "@codemirror/view"

import * as CodeMirrorLangCpp from "@codemirror/lang-cpp"
import * as CodeMirrorLangCss from "@codemirror/lang-css"
import * as CodeMirrorLangHtml from "@codemirror/lang-html"
import * as CodeMirrorLangJava from "@codemirror/lang-java"
import * as CodeMirrorLangJavascript from "@codemirror/lang-javascript"
import * as CodeMirrorLangJson from "@codemirror/lang-json"
import * as CodeMirrorLangMarkdown from "@codemirror/lang-markdown"
import * as CodeMirrorLangPhp from "@codemirror/lang-php"
import * as CodeMirrorLangPython from "@codemirror/lang-python"
import * as CodeMirrorLangRust from "@codemirror/lang-rust"
import * as CodeMirrorLangSql from "@codemirror/lang-sql"
import * as CodeMirrorLangXml from "@codemirror/lang-xml"

window.CM6 = {
    ...CodeMirror,
    ...CodeMirrorAutocomplete,
    ...CodeMirrorCommands,
    ...CodeMirrorIndentationMarkers,
    ...CodeMirrorLanguage,
    ...CodeMirrorLint,
    ...CodeMirrorSearch,
    ...CodeMirrorState,
    ...CodeMirrorView,

    ...CodeMirrorLangCpp,
    ...CodeMirrorLangCss,
    ...CodeMirrorLangHtml,
    ...CodeMirrorLangJava,
    ...CodeMirrorLangJavascript,
    ...CodeMirrorLangJson,
    ...CodeMirrorLangMarkdown,
    ...CodeMirrorLangPhp,
    ...CodeMirrorLangPython,
    ...CodeMirrorLangRust,
    ...CodeMirrorLangSql,
    ...CodeMirrorLangXml
}
