import markdown
from mdx_embedly import EmbedlyExtension


def test_embedly():
    s = "[https://github.com/yymm:embed]"
    expected = """
<p>
<a class="embedly-card" href="https://github.com/yymm">embed.ly</a>
<script async src="//cdn.embedly.com/widgets/platform.js" charset="UTF-8"></script>
</p>
    """.strip()
    html = markdown.markdown(s, extensions=[EmbedlyExtension()])
    assert html == expected


def test_gist():
    s = "[https://gist.github.com/yymm/726df7f0e4ed48e54a06:embed]"
    expected = """
<p>
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/gist-embed/2.4/gist-embed.min.js"></script>
<code data-gist-id="726df7f0e4ed48e54a06"></code>
</p>
    """.strip()
    html = markdown.markdown(s, extensions=[EmbedlyExtension()])
    assert html == expected
