This is a tool for creating simple <a href="http://www.angelcode.com/products/bmfont/">Bitmap Fonts</a> from a pixel art spritesheet. I use it for adding simple pixel-art fonts in <a href="https://godotengine.org/">Godot</a>.


It is a Python script, so you'll need <a href="https://www.python.org/">Python</a> (and the <a href="https://github.com/python-pillow/Pillow">Pillow</a> library). After that, simply run <i>py pxlfont.py</i>.


Info for parsing the font can be provided via a small configuration text-file (recommended), or manually in the Python window (cumbersome).

The config file parameters are as follows:
<ul><li><b>name</b> -- The font name</li>
<li><b>alph</b> -- The alphabet<ul><li>Each char in the sprite-sheet, in order.</li><li>No line breaks--the script will figure these out on its own.</li><li>No spaces, unless you are indicating a space character.</li></ul></li>
<li><b>lheight</b> -- Line height for this font (pixels)</li>
<li><b>base</b> -- Pixels from top of line to base of glyphs (defaults to lheight)</li>
<li><b>width</b> -- Character widths.<ul><li>Separate multiple widths with commas.</li><li>If all chars are the same width, only 1 number is needed.</li></ul></li>
<li><b>tail</b> -- The amount of unused space at the end of the rows.<ul><li>Defaults to 0.</li><li>Separate multiple tales with commas.</li><li>If all rows have the same tail size, only 1 number is needed.</li></ul></li></ul>

The script will ask for the image file path, then ask if you have a config file. Alternately, you can supply these as arguments, i.e.: <i>py pxlfont.py spritesheet.png cfg.txt</i>.

The output is a .fnt file containing the Bitmap Font info in text format. You'll need to have the .fnt in the same folder as your spritesheet for it to work!

This uses <a href="https://github.com/python-pillow/Pillow">Pillow</a> for parsing the image file.
