import { EditorState } from '@codemirror/state';
import { EditorView, keymap, showPanel } from "@codemirror/view"
import { autocompletion } from "@codemirror/autocomplete"
import { basicSetup } from "codemirror"
import { indentWithTab } from "@codemirror/commands"
import { indentationMarkers } from '@replit/codemirror-indentation-markers'

window.EditorState = EditorState
window.EditorView = EditorView
window.autocompletion = autocompletion
window.basicSetup = basicSetup
window.indentWithTab = indentWithTab
window.indentationMarkers = indentationMarkers
window.keymap = keymap
window.showPanel = showPanel
