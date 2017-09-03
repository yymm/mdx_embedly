from markdown import Extension
from markdown.postprocessors import Postprocessor
import re

GIST_RE = r"^http(?:s)?://gist\.github\.com/.+$"

class EmbedlyExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add('embed', EmbedlyPostprocesser(self), '>raw_html')


class EmbedlyPostprocesser(Postprocessor):

    _pattern = re.compile(r"\[(http(s)?(://[\w:;/.?%#&=+-]+)):embed\]")

    def run(self, html):
        html = re.sub(self._pattern, self._replace_embed, html) 
        return html

    def _replace_embed(self, match):
        url = match.group(1)
        if re.match(GIST_RE, url):
            gist_id = url.split("/")[4]
            return """
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/gist-embed/2.4/gist-embed.min.js"></script>
<code data-gist-id="{}"></code>
""".format(gist_id)
        title = "embed.ly"
        return """
<a class="embedly-card" href="{0}">{1}</a>
<script async src="//cdn.embedly.com/widgets/platform.js" charset="UTF-8"></script>
""".format(url, title)


def makeExtension(*args, **kwargs):
    return EmbedlyExtension(*args, **kwargs)
