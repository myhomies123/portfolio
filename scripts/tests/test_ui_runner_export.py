import copy
import unittest

import nbformat
from nbconvert import MarkdownExporter
from scripts.convert_notebooks import process_custom_cells, inject_code_runners


class UiRunnerExportTests(unittest.TestCase):
    def test_executed_runners_export_once_without_losing_notebook_evidence(self):
        cells = []
        for name in ('first', 'second'):
            markup = f'<div id="{name}"><button>Run {name}</button></div>'
            cell = nbformat.v4.new_code_cell(
                '%%html\n<!-- UI_RUNNER: sample -->\n' + markup,
                execution_count=1,
                outputs=[nbformat.v4.new_output('display_data', data={'text/html': markup})],
            )
            cells.append(cell)
        saved = nbformat.v4.new_notebook(cells=cells)
        conversion = process_custom_cells(copy.deepcopy(saved), '/test/')
        markdown, _ = MarkdownExporter().from_notebook_node(conversion)
        exported = inject_code_runners(markdown, conversion)
        for name in ('first', 'second'):
            self.assertEqual(exported.count(f'id="{name}"'), 1)
        self.assertTrue(all(cell.outputs for cell in saved.cells))

    def test_regular_html_outputs_are_preserved(self):
        cell = nbformat.v4.new_code_cell(
            '%%html\n<p>Ordinary HTML</p>', execution_count=1,
            outputs=[nbformat.v4.new_output('display_data', data={'text/html': '<p>Ordinary HTML</p>'})],
        )
        result = process_custom_cells(nbformat.v4.new_notebook(cells=[cell]), '/test/')
        self.assertEqual(result.cells[0].outputs[0].data['text/html'], '<p>Ordinary HTML</p>')


if __name__ == '__main__':
    unittest.main()
