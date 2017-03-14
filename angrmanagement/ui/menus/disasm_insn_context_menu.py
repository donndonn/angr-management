
from PySide.QtGui import QKeySequence
from PySide.QtCore import Qt

from .menu import Menu, MenuEntry, MenuSeparator

class DisasmInsnContextMenu(Menu):
    def __init__(self, disasm_view):
        super(DisasmInsnContextMenu, self).__init__(disasm_view, "&File")

        self.insn_addr = None

        self.entries.extend([
            MenuEntry('T&oggle selection', self._toggle_instruction_selection),
            MenuSeparator(),
            MenuEntry('E&xecute symbolically...', self._disasm_view.popup_newpath_dialog),
            MenuEntry('&Avoid in execution...', self._avoid_in_execution)
        ])

    @property
    def _disasm_view(self):
        return self.window

    def _toggle_instruction_selection(self): self._disasm_view.toggle_instruction_selection(self.insn_addr)

    def _avoid_in_execution(self): self._disasm_view.avoid_addr_in_exec(self.insn_addr)
