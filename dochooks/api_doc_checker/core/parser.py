import docutils.frontend
import docutils.nodes
import docutils.parsers.rst
import docutils.utils

from ..core.directives import preset_sphinx_directives
from ..core.roles import preset_sphinx_roles


def parse_rst(text: str, file_path: str) -> docutils.nodes.document:
    parser = docutils.parsers.rst.Parser()

    preset_sphinx_roles()
    preset_sphinx_directives()

    components = (docutils.parsers.rst.Parser,)
    settings = docutils.frontend.OptionParser(components=components).get_default_values()
    document = docutils.utils.new_document(file_path, settings=settings)
    parser.parse(text, document)
    return document
